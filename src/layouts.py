from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QLineEdit, QTimeEdit, QGridLayout


class TopGridLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        self.add_widgets()

    def create_alarm_label(self):
        alarm_label = QLabel()
        alarm_label.setText('Alarme para as:')

        return alarm_label

    def create_alarm_input(self):
        alarm_input = QTimeEdit()

        return alarm_input

    def create_time_remaining_label(self):
        time_remaining_label = QLabel()
        time_remaining_label.setText('Tempo restante:')

        return time_remaining_label

    def create_time_remaining_display(self):
        time_remaining_display = QLineEdit()
        time_remaining_display.setReadOnly(True)
        time_remaining_display.setText('00:00:00')

        return time_remaining_display

    def create_widgets(self):
        alarm_label = self.create_alarm_label()
        alarm_input = self.create_alarm_input()
        time_remaining_label = self.create_time_remaining_label()
        time_remaining_display = self.create_time_remaining_display()

        return alarm_label, alarm_input, time_remaining_label, time_remaining_display

    def add_widgets(self):
        alarm_label, alarm_input, time_remaining_label, time_remaining_display = self.create_widgets()

        self.addWidget(alarm_label, 0, 0)
        self.addWidget(alarm_input, 0, 1)
        self.addWidget(time_remaining_label, 1, 0)
        self.addWidget(time_remaining_display, 1, 1)


class BottomGridLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        self.add_widgets()

    def create_notification_label(self):
        notification_label = QLabel()
        notification_label.setText('Ajustes da notificação (opcionais)')
        notification_label.setAlignment(Qt.AlignmentFlag.AlignBottom)

        return notification_label

    def create_title_label(self):
        title_label = QLabel()
        title_label.setText('Título:')

        return title_label

    def create_title_input(self):
        title_input = QLineEdit()

        return title_input

    def create_description_label(self):
        description_label = QLabel()
        description_label.setText('Descrição:')

        return description_label

    def create_description_input(self):
        description_input = QLineEdit()

        return description_input

    def create_widgets(self):
        notification_label = self.create_notification_label()
        title_label = self.create_title_label()
        title_input = self.create_title_input()
        description_label = self.create_description_label()
        description_input = self.create_description_input()

        return notification_label, title_label, title_input, description_label, description_input

    def add_widgets(self):
        notification_label, title_label, title_input, description_label, description_input = self.create_widgets()

        self.addWidget(notification_label, 0, 0, 1, 2)
        self.addWidget(title_label, 1, 0)
        self.addWidget(title_input, 1, 1)
        self.addWidget(description_label, 2, 0)
        self.addWidget(description_input, 2, 1)
