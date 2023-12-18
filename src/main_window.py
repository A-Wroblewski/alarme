from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from assets_path import ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        self.setCentralWidget(central_widget)
        self.setWindowTitle('Alarme')

        icon = QIcon(str(ICON_PATH))
        self.setWindowIcon(icon)

    def closeEvent(self, event):
        self.hide()
        event.ignore()
