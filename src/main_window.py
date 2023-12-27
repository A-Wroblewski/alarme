from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from utils.assets_paths import ICON
from utils.pyinstaller import resource_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Alarme')

        icon_path = resource_path(ICON)
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)

    def closeEvent(self, event):
        self.hide()
        event.ignore()
