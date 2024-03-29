import sys

import qtawesome
from qthandy import vbox, transparent
from qtpy.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QTextEdit, QToolButton

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

        frame = Frame()
        frame.setNestedFrameEnabled(False)
        frame.setOuterFrameWidth(3)
        btn = QToolButton()
        transparent(btn)
        btn.setIcon(qtawesome.icon('ei.adult'))
        frame.setWidget(btn)
        self.widget.layout().addWidget(frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    app.exec()
