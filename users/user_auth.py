import json
import os

DATA_FILE = 'data/tasks.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_user():
    user_name = input("Enter your name: ").strip().capitalize()
    data = load_data()

    if user_name not in data:
        print(f"👋 Welcome, {user_name}! Creating your account...")
        data[user_name] = {"tasks": []}
        save_data(data)
    else:
        print(f"👋 Welcome back, {user_name}!")

    return user_name
