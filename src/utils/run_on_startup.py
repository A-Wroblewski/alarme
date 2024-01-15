import os
import sys
import shutil
import getpass

def get_startup_path():
    USER_NAME = getpass.getuser()
    startup_path = rf'C:\Users\{USER_NAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

    return startup_path

def add_shortcut():
    startup_path = get_startup_path()

    python_executable = sys.executable
    shortcut_path = os.path.join(startup_path, 'Alarme.lnk')

    try:
        shutil.copy(python_executable, shortcut_path)
    except:
        pass

def remove_shortcut():
    startup_path = get_startup_path()

    shortcut_path = os.path.join(startup_path, 'Alarme.lnk')

    try:
        os.remove(shortcut_path)
    except:
        pass
