
# Features: improved input handling, simulated weather, simulated news,
# local time for cities, colored output, and notes where NLP would help.

import re
import random
import sys
from datetime import datetime, timedelta

# Try to import colorama for colored text; if missing, tell the user how to install.
try:
    from colorama import Fore, Style, init
except ImportError:
    print("Optional dependency 'colorama' not found.")
    print("Install it for colored output: pip install colorama")
    # Provide simple fallback (no colors) by creating dummy constants
    class Dummy:
        RESET_ALL = ""
    class F:
        RED = GREEN = YELLOW = CYAN = MAGENTA = BLUE = ""
    Fore = F()
    Style = Dummy()
else:
    init(autoreset=True)  # makes prints return to normal after each colored print

# -----------------------
# Data stores (simple)
# -----------------------
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rockies", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why are computers so smart? They listen to their motherboards!"
]

advice = [
    "Pack light and bring a reusable water bottle.",
    "Keep a photocopy of important documents.",
    "Charge devices and bring adaptors if needed."
]

# Simulated news headlines 
simulated_news = [
    "Local park to host science fair this weekend.",
    "New library opening downtown with cool robotics workshops.",
    "City announces extra bike lanes for safer commuting."
]

# Simulated weather descriptions for demonstration
weather_samples = {
    "sunny": ["Sunny and warm ☀️", "Clear skies all day. Bring sunglasses!"],
    "rainy": ["Light rain showers 🌧️", "Heavy rain likely. Bring an umbrella!"],
    "cloudy": ["Mostly cloudy ☁️", "Overcast with cool temperatures."],
    "snow": ["Snow expected ❄️", "Cold and snowy — dress warmly!"]
}

# Helpful city -> UTC offset mapping (hours). Simple and small — for teaching.
city_timezones = {
    "new york": -5,
    "london": 0,
    "paris": 1,
    "tokyo": 9,
    "delhi": 5.5,
    "sydney": 10,
    "los angeles": -8
}

# -----------------------
# Input handling helpers
# -----------------------
# Compile some regexes once (faster & easier to read)
RE_RECOMMEND = re.compile(r"\b(recommend|suggest|where|go|trip|vacation)\b")
RE_PACK = re.compile(r"\b(pack|packing|luggage|bag)\b")
RE_JOKE = re.compile(r"\b(joke|funny|laugh)\b")
RE_HELP = re.compile(r"\b(help|options|show)\b")
RE_EXIT = re.compile(r"\b(exit|bye|quit|goodbye)\b")
RE_WEATHER = re.compile(r"\b(weather|forecast|rain|sunny|snow)\b")
RE_NEWS = re.compile(r"\b(news|headline|update)\b")
RE_TIME = re.compile(r"\b(time|clock|local time)\b")
RE_HISTORY = re.compile(r"\b(history|past|log)\b")
RE_REPEAT = re.compile(r"\b(repeat|again)\b")
RE_JUST_TEXT = re.compile(r"[a-zA-Z]")  # detect if there's any letter

# Normalize input text: strip spaces, lowercase, collapse spaces
def normalize_input(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())

# Slightly smarter "contains" check using regex keywords
def matches_any(regex, text: str) -> bool:
    return bool(regex.search(text))

# -----------------------
# Conversation history
# -----------------------
# Stores tuples (user_text, intent_label)
history = []

# -----------------------
# Bot functionality
# -----------------------
def show_help():
    print(Fore.MAGENTA + "\nI can help with:")
    print(Fore.GREEN + "- Recommendations (say 'recommend' or 'suggest')")
    print(Fore.GREEN + "- Packing tips (say 'packing' or 'pack')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Simulated weather (say 'weather')")
    print(Fore.GREEN + "- Simulated news (say 'news')")
    print(Fore.GREEN + "- Local time in a city (say 'time' and a city)")
    print(Fore.CYAN + "Other commands: 'history', 'repeat', 'help', 'exit'\n")

def recommend(user_text=""):
    # If user already named a preference in the input, try to extract it.
    # Very simple parsing: check for known destination types.
    pref = None
    for key in destinations:
        if key in user_text:
            pref = key
            break

    if not pref:
        print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities? Which do you like?")
        pref = normalize_input(input(Fore.YELLOW + "You: "))

    pref = pref.lower()
    if pref in destinations:
        suggestion = random.choice(destinations[pref])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = normalize_input(input(Fore.YELLOW + "You: "))
        if "yes" in answer:
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
            history.append((f"Requested recommendation: {pref}", "recommendation/accepted"))
            return
        else:
            print(Fore.YELLOW + "TravelBot: No worries, let me suggest another.")
            # Suggest again but keep it simple (no infinite recursion)
            options = [d for d in destinations[pref] if d != suggestion]
            if options:
                suggestion2 = random.choice(options)
                print(Fore.GREEN + f"TravelBot: How about {suggestion2}?")
                history.append((f"Requested recommendation: {pref}", "recommendation/retry"))
            else:
                print(Fore.RED + "TravelBot: That's all I have for that category.")
    else:
        print(Fore.RED + "TravelBot: I don't know that category. Try 'beaches', 'mountains', or 'cities'.")

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where are you going? (type a city or place)")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days will you stay?")
    days = normalize_input(input(Fore.YELLOW + "You: "))
    # Basic validation
    try:
        days_int = int(days.split()[0])
        day_text = f"{days_int} day{'s' if days_int != 1 else ''}"
    except Exception:
        day_text = days or "a few days"
    print(Fore.GREEN + f"TravelBot: Packing tips for {day_text} in {location.title()}:")
    print(Fore.GREEN + "- Pack versatile clothes you can mix and match.")
    print(Fore.GREEN + "- Don't forget chargers and a small first-aid kit.")
    print(Fore.GREEN + "- Carry a reusable water bottle and snacks.")
    history.append((f"Asked packing tips for {location} ({day_text})", "packing"))

