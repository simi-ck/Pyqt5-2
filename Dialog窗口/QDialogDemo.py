from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initGui()

    def initGui(self):
        self.setWindowTitle("Dialog对话框")
        self.resize(400, 300)

        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle("对话框")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialogDemo()
    window.show()
    sys.exit(app.exec_())


