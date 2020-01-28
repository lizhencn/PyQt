from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('first')
window.resize(500, 400)
window.move(200, 300)
label = QLabel(window)
label.setText('hello')
label.move(100, 100)
window.show()
app.exec_()
# sys.exit(app.exec_())
