from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditConstrain(QWidget):
    def __init__(self):
        super(QLineEditConstrain, self).__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("校验器")
        formlayout = QFormLayout()

        intLineEdit = QLineEdit(self)
        doubleLineEdit = QLineEdit(self)
        validatorLineEdit = QLineEdit(self)

        formlayout.addRow("整数校验", intLineEdit)
        formlayout.addRow("浮点校验", doubleLineEdit)
        formlayout.addRow("数字和字母校验", validatorLineEdit)

        intLineEdit.setPlaceholderText("请输入整数")
        doubleLineEdit.setPlaceholderText("请输入浮点数")
        validatorLineEdit.setPlaceholderText("请输入数字和字母")

        intValidator = QIntValidator(self)
        intValidator.setRange(1,10)

        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-180, 180)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 小数点后两位
        doubleValidator.setDecimals(2)

        reg = QRegExp('[a-zA-Z0-9]+$')
        regValidator = QRegExpValidator(self)
        regValidator.setRegExp(reg)

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(regValidator)

        self.setLayout(formlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditConstrain()
    window.show()
    sys.exit(app.exec_())

