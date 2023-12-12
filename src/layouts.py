from PySide6.QtWidgets import QLabel, QLineEdit, QTimeEdit, QGridLayout, QFrame


class TopGridLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        self.add_widgets()

    def create_widgets(self):
        alarm_label = QLabel()
        alarm_label.setText('Alarme para as:')

        alarm_input = QTimeEdit()

        time_remaining_label = QLabel()
        time_remaining_label.setText('Tempo restante:')

        time_remaining_display = QLineEdit()
        time_remaining_display.setReadOnly(True)
        time_remaining_display.setText('00:00:00')

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

    def create_widgets(self):
        notification_label = QLabel()
        notification_label.setText('Ajustes da notificação (opcionais)')

        title_label = QLabel()
        title_label.setText('Título:')

        title_input = QLineEdit()

        description_label = QLabel()
        description_label.setText('Descrição:')

        description_input = QLineEdit()

        return notification_label, title_label, title_input, description_label, description_input

    def add_widgets(self):
        notification_label, title_label, title_input, description_label, description_input = self.create_widgets()

        # frame = QFrame()
        # frame.setStyleSheet('background-color: grey;')
        # self.addWidget(frame)

        self.addWidget(notification_label, 0, 0, 1, 2)
        self.addWidget(title_label, 1, 0)
        self.addWidget(title_input, 1, 1)
        self.addWidget(description_label, 2, 0)
        self.addWidget(description_input, 2, 1)
