from users.user_auth import get_user
from tasks.task_crud import task_menu
from utils.styling import print_title, info_message
from utils.motivational_quotes import get_quote

def main():
    print_title("Welcome to Your Personal Task Manager")
    get_quote()  # Show motivational quote at start
    print()
    try:
        user = get_user()
    except Exception as e:
        print(e)

    task_menu(user)

if __name__ == "__main__":
    main()
