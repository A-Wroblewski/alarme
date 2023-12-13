from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from images_path import ICON_PATH

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Alarme')

        self.set_icon()

    def set_icon(self):
        icon = QIcon(str(ICON_PATH))
        self.setWindowIcon(icon)
