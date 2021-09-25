from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('English helper')
    window.setGeometry(300,250,450,300)

    text_1 = QtWidgets.QLabel(window)
    text_1.setText('Add new words')
    text_1.move(10, 10)
    text_1.adjustSize()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()

