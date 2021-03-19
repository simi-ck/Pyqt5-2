from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget
import sys
class QuitMainWindow(QMainWindow):
    def __init__(self):
        super(QuitMainWindow, self).__init__()
        self.resize(600, 400)
        self.setWindowTitle("退出应用程序实例")
        # 设置button
        self.button1 = QPushButton("退出")
        # 信号和槽绑定
        self.button1.clicked.connect(self.onClickAction)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClickAction(self):
        sender = self.sender()
        print(sender.text() + "按钮被按下")
        app = QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuitMainWindow()
    window.show()
    sys.exit(app.exec_())