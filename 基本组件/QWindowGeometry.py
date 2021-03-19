from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys
def onclickButton():
    print(1)
    print("Widget.x = %d" % widget.x())
    print("Widget.y = %d" % widget.y())
    print("Widget.width = %d" % widget.width())
    print("Widget.height = %d" % widget.height())

    print(2)
    print("Widget.geometry.x = %d" % widget.geometry().x())
    print("Widget.geometry.y = %d" % widget.geometry().y())
    print("Widget.geometry.width = %d" % widget.geometry().width())
    print("Widget.geometry.height = %d" % widget.geometry().height())

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("显示坐标")
btn.clicked.connect(onclickButton)
btn.move(24, 52)
widget.resize(400,300)
widget.move(250, 200)
widget.setWindowTitle("坐标")
widget.show()
sys.exit(app.exec_())

