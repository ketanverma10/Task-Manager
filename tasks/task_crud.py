import threading
import time
from datetime import datetime, timedelta
from utils.file_manager import load_data, save_data
from utils.styling import success_message, error_message, info_message
from utils.motivational_quotes import get_quote

def start_reminder(user, task):
    def reminder():
        task_deadline = datetime.strptime(task['deadline'], "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        time_diff = task_deadline - now

        while True:
            now = datetime.now()
            diff = task_deadline - now
            minutes_left = diff.total_seconds() / 60

            if minutes_left <= 0:
                print(f"\n⏰ Time's up for task '{task['name']}'!")
                break
            elif 0 < minutes_left <= 5:
                print(f"\n⚠️ Only 5 minutes left for '{task['name']}'!")
            elif 5 < minutes_left <= 30:
                print(f"\n⚠️ Only 30 minutes left for '{task['name']}'!")
            elif 30 < minutes_left and int(minutes_left) % 60 == 0:
                print(f"\n⏰ Reminder: Still working on '{task['name']}'")

            time.sleep(60)  # check every minute

    thread = threading.Thread(target=reminder)
    thread.daemon = True
    thread.start()

def add_task(user):
    data = load_data()

    name = input("Enter task name: ").strip()
    desc = input("Enter description: ").strip()
    hours = int(input("Estimated hours: "))
    minutes = int(input("Estimated minutes: "))

    deadline = datetime.now() + timedelta(hours=hours, minutes=minutes)
    deadline_str = deadline.strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "name": name,
        "description": desc,
        "deadline": deadline_str,
        "status": "Not Done"
    }

    data[user]["tasks"].append(task)
    save_data(data)

    success_message(f"Task '{name}' added successfully!")
    info_message(get_quote())  # Quote after task added
    start_reminder(user, task)

def view_tasks(user):
    data = load_data()
    tasks = data.get(user, {}).get("tasks", [])

    if not tasks:
        error_message("No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"\n{i}. {task['name']} - {task['status']}")
        print(f"   Description: {task['description']}")
        print(f"   Deadline: {task['deadline']}")

def update_task(user):
    data = load_data()
    tasks = data[user]["tasks"]

    view_tasks(user)
    name = input("Enter task name to update: ").strip()

    for task in tasks:
        if task["name"].lower() == name.lower():
            new_status = input("Enter new status (Done/Not Done): ").strip()
            task["status"] = new_status
            save_data(data)
            success_message(f"Task '{name}' updated.")
            return
    error_message("Task not found.")

def delete_task(user):
    data = load_data()
    tasks = data[user]["tasks"]

    view_tasks(user)
    name = input("Enter task name to delete: ").strip()

    for task in tasks:
        if task["name"].lower() == name.lower():
            tasks.remove(task)
            save_data(data)
            success_message(f"Task '{name}' deleted.")
            return
    error_message("Task not found.")

def task_menu(user):
    while True:
        print("\n📋 Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(user)
        elif choice == "2":
            view_tasks(user)
        elif choice == "3":
            update_task(user)
        elif choice == "4":
            delete_task(user)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            error_message("Invalid choice. Try again.")
