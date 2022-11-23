from qthandy import vbox, clear_layout, margins
from qtpy.QtCore import Qt, QRect
from qtpy.QtGui import QPainter, QPen, QBrush, QPainterPath, QPaintEvent, QResizeEvent
from qtpy.QtWidgets import QWidget


class Frame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._frameBorderWidth: int = 5
        self._nestedFrameBorderWidth: int = 2
        self._heightPercent: float = 0.8

        vbox(self, self._frameBorderWidth, 0)

    def setWidget(self, widget):
        clear_layout(self)
        self.layout().addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self._calculateMargins()

    def resizeEvent(self, event: QResizeEvent) -> None:
        super(Frame, self).resizeEvent(event)
        self._calculateMargins()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.RenderHint.LosslessImageRendering)
        pen = QPen()
        pen.setWidth(self._frameBorderWidth)
        pen.setColor(Qt.GlobalColor.darkBlue)
        painter.setPen(pen)
        painter.setBrush(Qt.GlobalColor.white)

        rect = event.rect()
        rect.setX(self._frameBorderWidth)
        rect.setY(self._frameBorderWidth)
        rect.setWidth(rect.width() - self._frameBorderWidth)
        rect.setHeight(rect.height() - self._frameBorderWidth)
        self._drawFrame(painter, rect)

        painter.setBrush(QBrush())
        pen = QPen()
        pen.setWidth(self._nestedFrameBorderWidth)
        pen.setColor(Qt.GlobalColor.white)
        painter.setPen(pen)
        nested_rect = event.rect()
        nested_rect.setX(self._frameBorderWidth)
        nested_rect.setY(self._frameBorderWidth)
        nested_rect.setWidth(nested_rect.width() - self._frameBorderWidth)
        nested_rect.setHeight(nested_rect.height() - self._frameBorderWidth)
        self._drawFrame(painter, nested_rect)

    def _drawFrame(self, painter: QPainter, rect: QRect):
        path = QPainterPath()
        path.moveTo(self._frameBorderWidth, self._frameBorderWidth)
        path.lineTo(rect.topRight())

        height = rect.height() * 0.8
        path.lineTo(rect.bottomRight().x(), height)
        path.lineTo(rect.center().x(), rect.bottom() - 5)
        path.lineTo(rect.bottomLeft().x(), height)
        path.lineTo(rect.topLeft())

        painter.drawPath(path)

    def _calculateMargins(self):
        if self.height():
            bottom_margin = self.height() * (1 - self._heightPercent) + self._frameBorderWidth * 2
        else:
            bottom_margin = self._frameBorderWidth

        margins(self, self._frameBorderWidth * 2, self._frameBorderWidth * 2, self._frameBorderWidth * 2,
                bottom=bottom_margin)
