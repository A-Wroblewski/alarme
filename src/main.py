import sys

from PySide6.QtGui import QFont, QAction, QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from button import StartCancelButton
from layouts import TopGridLayout, BottomGridLayout
from main_window import MainWindow

from utils.assets_paths import ICON
from utils.pyinstaller import resource_path
from utils.pyside_stuff import make_spacer

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow(app)

    font = QFont('Segoe UI', 16)
    app.setFont(font)

    app.setStyle('Fusion')

    top_grid_layout = TopGridLayout()
    window.main_layout.addLayout(top_grid_layout)

    make_spacer(25, window)

    bottom_grid_layout = BottomGridLayout()
    window.main_layout.addLayout(bottom_grid_layout)

    make_spacer(30, window)

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
