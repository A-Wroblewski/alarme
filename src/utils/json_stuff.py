import json

json_file = r'src\settings.json'

def save_settings(checkbox_state):
    settings = {'checkbox_state': checkbox_state}

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(settings, file, indent=4)

def load_settings():
    with open(json_file, 'r', encoding='utf-8') as file:
        settings = json.load(file)
        checkbox_state = settings['checkbox_state']

    return checkbox_state
