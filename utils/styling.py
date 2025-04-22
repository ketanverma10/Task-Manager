# utils/styling.py

from colorama import init, Fore, Style

init(autoreset=True)

def title(msg):
    print(Fore.CYAN + Style.BRIGHT + f"\n=== {msg} ===")

def success(msg):
    print(Fore.GREEN + Style.BRIGHT + msg)
