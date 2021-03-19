'''
计算器构件
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initGui()

    def initGui(self):
        self.setWindowTitle("计算器使用")
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.label = QLabel("当前值")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.sb = QSpinBox()
        self.sb.setValue(18)
        self.sb.setRange(10, 20)
        self.sb.setSingleStep(2)
        layout.addWidget(self.sb)
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText("当前值" + str(self.sb.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())