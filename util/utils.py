# utils.py
from datetime import datetime

def greet_user(name):
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    print(f"{greeting}, {name}! Welcome to your first GitHub project 🎉")

