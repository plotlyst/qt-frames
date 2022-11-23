import sys

from qthandy import vbox
from qtpy.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QTextEdit

from qtframes import Frame


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        frame = Frame()
        frame.setWidget(QLabel('Test label inside the frame'))
        frame.setWidget(QTextEdit())
        vbox(self.widget, 5)
        self.widget.layout().addWidget(frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    app.exec()
