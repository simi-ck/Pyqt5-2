import sys

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QSplitter, QHBoxLayout


class MyLineEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragMoveEvent(self, event):
        drag = QDrag(self)
        mime = QMimeData()
        drag.setMimeData(mime)
        drag.exec(Qt.CopyAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mimeData().text())
        event.source().setText("")


class SimpleDrag(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hlayout = QHBoxLayout(self)
        edit1 = MyLineEdit(self)
        edit1.setDragEnabled(True)
        edit2 = MyLineEdit(self)
        edit2.setDragEnabled(True)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(edit1)
        splitter.addWidget(edit2)
        hlayout.addWidget(splitter)
        self.setLayout(hlayout)
        self.setWindowTitle('简易的拖动事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleDrag()
    ex.show()
    app.exec_()