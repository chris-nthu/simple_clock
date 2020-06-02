
class Countdown():

    def __init__(self, widget):
        self.w = widget
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self._flag = 0
        self.w.countdown_close_btn.setVisible(False)
    

    def reset_btn(self):
        self.w.countdown_start_btn.setEnabled(True)
        self.w.countdown_pause_btn.setEnabled(False)

        self.w.countdown_hours_spinBox.setEnabled(True)
        self.w.countdown_mins_spinBox.setEnabled(True)
        self.w.countdown_secs_spinBox.setEnabled(True)

        self.w.countdown_hours_spinBox.setValue(0)
        self.w.countdown_mins_spinBox.setValue(0)
        self.w.countdown_secs_spinBox.setValue(0)
    

    def start_btn(self):
        self.w.countdown_pause_btn.setEnabled(True)
        self.w.countdown_start_btn.setEnabled(False)

        self.w.countdown_hours_spinBox.setEnabled(False)
        self.w.countdown_mins_spinBox.setEnabled(False)
        self.w.countdown_secs_spinBox.setEnabled(False)

        self.w.countdown_timer.start(10)

    
    def pause_btn(self):
        self.w.countdown_start_btn.setEnabled(True)
        self.w.countdown_pause_btn.setEnabled(False)

        self.w.countdown_hours_spinBox.setEnabled(True)
        self.w.countdown_mins_spinBox.setEnabled(True)
        self.w.countdown_secs_spinBox.setEnabled(True)

        self.w.countdown_timer.stop()
    

    def close_btn(self):
        self.w.countdown_reset_btn.setEnabled(True)
        self.w.countdown_start_btn.setEnabled(True)
        self.w.countdown_pause_btn.setEnabled(False)
        self.w.countdown_close_btn.setVisible(False)

        self.w.countdown_hours_spinBox.setEnabled(True)
        self.w.countdown_mins_spinBox.setEnabled(True)
        self.w.countdown_secs_spinBox.setEnabled(True)

        self.setCountdownTime()


    def setCountdownTime(self):
        self.hours = self.w.countdown_hours_spinBox.value()
        self.mins = self.w.countdown_mins_spinBox.value()
        self.secs = self.w.countdown_secs_spinBox.value()
        fmt = '{:0>2d}:{:0>2d}:{:0>2d}'
        self.w.countdown_label.setText(fmt.format(self.hours, self.mins, self.secs))


    def convert(self):
        fmt = '{:0>2d}:{:0>2d}:{:0>2d}'
        return fmt.format(self.hours, self.mins, self.secs)


    def run_out_of_time(self):
        self.w.countdown_timer.stop()
        self.w.countdown_pause_btn.setEnabled(False)
        self.w.countdown_reset_btn.setEnabled(False)
        self.w.countdown_close_btn.setVisible(True)


    def display(self):
        self._flag += 10

        if self._flag == 1000:
            self._flag = 0
            if self.secs != 0:
                self.secs -= 1
            else:
                if self.mins != 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    if self.hours != 0:
                        self.hours -= 1
                        self.mins = 59
                        self.secs = 59
                    else:
                        self.run_out_of_time()


        self.w.countdown_label.setText(self.convert())
