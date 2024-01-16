import os
import json

from utils.paths import JSON_PATH
from utils.run_on_startup import get_startup_path

def save_settings(checkbox_state):
    settings = {'checkbox_state': checkbox_state}

    with open(JSON_PATH, 'w', encoding='utf-8') as file:
        json.dump(settings, file, indent=4)

def load_settings():
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
        settings = json.load(file)
        checkbox_state = settings['checkbox_state']

    return checkbox_state

def set_json_on_run():
    startup_path = get_startup_path()
    startup_path += r'\Alarme.lnk'

    shortcut_is_set = os.path.exists(startup_path)

    save_settings(shortcut_is_set)
