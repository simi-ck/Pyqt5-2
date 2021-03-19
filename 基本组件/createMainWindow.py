import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon

class FirstWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstWindow, self).__init__(parent)
        self.setWindowTitle("第一个GUI")
        self.resize(600,400)
        self.status = self.statusBar()
        self.status.showMessage("只存在5秒的消息", 5000)
    def center(self):
        # 获取窗口坐标系
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        dw = int((screen.width() - size.width())/2)
        dh = int((screen.height() - size.height())/2)
        self.move(dw, dh)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("../Image/1.jpg"))
    window = FirstWindow()

    window.show()
    window.center()
    # 进入程序主循环
    sys.exit(app.exec_())

