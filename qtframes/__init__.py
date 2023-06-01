from qthandy import vbox, clear_layout, margins
from qtpy.QtCore import Qt, QRect
from qtpy.QtGui import QPainter, QPen, QBrush, QPainterPath, QPaintEvent, QResizeEvent
from qtpy.QtWidgets import QWidget, QSizePolicy


class _AbstractFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._frameBorderWidth: int = 5
        self._nestedFrameBorderWidth: int = 2
        self._nestedFrameEnabled: bool = False
        self._padding: int = 2
        self._frameColor = Qt.GlobalColor.darkBlue
        self._brushColor = Qt.GlobalColor.transparent

        vbox(self, self._frameBorderWidth, 0)
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)

    def frameColor(self):
        return self._frameColor

    def setFrameColor(self, color):
        self._frameColor = color
        self.update()

    def backgroundColor(self):
        return self._brushColor

    def setBackgroundColor(self, color):
        self._brushColor = color
        self.update()

    def setOuterFrameWidth(self, width: int):
        self._frameBorderWidth = width
        self._calculateMargins()
        self.update()

    def outerFrameWidth(self) -> int:
        return self._frameBorderWidth

    def setPadding(self, padding: int):
        self._padding = padding
        self._calculateMargins()
        self.update()

    def padding(self) -> int:
        return self._padding

    def setNestedFrameEnabled(self, enabled: bool):
        self._nestedFrameEnabled = enabled
        self.update()

    def nestedFrameEnabled(self) -> bool:
        return self._nestedFrameEnabled

    def widget(self):
        if self.layout().count():
            return self.layout().itemAt(0).widget()

    def setWidget(self, widget):
        clear_layout(self)
        self.layout().addWidget(widget)
        self._calculateMargins()

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self._calculateMargins()

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.RenderHint.LosslessImageRendering)

        pen = QPen()
        pen.setWidth(self._frameBorderWidth)
        pen.setColor(self._frameColor)
        painter.setPen(pen)
        painter.setBrush(self._brushColor)

        rect = self.rect()
        rect.setX(self._frameBorderWidth)
        rect.setY(self._frameBorderWidth)
        rect.setWidth(rect.width() - self._frameBorderWidth)
        rect.setHeight(rect.height() - self._frameBorderWidth)
        self._drawFrame(painter, rect)

        if self._nestedFrameEnabled:
            painter.setBrush(QBrush())
            pen = QPen()
            pen.setWidth(self._nestedFrameBorderWidth)
            pen.setColor(Qt.GlobalColor.white)
            painter.setPen(pen)

            nested_rect = self.rect()
            nested_rect.setX(self._frameBorderWidth)
            nested_rect.setY(self._frameBorderWidth)
            nested_rect.setWidth(nested_rect.width() - self._frameBorderWidth)
            nested_rect.setHeight(nested_rect.height() - self._frameBorderWidth)
            self._drawFrame(painter, nested_rect)

        painter.end()

    def _calculateMargins(self):
        pass

    def _drawFrame(self, painter: QPainter, rect: QRect):
        pass


class Frame(_AbstractFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._heightPercent: float = 0.8

    def _drawFrame(self, painter: QPainter, rect: QRect):
        path = QPainterPath()
        path.moveTo(self._frameBorderWidth, self._frameBorderWidth)
        path.lineTo(rect.topRight().x(), rect.topRight().y())

        height = rect.height() * self._heightPercent
        path.lineTo(rect.bottomRight().x(), height)
        path.lineTo(rect.center().x(), rect.bottom() - self._frameBorderWidth)
        path.lineTo(rect.bottomLeft().x(), height)
        path.lineTo(rect.topLeft().x(), rect.topLeft().y())

        painter.drawPath(path)

    def _calculateMargins(self):
        if self.height():
            bottom_margin = int(self.height() * (1 - self._heightPercent) + self._frameBorderWidth * 2)
        else:
            bottom_margin = self._frameBorderWidth

        m = self._frameBorderWidth + self._padding
        margins(self, m, m, m,
                bottom=bottom_margin)


class RoundedFrame(_AbstractFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._heightPercent: float = 0.7

    def _drawFrame(self, painter: QPainter, rect: QRect):
        path = QPainterPath()
        path.moveTo(self._frameBorderWidth, self._frameBorderWidth)
        path.lineTo(rect.topRight().x(), rect.topRight().y())

        height = rect.height() * self._heightPercent
        path.lineTo(rect.bottomRight().x(), height)
        path.quadTo(rect.center().x(), rect.bottom() - self._frameBorderWidth, rect.bottomLeft().x(), height)
        path.lineTo(rect.bottomLeft().x(), height)
        path.lineTo(rect.topLeft().x(), rect.topLeft().y())

        painter.drawPath(path)

    def _calculateMargins(self):
        if self.height():
            bottom_margin = self.height() * (1 - self._heightPercent) + self._frameBorderWidth * 2
        else:
            bottom_margin = self._frameBorderWidth

        margins(self, self._frameBorderWidth * 2, self._frameBorderWidth * 2, self._frameBorderWidth * 2,
                bottom=bottom_margin)
