from users.user_auth import get_username
from utils.styling import title

def main():
    user=get_username()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Add Task feature coming soon!")
        elif choice == '2':
            print("View Task feature coming soon!")
        elif choice == '3':
            print("Delete Task feature coming soon!")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
            