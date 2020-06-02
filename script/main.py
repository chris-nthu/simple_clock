import sys
import os.path
from stopwatch import Stopwatch
from countdown import Countdown
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    stopwatch_lap_count = 0
    stopwatch_current_time = 0
    stopwatch_lap = ''

    # Load UI file
    w = loadUi(os.path.dirname(__file__) + '/../ui/clock.ui')

    try:
        # Read operation history of stopwatch
        stopwatch_history = open(os.path.dirname(__file__) + '/../save/stopwatch_save.bin', 'rb')
        stopwatch_lines = stopwatch_history.readlines()

        stopwatch_lap_count = int(stopwatch_lines[0].decode().strip('\n'))
        stopwatch_current_time = int(stopwatch_lines[1].decode().strip('\n'))

        for i in range(2,len(stopwatch_lines)):
            stopwatch_lap += stopwatch_lines[i].decode()

        # Initial the class of Stopwatch and Countdown
        s = Stopwatch(w, stopwatch_lap_count, stopwatch_current_time, stopwatch_lap)
        c = Countdown(w)

    except:
        # Initial the class of Stopwatch and Countdown
        s = Stopwatch(w)
        c = Countdown(w)

    # Declare timer for stopwatch and countdown
    w.stopwatch_timer = QTimer()
    w.countdown_timer = QTimer()

    # Load beep voice
    # w.beep_sound = QSound('beep.wav', w)

    # Connect to slot function of stopwatch
    w.stopwatch_lap_btn.clicked.connect(s.lap_btn)
    w.stopwatch_reset_btn.clicked.connect(s.reset_btn)
    w.stopwatch_start_stop_btn.clicked.connect(s.start_stop_btn)
    w.stopwatch_timer.timeout.connect(s.display)

    # Connect to slot function of countdown
    w.countdown_reset_btn.clicked.connect(c.reset_btn)
    w.countdown_start_btn.clicked.connect(c.start_btn)
    w.countdown_pause_btn.clicked.connect(c.pause_btn)
    w.countdown_close_btn.clicked.connect(c.close_btn)
    w.countdown_hours_spinBox.valueChanged.connect(c.setCountdownTime)
    w.countdown_mins_spinBox.valueChanged.connect(c.setCountdownTime)
    w.countdown_secs_spinBox.valueChanged.connect(c.setCountdownTime)
    w.countdown_timer.timeout.connect(c.display)

    w.show()
    app.exec_()
