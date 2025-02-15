import os
import time

def display_main_menu(modules):
    print("\033[1;36mMain Menu:")
    for idx, module_name in enumerate(modules.keys(), 1):
        print(f"\033[1;32m{idx}. {module_name.replace('_', ' ').title()}")
    print(f"\033[1;31m{len(modules) + 1}. Exit\033[0m")


def clear_screen():
    # Function for cleaning the screen depending on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux / macOS
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
    print("\033[1;34m" + logo + "\033[1m")

def display_welcome_message():
    # Function for displaying the welcome message
    print("\033[35mWelcome to Sniffle - the ultimate OSINT tool!")
    print("\033[35mLet's begin the scan and gather some insightful data!")
    print("\033[36m\nPlease wait while the program initializes...\n\033[0m")
    time.sleep(1)  # Delay before starting

def check_config():
    # Function to check if the configuration file exists
    if not os.path.exists("config.py"):
        print("\033[31mSniffle is confused! Before running the script, you need to rename the config_template.py file to config.py and fill in all the data!\033[0m")
        return True
