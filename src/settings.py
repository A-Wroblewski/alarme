from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QDialog, QCheckBox

from utils.assets_paths import ICON
from utils.json_stuff import save_settings, load_settings
from utils.pyinstaller import resource_path
from utils.pyside_stuff import make_spacer, decide_unsaved_settings
from utils.run_on_startup import add_shortcut, remove_shortcut


class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.checkbox_state = load_settings()

        self.setWindowTitle('Configurações')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        icon_path = resource_path(ICON)
        icon = QIcon(icon_path)
        self.setWindowIcon(icon)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.checkbox = self.create_checkbox()
        self.main_layout.addWidget(self.checkbox)

        make_spacer(20, self)

        apply_button, cancel_button = self.create_buttons()
        buttons_layout = self.set_buttons_layout(apply_button, cancel_button)

        self.main_layout.addLayout(buttons_layout)

    def create_checkbox(self):
        checkbox = QCheckBox('Iniciar ao ligar o computador')
        checkbox.setChecked(self.checkbox_state)

        return checkbox

    def create_buttons(self):
        apply_button = QPushButton('Aplicar')
        cancel_button = QPushButton('Cancelar')

        apply_button.clicked.connect(self.apply_changes)
        cancel_button.clicked.connect(self.cancel_changes)

        return apply_button, cancel_button

    def set_buttons_layout(self, apply_button, cancel_button):
        buttons_layout = QHBoxLayout()

        buttons_layout.addWidget(apply_button)
        buttons_layout.addWidget(cancel_button)

        return buttons_layout

    def apply_changes(self, choice=None, _=''):
        if choice is not None:
            save_settings(choice)

            if choice:
                add_shortcut()
            else:
                remove_shortcut()
        else:
            checkbox_state = self.checkbox.isChecked()
            save_settings(checkbox_state)

            if checkbox_state:
                add_shortcut()
            else:
                remove_shortcut()

        self.close()

    def cancel_changes(self):
        json_checkbox_state = self.checkbox_state
        user_checkbox_state = self.checkbox.isChecked()

        if json_checkbox_state != user_checkbox_state:
            choice = decide_unsaved_settings(json_checkbox_state, user_checkbox_state)
            self.apply_changes(choice)

        self.close()
