import os
import importlib

def load_modules(MODULES_DIR):
    """Загружает все модули из папки 'modules'"""
    modules = {}
    for filename in os.listdir(MODULES_DIR):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Убираем '.py' из имени файла
            module = importlib.import_module(f"modules.{module_name}")
            modules[module_name] = module
    return modules