import os
import importlib

def load_modules(MODULES_DIR):
    # Loads all modules from the 'modules' folder
    modules = {}
    for filename in os.listdir(MODULES_DIR):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove '.py' from the file name
            module = importlib.import_module(f"modules.{module_name}")
            modules[module_name] = module
    return modules