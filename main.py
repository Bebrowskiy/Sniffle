import logging

from utils.modules_loader import load_modules
from utils.menu import display_main_menu
from utils.menu import clear_screen, display_logo, display_welcome_message

# Папка, где хранятся модули
MODULES_DIR = 'modules'


def main():
    modules = load_modules(MODULES_DIR)

    clear_screen()
    display_logo()
    display_welcome_message()

    while True:
        display_main_menu(modules)
        choice = input("Choose option (1-{}): ".format(len(modules) + 1))

        if choice.isdigit():
            choice = int(choice)
            if choice == len(modules) + 1:
                print("The smell of finished work - out for a break!")
                break
            elif 1 <= choice <= len(modules):
                selected_module = list(modules.values())[choice - 1]
                # Вызовем основной метод модуля (должен быть реализован в каждом модуле)
                print("\n\n\n")
                selected_module.main()
                print("\n\n\n")
            else:
                print("Nose didn't smell the right choice! Try again!")
        else:
            print("Nose didn't smell the right choice! Try again!")

if __name__ == "__main__":
    main()
