import sys

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QWidget

from button import StartCancelButton
from layouts import TopGridLayout, BottomGridLayout
from main_window import MainWindow

def make_spacer(height):
    spacer = QWidget()
    spacer.setFixedHeight(height)
    window.main_layout.addWidget(spacer)

if __name__ == '__main__':
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

    window.show()
    sys.exit(app.exec())
