'''

颜色对话框：QColorDialog

'''

'''

字体对话框：QFontDialog
QPalette:Base，指文本输入窗口部件（比如QtTextEdit，QLineEdit等）的背景色.
QPalette:Text，与QPalette:Base一块使用，指文本输入窗口部件的前景色；
QPalette:Button，指按钮窗口部件的背景色；
QPalette:ButtonText，指按钮窗口部件的前景色.


'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog例子')
        layout = QVBoxLayout()
        self.colorButton = QPushButton('设置颜色')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorButton1 = QPushButton('设置背景颜色')
        self.colorButton1.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorButton1)

        self.colorLabel = QLabel('Hello，测试颜色例子')
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)
    def getColor(self):
        color = QColorDialog.getColor()
        color = QColorDialog.getColor()
        p = QPalette()
        # p = QPalette()
        # QPalette.WindowText指的是窗口部件的前景色
        p.setColor(QPalette.WindowText, color)
        # p.setColor(QPalette.WindowText,color)
        self.colorLabel.setPalette(p)
        # self.colorLabel.setPalette(p)
    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        # QPalette.Window指的是窗口部件的背景色

        p.setColor(QPalette.Window,color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())

