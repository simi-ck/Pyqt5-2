from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QToolTip
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt
import sys

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.InitGUI()
    def InitGUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label1.setText("<font color=yellow>这是文本标签.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>Python GUI</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("../Image/1.jpg"))

        label4.setText('<a href="https://www.baidu.com">这是百度连接</a>')
        label4.setOpenExternalLinks(True)
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是超级链接")

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
        self.setLayout(layout)
        self.setWindowTitle("Label控件")

    def linkHovered(self):
        print("当鼠标划过label2")

    def linkClicked(self):
        print("鼠标点击label4")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QLabelDemo()
    window.show()
    sys.exit(app.exec_())