from PyQt5.QtWidgets import QApplication, QFormLayout, QWidget, QLineEdit
import sys

class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("文本输入模式")
        layout = QFormLayout()
        normalLineEdit = QLineEdit(self)
        noEchoLineEdit = QLineEdit(self)
        passwordLineEdit = QLineEdit(self)
        passwordEchoOnLineEdit = QLineEdit(self)

        layout.addRow("Normal", normalLineEdit)
        layout.addRow("NoEcho", noEchoLineEdit)
        layout.addRow("Password", passwordLineEdit)
        layout.addRow("PasswordEchoOnEdit", passwordEchoOnLineEdit)

        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLineEditDemo()
    window.show()
    sys.exit(app.exec_())
