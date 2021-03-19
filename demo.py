import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import demo4

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    w = demo4.Ui_MainWindow()
    w.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

