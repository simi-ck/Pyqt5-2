from PyQt5.QtWidgets import QLabel, QLineEdit, QApplication, QDialog, QPushButton, QGridLayout
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initGUI()
    def initGUI(self):
        self.setWindowTitle("QLabel和伙伴关系")
        nameLabel = QLabel('&name', self)
        nameLabelText = QLineEdit(self)
        nameLabel.setBuddy(nameLabelText)

        passwordLabel = QLabel('&password', self)
        passwordLabelText = QLineEdit(self)
        passwordLabel.setBuddy(nameLabelText)

        btnOK = QPushButton("&Ok")
        btnCancel = QPushButton("&Cancel")

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLabelText, 0, 1, 1, 2)
        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLabelText, 1, 1, 1, 2)
        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelBuddy()
    window.show()
    sys.exit(app.exec_())
