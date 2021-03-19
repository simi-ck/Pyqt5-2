from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()
    def initGUI(self):
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(3)
        edit1.setAlignment(Qt.AlignCenter)
        edit1.setFont(QFont('Arial', 20))

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        edit3 = QLineEdit()
        edit3.setInputMask("99_9999_9999;#")

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.changeText)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)

        edit6 = QLineEdit()
        edit6.setReadOnly(True)

        formLayout = QFormLayout()
        formLayout.addRow("编辑1", edit1)
        formLayout.addRow("编辑2", edit2)
        formLayout.addRow("编辑3", edit3)
        formLayout.addRow("文本变化", edit4)
        formLayout.addRow("密码", edit5)
        formLayout.addRow("只读", edit6)

        self.setLayout(formLayout)
        self.setWindowTitle("QLineEdit综合案例")

    def changeText(self, text):
        print("输入内容" + text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditDemo()
    window.show()
    sys.exit(app.exec_())
