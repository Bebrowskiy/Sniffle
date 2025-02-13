import os
import time


def display_main_menu(modules):
    print("Main Menu:")
    for idx, module_name in enumerate(modules.keys(), 1):
        print(f"{idx}. {module_name.replace('_', ' ').title()}")
    print(f"{len(modules) + 1}. Exit")


def clear_screen():
    """Функция для очистки экрана в зависимости от операционной системы"""
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux / macOS
        os.system('clear')

def display_logo():
    """Функция для отображения логотипа программы"""
    logo = '''
.oooooo..o              o8o   .o88o.  .o88o.                    
d8P'    `Y8              `"'   888 `"  888 `"                    
Y88bo.      ooo. .oo.   oooo  o888oo  o888oo   .ooooo.  oooo d8b 
 `"Y8888o.  `888P"Y88b  `888   888     888    d88' `88b `888""8P 
     `"Y88b  888   888   888   888     888    888ooo888  888     
oo     .d8P  888   888   888   888     888    888    .o  888     
8""88888P'  o888o o888o o888o o888o   o888o   `Y8bod8P' d888b    
'''
    print(logo)

def display_welcome_message():
    """Функция для отображения приветственного сообщения"""
    print("Welcome to Sniffle - the ultimate OSINT tool!")
    print("Let's begin the scan and gather some insightful data!")
    print("\nPlease wait while the program initializes...\n")
    time.sleep(1)  # Задержка перед запуском