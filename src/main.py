import os
import sys
import winreg as wr

from PySide6.QtGui import QFont, QAction, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu

from button import StartCancelButton
from layouts import TopGridLayout, BottomGridLayout
from main_window import MainWindow

from utils.assets_paths import ICON
from utils.pyinstaller import resource_path

def set_run_on_startup():
    key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    app_name = 'Alarme'
    script_path = os.path.abspath(sys.argv[0])

    try:
        with wr.OpenKey(wr.HKEY_CURRENT_USER, key, 0, wr.KEY_SET_VALUE) as registry_key:
            wr.SetValueEx(registry_key, app_name, 0, wr.REG_SZ, script_path)
    except:
        pass

def make_spacer(height):
    spacer = QWidget()
    spacer.setFixedHeight(height)
    window.main_layout.addWidget(spacer)

if __name__ == '__main__':
    set_run_on_startup()

    app = QApplication([])
    window = MainWindow()

    font = QFont('Segoe UI', 16)
    app.setFont(font)

    app.setStyle('Fusion')

    top_grid_layout = TopGridLayout()
    window.main_layout.addLayout(top_grid_layout)

    make_spacer(25)

    bottom_grid_layout = BottomGridLayout()
    window.main_layout.addLayout(bottom_grid_layout)

    make_spacer(30)

    button = StartCancelButton(top_grid_layout, bottom_grid_layout)
    window.main_layout.addWidget(button)

    # ----------------------------------------------------------------------- #
    #                                tray icon                                #
    # ----------------------------------------------------------------------- #

    icon_path = resource_path(ICON)
    icon = QIcon(icon_path)

    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(icon)

    menu = QMenu()
    show_action = QAction('Abrir', triggered=window.show)
    quit_action = QAction('Encerrar', triggered=app.quit)

    menu.addAction(show_action)
    menu.addAction(quit_action)

    tray_icon.setContextMenu(menu)
    tray_icon.show()

    # ----------------------------------------------------------------------- #

    window.show()
    sys.exit(app.exec())
