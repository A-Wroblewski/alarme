from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QMessageBox

from utils.assets_paths import ICON
from utils.pyinstaller import resource_path

def make_spacer(height, window):
    spacer = QWidget()
    spacer.setFixedHeight(height)

    window.main_layout.addWidget(spacer)

def decide_unsaved_settings(json_checkbox_state, user_checkbox_state):
    confirmation_message = QMessageBox()

    icon_path = resource_path(ICON)
    icon = QIcon(icon_path)
    confirmation_message.setWindowIcon(icon)

    icon = confirmation_message.Icon.Question
    confirmation_message.setIcon(icon)

    confirmation_message.setWindowTitle('Confirmar alterações')
    confirmation_message.setText('Há alterações não salvas. Deseja salvar?')

    confirmation_message.setStandardButtons(
        QMessageBox.Save | QMessageBox.Discard
    )

    confirmation_message.setButtonText(QMessageBox.Save, 'Sim')
    confirmation_message.setButtonText(QMessageBox.Discard, 'Não')

    choice = confirmation_message.exec()

    if choice == QMessageBox.Save:
        return user_checkbox_state
    elif choice == QMessageBox.Discard:
        return json_checkbox_state
