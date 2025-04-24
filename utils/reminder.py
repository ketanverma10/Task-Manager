import threading
import time
from datetime import datetime, timedelta
from utils.motivational_quotes import fetch_motivational_quote
from utils.styling import info_message

def start_reminder(task_name, deadline):
    def reminder_loop():
        while True:
            now = datetime.now()
            remaining = deadline - now

            if remaining <= timedelta(seconds=0):
                info_message(f"⏰ Task '{task_name}' time is up!")
                print(fetch_motivational_quote())
                break
            elif timedelta(minutes=4) < remaining <= timedelta(minutes=6):
                info_message(f"⏳ Just 5 minutes left for '{task_name}'!")
                print(fetch_motivational_quote())
            elif timedelta(minutes=29) < remaining <= timedelta(minutes=31):
                info_message(f"⏰ 30 minutes remaining for '{task_name}'!")
                print(fetch_motivational_quote())
            elif remaining.seconds % 3600 < 5:  # Every hour mark (approx)
                info_message(f"🕐 Reminder: You are still working on '{task_name}'...")
                print(fetch_motivational_quote())

            time.sleep(60)  # Check every minute

    # Start the thread
    thread = threading.Thread(target=reminder_loop, daemon=True)
    thread.start()
