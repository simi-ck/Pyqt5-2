from PyQt5.QtWidgets import *
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("用掩码限制LineEdit输入")
        formlayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        ipLineEdit.setInputMask("000.000.000.000;_")
        macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        dateLineEdit.setInputMask("0000-00-00")
        licenseLineEdit.setInputMask('>AAAA-AAAA-AAAA-AAAA-AAAA;#')

        formlayout.addRow("ip掩码", ipLineEdit)
        formlayout.addRow("mac掩码", macLineEdit)
        formlayout.addRow("日期掩码", dateLineEdit)
        formlayout.addRow("证书掩码", licenseLineEdit)

        self.setLayout(formlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditMask()
    window.show()
    sys.exit(app.exec_())

