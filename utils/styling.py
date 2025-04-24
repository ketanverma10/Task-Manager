from colorama import Fore, Style, init
init(autoreset=True)

def print_title(text):
    print(Fore.CYAN + Style.BRIGHT + "="*50)
    print(Fore.YELLOW + Style.BRIGHT + f"{text.center(50)}")
    print(Fore.CYAN + Style.BRIGHT + "="*50)

def print_menu():
    print(Fore.GREEN + "\nWhat would you like to do?")
    print(Fore.BLUE + "1. ➕ Add Task")
    print(Fore.BLUE + "2. 📋 View Tasks")
    print(Fore.BLUE + "3. ✏️  Update Task")
    print(Fore.BLUE + "4. ❌ Delete Task")
    print(Fore.RED + "5. 🚪 Exit\n")

def success_message(msg):
    print(Fore.GREEN + f"✅ {msg}")

def error_message(msg):
    print(Fore.RED + f"❌ {msg}")

def info_message(msg):
    print(Fore.YELLOW + f"💡 {msg}")
