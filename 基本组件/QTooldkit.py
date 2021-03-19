from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QToolTip
from PyQt5.QtGui import QIcon, QFont
import sys
class Tooltip(QMainWindow):
    def __init__(self):
        super(Tooltip, self).__init__()
        QToolTip.setFont(QFont("SansSerif", 12))
        self.setToolTip("要加油")
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle("提示信息")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Tooltip()
    app.setWindowIcon(QIcon("../Image/1.jpg"))
    window.show()
    sys.exit(app.exec_())
