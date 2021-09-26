from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('English helper')
        self.setGeometry(300,250,450,500)

        # Text - add new words
        text_1 = QtWidgets.QLabel(self)
        text_1.setText('Add new words')
        text_1.move(10, 10)
        text_1.adjustSize()

        # Button - add to database
        btn_1 = QtWidgets.QPushButton(self)
        btn_1.move(10,100)
        btn_1.setText('Add to database')
        btn_1.setFixedWidth(200)
        btn_1.clicked.connect(add_in_db)

        # Button - clear database
        btn_2 = QtWidgets.QPushButton(self)
        btn_2.move(230,100)
        btn_2.setText('Clear database')
        btn_2.setFixedWidth(200)
        btn_2.clicked.connect(clear_db)

        # Text - check English words
        text_2 = QtWidgets.QLabel(self)
        text_2.setText('Check English words')
        text_2.move(10, 140)
        text_2.adjustSize()

        # Button - check English words
        btn_3 = QtWidgets.QPushButton(self)
        btn_3.move(10,230)
        btn_3.setText('Check')
        btn_3.setFixedWidth(200)
        btn_3.clicked.connect(check_en)

        # Field - add English words
        self.textbox_1 = QtWidgets.QLineEdit(self)
        self.textbox_1.move(10, 50)
        self.textbox_1.resize(200,40)

        # Field - add Russian words
        self.textbox_2 = QtWidgets.QLineEdit(self)
        self.textbox_2.move(230, 50)
        self.textbox_2.resize(200,40)

        # Text - English 1
        text_3 = QtWidgets.QLabel(self)
        text_3.setText('English')
        text_3.move(10, 30)
        text_3.adjustSize()

        # Text - Russian 1
        text_3 = QtWidgets.QLabel(self)
        text_3.setText('Russian')
        text_3.move(230, 30)
        text_3.adjustSize()

        # Text - English 2
        text_3 = QtWidgets.QLabel(self)
        text_3.setText('English')
        text_3.move(10, 160)
        text_3.adjustSize()

        # Field - check English words
        self.textbox_3 = QtWidgets.QLineEdit(self)
        self.textbox_3.move(10, 180)
        self.textbox_3.resize(200,40)

        # Text - Russian 2
        text_3 = QtWidgets.QLabel(self)
        text_3.setText('Russian')
        text_3.move(230, 160)
        text_3.adjustSize()

        # Text - Russian word
        text_4 = QtWidgets.QLabel(self)
        text_4.setText('- ...')
        text_4.move(230, 190)
        text_4.adjustSize()

        # Text - check Russian words
        text_2 = QtWidgets.QLabel(self)
        text_2.setText('Check Russian words')
        text_2.move(10, 270)
        text_2.adjustSize()

        # Button - check Russian words
        btn_3 = QtWidgets.QPushButton(self)
        btn_3.move(10,360)
        btn_3.setText('Check')
        btn_3.setFixedWidth(200)
        btn_3.clicked.connect(check_en)

        # Text - English 3
        text_3 = QtWidgets.QLabel(self)
        text_3.setText('English')
        text_3.move(10, 290)
        text_3.adjustSize()

        # Field - check Russian words
        self.textbox_3 = QtWidgets.QLineEdit(self)
        self.textbox_3.move(220, 310)
        self.textbox_3.resize(200,40)

        # Text - Russian 3
        text_3 = QtWidgets.QLabel(self)
        text_3.setText('Russian')
        text_3.move(230, 290)
        text_3.adjustSize()

        # Text - English word
        text_4 = QtWidgets.QLabel(self)
        text_4.setText('... -')
        text_4.move(10, 320)
        text_4.adjustSize()

        # Text - result
        text_4 = QtWidgets.QLabel(self)
        text_4.setText('Result')
        text_4.move(200, 435)
        text_4.adjustSize()

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

