import os
import time


def display_main_menu(modules):
    print("Main Menu:")
    for idx, module_name in enumerate(modules.keys(), 1):
        print(f"{idx}. {module_name.replace('_', ' ').title()}")
    print(f"{len(modules) + 1}. Exit")


def clear_screen():
    # Function for cleaning the screen depending on the operating system
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux / macOS
        os.system('clear')

def display_logo():
    # Function for displaying the program logo
    logo = '''
.d8888. d8b   db d888888b d88888b d88888b db      d88888b 
88'  YP 888o  88   `88'   88'     88'     88      88'     
`8bo.   88V8o 88    88    88ooo   88ooo   88      88ooooo 
  `Y8b. 88 V8o88    88    88~~~   88~~~   88      88~~~~~ 
db   8D 88  V888   .88.   88      88      88booo. 88.     
`8888Y' VP   V8P Y888888P YP      YP      Y88888P Y88888P 
'''
    print(logo)

def display_welcome_message():
    #Function for displaying the welcome message
    print("Welcome to Sniffle - the ultimate OSINT tool!")
    print("Let's begin the scan and gather some insightful data!")
    print("\nPlease wait while the program initializes...\n")
    time.sleep(1)  # Задержка перед запуском

def check_config():
    if not os.path.exists("config.py"):
        print("Sniffle is confused! Before running the script, you need to rename the config_template.py file to config.py and fill in all the data!")
        return True