from qtframes import Frame


def test_frames(qtbot):
    frame = Frame()
    qtbot.addWidget(frame)
    frame.show()
    qtbot.wait(100)
