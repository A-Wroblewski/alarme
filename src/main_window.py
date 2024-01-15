from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from settings import SettingsWindow

from utils.paths import ICON
from utils.pyinstaller import resource_path


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.main_layout = QVBoxLayout()

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Alarme')

        icon_path = resource_path(ICON)
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)

        self.set_menu_bar()

    def set_menu_bar(self):
        menu = self.menuBar()

        options_menu = menu.addMenu('Opções')

        settings_option = QAction('Configurações', self)
        settings_option.triggered.connect(self.open_settings_window)
        options_menu.addAction(settings_option)

        quit_option = QAction('Encerrar', self)
        quit_option.triggered.connect(self.app.quit)
        options_menu.addAction(quit_option)

    def open_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.exec()

    def closeEvent(self, event):
        self.hide()
        event.ignore()
