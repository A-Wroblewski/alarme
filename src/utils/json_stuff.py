import json

from utils.paths import JSON_PATH

def save_settings(checkbox_state):
    settings = {'checkbox_state': checkbox_state}

    with open(JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(settings, file, indent=4)

def load_settings():
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
        settings = json.load(file)
        checkbox_state = settings['checkbox_state']

    return checkbox_state
