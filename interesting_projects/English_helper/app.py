from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('English helper')
        self.setGeometry(300,250,450,500)

        # Text - add new words
        self.text_1 = QtWidgets.QLabel(self)
        self.text_1.setText('Add new words')
        self.text_1.move(10, 10)
        self.text_1.adjustSize()

        # Text - English 1
        self.text_3 = QtWidgets.QLabel(self)
        self.text_3.setText('English')
        self.text_3.move(10, 30)
        self.text_3.adjustSize()

        # Text - Russian 1
        self.text_3 = QtWidgets.QLabel(self)
        self.text_3.setText('Russian')
        self.text_3.move(230, 30)
        self.text_3.adjustSize()

        # Field - add English words
        self.textbox_1 = QtWidgets.QLineEdit(self)
        self.textbox_1.move(10, 50)
        self.textbox_1.resize(200,40)

        # Field - add Russian words
        self.textbox_2 = QtWidgets.QLineEdit(self)
        self.textbox_2.move(230, 50)
        self.textbox_2.resize(200,40)

        # Button - add to database
        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.move(10,100)
        self.btn_1.setText('Add to database')
        self.btn_1.setFixedWidth(200)
        self.btn_1.clicked.connect(add_in_db)

        # Button - clear database
        self.btn_2 = QtWidgets.QPushButton(self)
        self.btn_2.move(230,100)
        self.btn_2.setText('Clear database')
        self.btn_2.setFixedWidth(200)
        self.btn_2.clicked.connect(clear_db)

        # Text - check English words
        self.text_2 = QtWidgets.QLabel(self)
        self.text_2.setText('Check English words')
        self.text_2.move(10, 140)
        self.text_2.adjustSize()

        # Text - English 2
        self.text_3 = QtWidgets.QLabel(self)
        self.text_3.setText('English')
        self.text_3.move(10, 160)
        self.text_3.adjustSize()

        # Text - Russian 2
        self.text_3 = QtWidgets.QLabel(self)
        self.text_3.setText('Russian')
        self.text_3.move(230, 160)
        self.text_3.adjustSize()

        # Field - check English words
        self.textbox_3 = QtWidgets.QLineEdit(self)
        self.textbox_3.move(10, 180)
        self.textbox_3.resize(200,40)

        # Text - Russian word
        self.text_4 = QtWidgets.QLabel(self)
        self.text_4.setText('- ...')
        self.text_4.move(230, 190)
        self.text_4.adjustSize()

        # Button - check English words
        self.btn_3 = QtWidgets.QPushButton(self)
        self.btn_3.move(10,230)
        self.btn_3.setText('Check')
        self.btn_3.setFixedWidth(200)
        self.btn_3.clicked.connect(check_en)

        # Text - check Russian words
        self.text_2 = QtWidgets.QLabel(self)
        self.text_2.setText('Check Russian words')
        self.text_2.move(10, 270)
        self.text_2.adjustSize()

        # Text - English 3
        self.text_3 = QtWidgets.QLabel(self)
        self.text_3.setText('English')
        self.text_3.move(10, 290)
        self.text_3.adjustSize()

        # Text - Russian 3
        self.text_3 = QtWidgets.QLabel(self)
        self.text_3.setText('Russian')
        self.text_3.move(230, 290)
        self.text_3.adjustSize()

        # Text - English word
        self.text_4 = QtWidgets.QLabel(self)
        self.text_4.setText('... -')
        self.text_4.move(10, 320)
        self.text_4.adjustSize()

        # Field - check Russian words
        self.textbox_3 = QtWidgets.QLineEdit(self)
        self.textbox_3.move(220, 310)
        self.textbox_3.resize(200,40)

        # Button - check Russian words
        self.btn_3 = QtWidgets.QPushButton(self)
        self.btn_3.move(10,360)
        self.btn_3.setText('Check')
        self.btn_3.setFixedWidth(200)
        self.btn_3.clicked.connect(check_ru)

        # Text - result
        self.text_4 = QtWidgets.QLabel(self)
        self.text_4.setText('Result')
        self.text_4.move(200, 435)
        self.text_4.adjustSize()

def add_in_db():
    print('Add in database')

def clear_db():
    print('Clear database')

def check_en():
    print('Check English')

def check_ru():
    print('Check Russian')

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()

