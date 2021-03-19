from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QIcon
import sys
class IconWindow(QMainWindow):
    def __init__(self):
        super(IconWindow, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle("窗口图标")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IconWindow()
    app.setWindowIcon(QIcon("../Image/1.jpg"))
    window.show()
    sys.exit(app.exec_())
