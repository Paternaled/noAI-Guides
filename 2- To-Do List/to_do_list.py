import json
import os

def load_menu():
    if not os.path.exists("menu.json"):
        return {}
    
    with open("menu.json", "r") as file:
        return json.load(file)

def save_menu(menu):
    with open("menu.json", "w") as file:
        json.dump(menu, file, indent=4)