def tell_joke():
    joke = random.choice(jokes)
    print(Fore.YELLOW + "TravelBot: " + joke)
    history.append((joke, "joke"))

def simulated_weather(user_text=""):
    # Try to detect a city name in user_text by simple matching to city_timezones keys
    city = None
    for c in city_timezones.keys():
        if c in user_text:
            city = c
            break

    if not city:
        print(Fore.CYAN + "TravelBot: Which city's weather would you like? (e.g., Tokyo, Paris)")
        city = normalize_input(input(Fore.YELLOW + "You: "))

    # Choose a random weather type
    wtype = random.choice(list(weather_samples.keys()))
    desc = random.choice(weather_samples[wtype])
    print(Fore.GREEN + f"TravelBot: Simulated weather for {city.title()}: {desc}")
    history.append((f"Weather asked for {city}", "weather"))

def simulated_news():
    headline = random.choice(simulated_news)
    print(Fore.CYAN + "TravelBot: Here's a simulated news headline:")
    print(Fore.GREEN + f"- {headline}")
    history.append((headline, "news"))

def local_time_for_city(user_text=""):
    # Try to extract a city name from user_text
    city = None
    for c in city_timezones.keys():
        if c in user_text:
            city = c
            break

    if not city:
        print(Fore.CYAN + "TravelBot: Which city's local time do you want? (e.g., London, New York)")
        city = normalize_input(input(Fore.YELLOW + "You: "))

    city_key = city.lower()
    offset = city_timezones.get(city_key)
    if offset is None:
        print(Fore.RED + "TravelBot: Sorry, I don't know that city's timezone. Try one of:")
        print(Fore.GREEN + ", ".join([c.title() for c in city_timezones.keys()]))
        return

    # Compute approximate local time using UTC now + offset hours
    now_utc = datetime.utcnow()
    # offset can be fractional (e.g., 5.5)
    hours = int(offset)
    minutes = int((abs(offset) - abs(hours)) * 60)
    delta = timedelta(hours=hours, minutes=minutes if offset >= 0 else -minutes)
    local_time = now_utc + delta
    time_str = local_time.strftime("%Y-%m-%d %H:%M")
    print(Fore.GREEN + f"TravelBot: Approx local time in {city.title()} is {time_str} (UTC{offset:+})")
    history.append((f"Checked time for {city}", "time"))

def show_history():
    if not history:
        print(Fore.MAGENTA + "TravelBot: No history yet. Try asking or using a command.")
        return
    print(Fore.CYAN + "\n--- Conversation History ---")
    for idx, (text, label) in enumerate(history, start=1):
        print(f"{idx}. {label} -> {text}")
    print(Fore.CYAN + "--- End of History ---\n")

def repeat_last():
    if not history:
        print(Fore.MAGENTA + "TravelBot: Nothing to repeat yet.")
    else:
        last_text, last_label = history[-1]
        print(Fore.YELLOW + f"TravelBot (repeating last): [{last_label}] {last_text}")

# -----------------------
# NLP preparation notes
# -----------------------
def nlp_notes():
    print(Fore.BLUE + "\n--- NLP Integration Notes (for future) ---")
    print("- Intent detection: Instead of simple keyword checks, an NLP model could detect user intent (e.g., 'book flight' vs 'ask time').")
    print("- Entity recognition: NLP could extract city names, durations, or destination preferences automatically.")
    print("- Sentiment analysis: Understand user feelings to respond empathetically (e.g., 'I'm stressed about packing').")
    print("- Dialogue state: Track multi-step conversations (e.g., when user gives partial info) more robustly.")
    print(Fore.BLUE + "These are points you can explore later when adding real NLP libraries.\n")

# -----------------------
# Main chat loop
# -----------------------
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot — a friendly rule-based chatbot.")
    name = input(Fore.YELLOW + "Your name? ").strip() or "Traveler"
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ").strip()
        if user_input == "":
            print(Fore.MAGENTA + "TravelBot: You typed nothing — try a sentence or a command like 'help'.")
            continue

        text = normalize_input(user_input)

        # Save raw text to history for traceability (label will be updated when action chosen)
        # We append placeholder; some functions also append to history with more info.
        history.append((text, "raw"))

        # Check for commands & intents using regex matchers (order matters)
        if matches_any(RE_EXIT, text):
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye! 👋")
            break
        elif matches_any(RE_HELP, text):
            show_help()
        elif matches_any(RE_HISTORY, text):
            show_history()
        elif matches_any(RE_REPEAT, text):
            repeat_last()
        elif matches_any(RE_RECOMMEND, text):
            recommend(text)
        elif matches_any(RE_PACK, text):
            packing_tips()
        elif matches_any(RE_JOKE, text):
            tell_joke()
        elif matches_any(RE_WEATHER, text):
            simulated_weather(text)
        elif matches_any(RE_NEWS, text):
            simulated_news()
        elif matches_any(RE_TIME, text):
            local_time_for_city(text)
        elif "nlp" in text or "learn nlp" in text:
            nlp_notes()
        else:
            # Try to be a bit friendlier: if user has letters, ask to rephrase; otherwise show help
            if matches_any(RE_JUST_TEXT, text):
                print(Fore.RED + "TravelBot: I didn't understand that. Try asking for 'recommend', 'weather', 'time', or type 'help'.")
            else:
                print(Fore.RED + "TravelBot: Please type visible text or type 'help' for options.")

# -----------------------
# Run the bot
# -----------------------
if __name__ == "__main__":
    chat()
