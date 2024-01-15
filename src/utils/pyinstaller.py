import os
import sys

from utils.paths import ASSETS_PATH

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(ASSETS_PATH)

    return os.path.join(base_path, relative_path)
