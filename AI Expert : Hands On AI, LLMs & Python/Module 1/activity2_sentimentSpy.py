import sys
import subprocess

# ---------------------------
# Try to import required libs
# ---------------------------
try:
    from colorama import Fore, Style, init as colorama_init
except ImportError:
    print("colorama not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import Fore, Style, init as colorama_init

try:
    from textblob import TextBlob
except ImportError:
    print("textblob not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "textblob"])
    # textblob may need corpora; try to download them (works in Colab/with internet)
    try:
        import textblob
        textblob.download_corpora.download_all()
    except Exception:
        # If download fails, it's okay; polarity might still work in some environments.
        print("Warning: Could not download TextBlob corpora automatically.")
    from textblob import TextBlob

# Initialize colorama (makes colored text work on Windows)
colorama_init(autoreset=True)

import random

# ---------------------------
# 2) INITIAL GREETING
# ---------------------------
print(Fore.CYAN + "👋  Hello! Welcome to the Sentiment Chat Program. 🕵️‍♀️")
print(Fore.CYAN + "This simple program will analyze how your sentences feel (positive/neutral/negative).")
print()

# ---------------------------
# 3) USER NAME INPUT
# ---------------------------
name = input("What's your name? : ").strip()
if not name:
    name = "Mystery Agent"
print(f"Nice to meet you, {name}!")
print()

# ---------------------------
# 4) CONVERSATION HISTORY
# ---------------------------
# We'll store tuples: (user_text, polarity_float, sentiment_string)
history = []

# ---------------------------
# 5) INSTRUCTIONS
# ---------------------------
print("You can type sentences to see their sentiment.")
print("Special commands:")
print("  reset   -> clear conversation history")
print("  history -> show past inputs with sentiment")
print("  exit    -> end the program")
print()

# ---------------------------
# Helper: determine sentiment
# ---------------------------
def classify_sentiment(polarity: float) -> str:
    """
    Return a sentiment label from polarity:
      >  0.25 => Positive
      < -0.25 => Negative
      else    => Neutral
    """
    if polarity > 0.25:
        return "Positive"
    if polarity < -0.25:
        return "Negative"
    return "Neutral"

def print_colored_sentiment(sentiment: str, polarity: float, text: str):
    """
    Print a single line showing text, sentiment and polarity with colors and emoji.
    Kept simple for kids.
    """
    pol_text = f"{polarity:.2f}"
    if sentiment == "Positive":
        emoji = "😊"
        color = Fore.GREEN
    elif sentiment == "Negative":
        emoji = "😢"
        color = Fore.RED
    else:
        emoji = "😐"
        color = Fore.YELLOW

    print(color + f"{emoji}  \"{text}\"  -> {sentiment} (polarity {pol_text})" + Style.RESET_ALL)

# ---------------------------
# 6) MAIN INTERACTION LOOP
# ---------------------------
while True:
    user_input = input("\nType something (or a command): ").strip()
    if user_input == "":
        print(Fore.MAGENTA + "You typed nothing — try writing a sentence or a command (history/reset/exit).")
        continue

    cmd = user_input.lower()

    # 6.1) 'exit' COMMAND
    if cmd == "exit":
        print(Fore.CYAN + f"Goodbye, {name}! Thanks for trying the Sentiment Chat. 👋")
        break

    # 6.2) 'reset' COMMAND
    if cmd == "reset":
        history.clear()
        print(Fore.CYAN + "Conversation history cleared. You can start fresh now.")
        continue

    # 6.3) 'history' COMMAND
    if cmd == "history":
        if not history:
            print(Fore.MAGENTA + "No conversation history yet. Say something first!")
            continue
        print(Fore.CYAN + "\n--- Conversation History ---")
        for i, (text, polarity, sentiment) in enumerate(history, start=1):
            # Print each with color and emoji
            print_colored_sentiment(sentiment, polarity, text)
        print(Fore.CYAN + "--- End of History ---\n")
        continue

    # 6.4) SENTIMENT ANALYSIS
    # Use TextBlob to get polarity (-1.0 .. +1.0)
    try:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity  # float
    except Exception as e:
        # If TextBlob fails for any reason, fallback to neutral
        print(Fore.RED + "Oops — sentiment analysis failed. Treating as neutral.")
        polarity = 0.0

    sentiment_type = classify_sentiment(polarity)

    # Append to history
    history.append((user_input, polarity, sentiment_type))

    # Choose a friendly reply based on sentiment
    if sentiment_type == "Positive":
        replies = [
            "That's great to hear! Keep it up! 🎉",
            "Yay! That sounds lovely. 😊",
            "Nice! Your sentence feels positive."
        ]
    elif sentiment_type == "Negative":
        replies = [
            "I'm sorry you're feeling that way. If you want, tell me more. 💬",
            "That sounds tough. I hope things get better soon. 🌱",
            "I hear you. It's OK to feel sad sometimes."
        ]
    else:
        replies = [
            "Hmm — that seems pretty neutral.",
            "I can't tell strong feelings from that; it seems calm.",
            "Neutral detected — sometimes that's fine!"
        ]

    # Print the result with colored sentiment and one friendly reply
    print_colored_sentiment(sentiment_type, polarity, user_input)
    print(Fore.CYAN + random.choice(replies))