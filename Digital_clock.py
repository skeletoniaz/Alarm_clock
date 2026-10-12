import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtGui import QIcon
from Alarmclock import set_alarm
import threading

class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.time_label.setObjectName("time_label")
        self.timer = QTimer(self)
        self.alarm_set = QTextEdit(self)
        self.submit_button = QPushButton("Click to Confirm",self)
        self.alarm_label = QLabel("Alarm set for: ",self)
        self.initUI()

    def initUI(self):
        self.setGeometry(1400,200,500,100)
        self.setWindowTitle("YOKOSO WATASHI Digital Clock Society")
        self.setWindowIcon(QIcon("Python/GUI/smug face.png"))
        self.CSS()

    def CSS(self):
        self.time_label.setStyleSheet("font-size : 20px;"
                                      "font-family : Arial;"
                                      )
        self.setStyleSheet("background-color : #42f5a7;")

        self.alarm_label.setGeometry(0,0,100,20)
        self.alarm_label.setStyleSheet("font-size : 15px;")

        self.submit_button.setGeometry(0,0,100,50)
        self.submit_button.setStyleSheet("""
                                        QPushButton:hover{
                                        background-color : #a3c4fa;
                                        }""")

        self.alarm_set.setPlaceholderText("Type the time you want to set your alarm in 24 hour format (HH:MM:SS)")
        self.alarm_set.setGeometry(0,0,300,50)
        self.alarm_set.setStyleSheet("font-size : 15px")

        self.alarm_label.setFixedSize(300,50)
        #self.alarm_label.setAlignment
        self.alarm_label.setGeometry((self.width() - self.alarm_label.width())//2, 70,300,20)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.alarm_set)
        hbox.addWidget(self.submit_button)
        vbox.addWidget(self.alarm_label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # 1000 means 1000 ms
        self.update_time()

        self.submit_button.clicked.connect(self.set_alarm)

    def update_time(self):
        hh = QTime.currentTime().toString("hh")
        current_time = QTime.currentTime().toString("hh:mm:ss AP" + "\n" + f"{hh}:mm:ss") #AP allows for it to say am or pm
        self.time_label.setText(current_time)

    def set_alarm(self):
        alarm_set = self.alarm_set.toPlainText()
        self.alarm_label.setText(f"Alarm has been set for: {alarm_set}")

        #set_alarm(alarm_time=alarm_set)
        alarm_thread = threading.Thread(target=set_alarm, kwargs={'alarm_time': alarm_set}, daemon=True)
        #daemon=True: Ensures the alarm background loop automatically dies when you close your clock window.
        alarm_thread.start()
        self.update_time()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Digital_clock()
    clock.show()
    sys.exit(app.exec_())

#def custom_font()
    #FOR CUSTOM FONTS
    #font_id = QFontDatabase.addApplicationFont("filename.ttf")
    #font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
    #my_font = QFont(font_family,20)
    #self.time_label.setFont(my_font)