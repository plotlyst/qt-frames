import sys

from qthandy import vbox
from qtpy.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QTextEdit

from qtframes import Frame, RoundedFrame


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        vbox(self.widget, 5)
        
        frame = Frame()
        frame.setWidget(QTextEdit())
        self.widget.layout().addWidget(frame)

        roundedFrame = RoundedFrame()
        roundedFrame.setWidget(QLabel('Test label inside the frame'))
        self.widget.layout().addWidget(roundedFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    app.exec()
