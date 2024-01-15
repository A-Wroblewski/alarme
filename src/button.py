from notifypy import Notify
from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QPushButton

from utils.assets_paths import ICON, AUDIO
from utils.pyinstaller import resource_path


class StartCancelButton(QPushButton):
    def __init__(self, top_grid_layout, bottom_grid_layout):
        super().__init__()

        self.setText('Iniciar')
        self.is_running = False

        self.top_grid_layout = top_grid_layout
        self.bottom_grid_layout = bottom_grid_layout

        self.clicked.connect(self.toggle_timer)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)

    def toggle_timer(self):
        self.stop_timer() if self.is_running else self.start_timer()

    def start_timer(self):
        self.is_running = True
        self.setText('Cancelar')
        self.update_label()
        self.timer.start(1000)

    def stop_timer(self):
        self.is_running = False
        self.setText('Iniciar')
        self.timer.stop()

        time_remaining_display = self.top_grid_layout.itemAtPosition(1, 1).widget()
        time_remaining_display.setText('00:00:00')

    def update_label(self):
        alarm_time = self.top_grid_layout.itemAtPosition(0, 1).widget().time()
        computer_time = QTime().currentTime()

        seconds_remaining = computer_time.secsTo(alarm_time)
        formatted_time = QTime(0, 0).addSecs(seconds_remaining).toString()

        time_remaining_display = self.top_grid_layout.itemAtPosition(1, 1).widget()
        time_remaining_display.setText(formatted_time)

        if formatted_time == '00:00:00':
            self.stop_timer()
            self.send_notification()

    def send_notification(self):
        notification = Notify()

        app_name = 'Alarme'
        notification.application_name = app_name

        title = self.bottom_grid_layout.itemAtPosition(1, 1).widget().text()
        description = self.bottom_grid_layout.itemAtPosition(2, 1).widget().text()

        title = title.strip()
        description = description.strip()

        if not title:
            notification.title = app_name
        else:
            notification.title = title

        if not description:
            notification.message = 'Cronômetro finalizado'
        else:
            notification.message = description

        icon_path = resource_path(ICON)
        notification.icon = icon_path

        audio_path = resource_path(AUDIO)
        notification.audio = audio_path

        notification.send()
