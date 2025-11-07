import random

def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The secret of getting ahead is getting started. – Mark Twain",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Success is not for the lazy. – Unknown",
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("\n✨ Your Motivational Quote for Today ✨")
    print(get_random_quote())

