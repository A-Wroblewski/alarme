from notifypy import Notify
from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QPushButton

from assets_path import ICON_PATH, AUDIO_PATH


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

        title = self.bottom_grid_layout.itemAtPosition(1, 1).widget().text()
        description = self.bottom_grid_layout.itemAtPosition(2, 1).widget().text()

        if not title:
            notification.title = 'Cronômetro finalizado'
        else:
            notification.title = title

        notification.message = description
        notification.icon = ICON_PATH
        notification.audio = str(AUDIO_PATH)

        notification.send()
