import sys
import app_style

from PySide6.QtWidgets import QApplication

from button import StartCancelButton
from layouts import TopGridLayout, BottomGridLayout
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()

    app_style.set_style()

    top_grid_layout = TopGridLayout()
    window.main_layout.addLayout(top_grid_layout)

    bottom_grid_layout = BottomGridLayout()
    window.main_layout.addLayout(bottom_grid_layout)

    button = StartCancelButton()
    window.main_layout.addWidget(button)

    window.show()
    sys.exit(app.exec())
