import random

# Small data sets
GOOD = ["good", "great", "happy", "well", "fine", "awesome"]
BAD = ["bad", "sad", "unhappy", "terrible", "awful"]
JOKES = [
    "Why did the computer go to the doctor? It had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
]
ADVICE = [
    "Take a deep breath — small steps are okay!",
    "Try doing one fun thing for 10 minutes — it helps.",
]

# Greet the user
print("Hello! I am AI Bot. What's your name? : ")
name = input().strip()
if not name:
    name = "Friend"
print(f"Nice to meet you, {name}!")

last_bot = ""  # store last bot message for 'repeat'

# Ask how they are feeling
print("How are you feeling today? (you can type words like 'good' or 'sad') : ")
mood = input().strip().lower()

# Simple emotion-based response
if any(w in mood for w in GOOD):
    last_bot = "I'm glad to hear that! 😊 What made your day good?"
    print(last_bot)
elif any(w in mood for w in BAD):
    last_bot = "I'm sorry you're feeling down. Want a joke or some advice?"
    print(last_bot)
else:
    last_bot = "I see. Thanks for sharing — would you like to talk about a topic?"
    print(last_bot)

# Main simple loop
while True:
    print("\nChoose one: joke / hobby / advice / repeat / bye")
    choice = input("Your choice: ").strip().lower()

    if choice == "joke":
        last_bot = random.choice(JOKES)
        print(last_bot)

    elif choice == "hobby":
        print("Cool — what's a hobby you like?")
        hobby = input("My hobby is: ").strip()
        if hobby:
            last_bot = f"Nice! {hobby.capitalize()} sounds fun. How long have you done it?"
            print(last_bot)
            # short follow-up to keep it simple
            _ = input("(type how long, or press enter) ")
        else:
            last_bot = "No problem — hobbies can be many small things!"
            print(last_bot)

    elif choice == "advice":
        last_bot = random.choice(ADVICE)
        print(last_bot)

    elif choice == "repeat":
        if last_bot:
            print("Repeating:", last_bot)
        else:
            print("I haven't said anything yet to repeat.")

    elif choice in ("bye", "exit", "quit"):
        print(f"It was nice chatting with you, {name}. Goodbye!")
        break

    else:
        print("I didn't understand that. Try one of the options, or type 'bye' to end.")

# End of script
