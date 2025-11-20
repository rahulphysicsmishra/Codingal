# movie_recommender.py

import random
import time
import sys
import subprocess
import re

# Ensure TextBlob is available
try:
    from textblob import TextBlob
except Exception:
    print("TextBlob not found. Attempting to install...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "textblob"])
    try:
        from textblob import TextBlob
    except Exception:
        print("Warning: TextBlob installation failed. Sentiment will be limited.")
        TextBlob = None

# Try colorama
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except Exception:
    class _F: RED = GREEN = YELLOW = CYAN = MAGENTA = BLUE = RESET = ""
    Fore = _F()
    Style = _F()

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# Load & preprocess
# ---------------------------
def load_data(file_path='/content/imdb_top_1000.csv'):
    """
    Load CSV and normalize columns to Title, Genre, Overview, IMDb_Rating, combined_features.
    Expects Series_Title and IMDB_Rating in the CSV as provided.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(Fore.RED + f"Error: File '{file_path}' not found. Put it in same folder or change the path.")
        sys.exit(1)

    # Check required columns exist
    expected = ['Series_Title', 'Genre', 'Overview', 'IMDB_Rating']
    missing = [c for c in expected if c not in df.columns]
    if missing:
        print(Fore.RED + f"Error: Dataset is missing columns: {missing}")
        print("Found columns:", ", ".join(df.columns))
        sys.exit(1)

    # Rename for internal consistency
    df = df.rename(columns={'Series_Title': 'Title', 'IMDB_Rating': 'IMDb_Rating'})

    # Build combined features (Genre + Overview)
    df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')

    # Ensure rating numeric
    df['IMDb_Rating'] = pd.to_numeric(df['IMDb_Rating'], errors='coerce').fillna(0.0)

    # Keep only useful columns
    keep_cols = ['Title', 'Genre', 'Overview', 'IMDb_Rating', 'combined_features']
    for c in keep_cols:
        if c not in df.columns:
            df[c] = ''
    return df[keep_cols]

# ---------------------------
# Vectorize & sentiment helpers
# ---------------------------
def vectorize_text(df):
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    matrix = tfidf.fit_transform(df['combined_features'].values)
    return matrix, tfidf

def analyze_sentiment(text):
    if TextBlob is None:
        return 0.0, 'Neutral'
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0.25:
        label = 'Positive'
    elif polarity < -0.25:
        label = 'Negative'
    else:
        label = 'Neutral'
    return polarity, label

def processing_animation(message="Processing", duration=1.0, steps=5):
    print(Fore.CYAN + message, end='', flush=True)
    for _ in range(steps):
        print(Fore.CYAN + '.', end='', flush=True)
        time.sleep(duration / steps)
    print()

# ---------------------------
# Genre listing helper
# ---------------------------
def list_genres(df):
    all_genres = set()
    for g in df['Genre'].fillna(''):
        for part in re.split(r',|\|', str(g)):
            part = part.strip()
            if part:
                all_genres.add(part)
    return sorted(all_genres)

# ---------------------------
# Recommendation logic
# ---------------------------
def recommend_movies(df, tfidf_matrix, title_based=None, genre_choice=None, min_rating=0.0,
                     mood_label=None, top_n=5, randomize=True):
    candidates = df.copy()
    # Genre filter
    if genre_choice:
        candidates = candidates[candidates['Genre'].str.contains(re.escape(genre_choice), case=False, na=False)]
    # Rating filter
    candidates = candidates[candidates['IMDb_Rating'] >= float(min_rating)]
    if candidates.empty:
        return []

    # Title-based with cosine similarity
    if title_based:
        matches = candidates[candidates['Title'].str.lower().str.contains(title_based.lower())]
        if matches.empty:
            matches = df[df['Title'].str.lower().str.contains(title_based.lower())]
        if matches.empty:
            exact = df[df['Title'].str.lower() == title_based.lower()]
            if not exact.empty:
                matches = exact
        if matches.empty:
            seed_idx = None
        else:
            seed_title = matches.iloc[0]['Title']
            # get positional index into df (iloc index)
            seed_idx_list = df.index[df['Title'] == seed_title].tolist()
            seed_idx = seed_idx_list[0] if seed_idx_list else None

        if seed_idx is not None:
            sims = cosine_similarity(tfidf_matrix[seed_idx], tfidf_matrix).flatten()
            sim_indices = sims.argsort()[::-1]
            results = []
            for idx in sim_indices:
                if idx == seed_idx:
                    continue
                row = df.iloc[idx]
                if row['IMDb_Rating'] < min_rating:
                    continue
                if genre_choice and genre_choice.lower() not in str(row['Genre']).lower():
                    continue
                polarity, sentiment = analyze_sentiment(row['Overview'])
                results.append({
                    'Title': row['Title'],
                    'Genre': row['Genre'],
                    'IMDb_Rating': row['IMDb_Rating'],
                    'Overview': row['Overview'],
                    'Polarity': polarity,
                    'Sentiment': sentiment,
                    'Similarity': float(sims[idx])
                })
                if len(results) >= top_n * 4:
                    break
            if randomize:
                random.shuffle(results)
            results_sorted = sorted(results, key=lambda x: x['Similarity'], reverse=True)
            return results_sorted[:top_n]
        # else fall through to non-title flow

    # Non-title flow: sentiment matching
    sentiments = []
    for _, row in candidates.iterrows():
        polarity, label = analyze_sentiment(row['Overview'])
        sentiments.append((polarity, label))
    candidates = candidates.reset_index(drop=True)
    candidates['Polarity'] = [p for p, _ in sentiments]
    candidates['Sentiment'] = [l for _, l in sentiments]

    if mood_label:
        filtered = candidates[candidates['Sentiment'] == mood_label]
        if filtered.empty:
            filtered = candidates[
                (candidates['Sentiment'] == mood_label) |
                (candidates['Sentiment'] == 'Neutral')
            ]
            if filtered.empty:
                filtered = candidates
        candidates = filtered

    results = []
    for _, row in candidates.iterrows():
        results.append({
            'Title': row['Title'],
            'Genre': row['Genre'],
            'IMDb_Rating': row['IMDb_Rating'],
            'Overview': row['Overview'],
            'Polarity': float(row['Polarity']),
            'Sentiment': row['Sentiment']
        })

    if randomize:
        random.shuffle(results)
    results_sorted = sorted(results, key=lambda x: x['IMDb_Rating'], reverse=True)
    return results_sorted[:top_n]

def display_recommendations(recs):
    if not recs:
        print(Fore.MAGENTA + "No suitable movies were found. Try relaxing filters.")
        return
    print(Fore.CYAN + f"\nTop {len(recs)} Recommendations:\n")
    for i, r in enumerate(recs, start=1):
        sentiment_color = Fore.GREEN if r.get('Sentiment') == 'Positive' else (Fore.RED if r.get('Sentiment') == 'Negative' else Fore.YELLOW)
        print(Fore.BLUE + f"{i}. {r['Title']}  ({r['Genre']})  Rating: {r['IMDb_Rating']}")
        print(sentiment_color + f"   Sentiment: {r.get('Sentiment')}  Polarity: {r.get('Polarity'):.2f}")
        overview = (r.get('Overview') or "").strip()
        short = (overview[:200] + '...') if len(overview) > 200 else overview
        print(Fore.RESET + f"   Overview: {short}\n")

# ---------------------------
# Main interactive flow
# ---------------------------
def main():
    print(Fore.CYAN + "🎬 Welcome to the Simple Movie Recommender (fixed columns)!")
    print("This demo uses content-based filtering + sentiment analysis.\n")

    movies_df = load_data()  # expects imdb_top_1000.csv with the given columns

    processing_animation("Vectorizing movie data")
    tfidf_matrix, vectorizer = vectorize_text(movies_df)

    # Precompute sentiment for quick filtering
    movies_df['Polarity'], movies_df['Sentiment'] = zip(*movies_df['Overview'].fillna('').map(lambda t: analyze_sentiment(t)))

    print(Fore.CYAN + "Pick a genre or type 'any' to skip. Some options are:")
    genres = list_genres(movies_df)
    print(Fore.GREEN + ", ".join(genres[:20]) + ("..." if len(genres) > 20 else ""))

    genre_choice = input(Fore.YELLOW + "Genre (or 'any'): ").strip()
    if genre_choice.lower() in ('any', ''):
        genre_choice = None

    while True:
        min_rating_input = input(Fore.YELLOW + "Minimum IMDb rating (0-10, default 6.0): ").strip()
        if min_rating_input == "":
            min_rating = 6.0
            break
        try:
            min_rating = float(min_rating_input)
            if 0 <= min_rating <= 10:
                break
            else:
                print(Fore.RED + "Enter a number between 0 and 10.")
        except ValueError:
            print(Fore.RED + "Please enter a valid number (e.g., 7 or 6.5).")

    print(Fore.CYAN + "How are you feeling right now? (type a short sentence or word)")
    mood_text = input(Fore.YELLOW + "I feel: ").strip()
    mood_polarity, mood_label = analyze_sentiment(mood_text)
    print(Fore.CYAN + f"Interpreted mood as: {mood_label} (polarity {mood_polarity:.2f})")

    seed = input(Fore.YELLOW + "Type a movie title to find similar movies (or press Enter to skip): ").strip()
    if seed == "":
        seed = None

    while True:
        top_n_input = input(Fore.YELLOW + "How many recommendations would you like? (default 5): ").strip()
        if top_n_input == "":
            top_n = 5
            break
        try:
            top_n = int(top_n_input)
            if top_n > 0:
                break
            else:
                print(Fore.RED + "Enter a positive integer.")
        except ValueError:
            print(Fore.RED + "Enter a number like 3 or 5.")

    processing_animation("Analyzing mood and preferences", duration=1.0)
    processing_animation("Searching for good matches", duration=1.0)

    recs = recommend_movies(
        df=movies_df,
        tfidf_matrix=tfidf_matrix,
        title_based=seed,
        genre_choice=genre_choice,
        min_rating=min_rating,
        mood_label=mood_label,
        top_n=top_n,
        randomize=True
    )

    display_recommendations(recs)
    print(Fore.CYAN + "Thanks for using the Simple Movie Recommender!")

if __name__ == "__main__":
    main()