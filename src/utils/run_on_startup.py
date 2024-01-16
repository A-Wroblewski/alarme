import os
import sys
import getpass
import win32com.client

def get_startup_path():
    USER_NAME = getpass.getuser()
    startup_path = rf'C:\Users\{USER_NAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

    return startup_path

def add_shortcut():
    startup_path = get_startup_path()

    python_executable = sys.executable
    shortcut_path = os.path.join(startup_path, 'Alarme.lnk')

    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = python_executable
    shortcut.WorkingDirectory = os.path.dirname(python_executable)
    shortcut.save()

def remove_shortcut():
    startup_path = get_startup_path()
    shortcut_path = os.path.join(startup_path, 'Alarme.lnk')

    try:
        os.remove(shortcut_path)
    except FileNotFoundError:
        pass
