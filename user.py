from colorama import Fore,Style

def get_user():
    print(Fore.CYAN + "👤 Welcome to the Personal Task Manager!" + Style.RESET_ALL)
    name=input("Please entter you name:").strip().capitalize()

    if not name:
        print(Fore.RED+"⚠️ Name cannot be empty!" +Style.RESET_ALL)
        return get_user()
    print(Fore.GREEN + f"\n🎉 Hello, {name}! Let's manage your tasks!\n" + Style.RESET_ALL)
    return name