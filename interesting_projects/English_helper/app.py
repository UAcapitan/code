from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('English helper')
        self.setGeometry(300,250,450,500)

        text_1 = QtWidgets.QLabel(self)
        text_1.setText('Add new words')
        text_1.move(10, 10)
        text_1.adjustSize()

        # Buttons
        btn_1 = QtWidgets.QPushButton(self)
        btn_1.move(10,150)
        btn_1.setText('Add to database')
        btn_1.setFixedWidth(200)
        btn_1.clicked.connect(add_in_db)

        btn_2 = QtWidgets.QPushButton(self)
        btn_2.move(220,150)
        btn_2.setText('Clear database')
        btn_2.setFixedWidth(200)
        btn_2.clicked.connect(clear_db)

        text_2 = QtWidgets.QLabel(self)
        text_2.setText('Add new words')
        text_2.move(10, 200)
        text_2.adjustSize()

        btn_3 = QtWidgets.QPushButton(self)
        btn_3.move(10,270)
        btn_3.setText('Check')
        btn_3.setFixedWidth(200)
        btn_3.clicked.connect(check_en)

def add_in_db():
    print('Add in database')

def clear_db():
    print('Clear database')

def check_en():
    print('Check English')

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()

