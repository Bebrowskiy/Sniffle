import logging

from utils.modules_loader import load_modules
from utils.menu import display_main_menu, check_config
from utils.menu import clear_screen, display_logo, display_welcome_message

# Folder where the modules are stored
MODULES_DIR = 'modules'


def main():
    modules = load_modules(MODULES_DIR)

    clear_screen()
    display_logo()
    display_welcome_message()

    while True:
        if check_config():
            break

        display_main_menu(modules)
        choice = input("\033[1;33mChoose option (1-{}): \033[0m".format(len(modules) + 1))  # Желтый цвет для подсказки

        if choice.isdigit():
            choice = int(choice)
            if choice == len(modules) + 1:
                print("\033[1;32mThe smell of finished work - out for a break!\033[0m")  # Зеленый цвет для завершения
                break
            elif 1 <= choice <= len(modules):
                selected_module = list(modules.values())[choice - 1]
                # Let's call the main module method (must be implemented in every module)
                clear_screen()
                selected_module.main()
                print("\n")
            else:
                print("\033[1;31mNose didn't smell the right choice! Try again!\033[0m")  # Красный цвет для ошибки
        else:
            print("\033[1;31mNose didn't smell the right choice! Try again!\033[0m")  # Красный цвет для ошибки

if __name__ == "__main__":
    main()
