from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import sqlite3
import random

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('English helper')
        self.setGeometry(300,250,450,500)

        # Text - add new words
        self.text_add_new_words = QtWidgets.QLabel(self)
        self.text_add_new_words.setText('Add new words')
        self.text_add_new_words.move(170, 10)
        self.text_add_new_words.adjustSize()

        # Text - English 1
        self.text_english_1 = QtWidgets.QLabel(self)
        self.text_english_1.setText('English')
        self.text_english_1.move(10, 30)
        self.text_english_1.adjustSize()

        # Text - Russian 1
        self.text_russian_1 = QtWidgets.QLabel(self)
        self.text_russian_1.setText('Russian')
        self.text_russian_1.move(230, 30)
        self.text_russian_1.adjustSize()

        # Field - add English words
        self.textbox_add_english_words = QtWidgets.QLineEdit(self)
        self.textbox_add_english_words.move(10, 50)
        self.textbox_add_english_words.resize(200,40)

        # Field - add Russian words
        self.textbox_add_russian_words = QtWidgets.QLineEdit(self)
        self.textbox_add_russian_words.move(230, 50)
        self.textbox_add_russian_words.resize(200,40)

        # Button - add to database
        self.btn_add_to_database = QtWidgets.QPushButton(self)
        self.btn_add_to_database.move(10,100)
        self.btn_add_to_database.setText('Add to database')
        self.btn_add_to_database.setFixedWidth(200)
        self.btn_add_to_database.clicked.connect(self.add_in_db)

        # Button - clear database
        self.btn_clear_database = QtWidgets.QPushButton(self)
        self.btn_clear_database.move(230,100)
        self.btn_clear_database.setText('Clear database')
        self.btn_clear_database.setFixedWidth(200)
        self.btn_clear_database.clicked.connect(self.clear_db)

        # Text - check English words
        self.text_check_english_words = QtWidgets.QLabel(self)
        self.text_check_english_words.setText('Check English words')
        self.text_check_english_words.move(150, 140)
        self.text_check_english_words.adjustSize()

        # Text - English 2
        self.text_english_2 = QtWidgets.QLabel(self)
        self.text_english_2.setText('English')
        self.text_english_2.move(10, 160)
        self.text_english_2.adjustSize()

        # Text - Russian 2
        self.text_russian_2 = QtWidgets.QLabel(self)
        self.text_russian_2.setText('Russian')
        self.text_russian_2.move(230, 160)
        self.text_russian_2.adjustSize()

        # Field - check English words
        self.textbox_check_english_words = QtWidgets.QLineEdit(self)
        self.textbox_check_english_words.move(10, 180)
        self.textbox_check_english_words.resize(200,40)

        # Text - Russian word
        self.text_russian_word = QtWidgets.QLabel(self)
        self.text_russian_word.setText('- ...')
        self.text_russian_word.move(230, 185)
        self.text_russian_word.setFixedWidth(200)

        # Button - check English words
        self.btn_check_english_words = QtWidgets.QPushButton(self)
        self.btn_check_english_words.move(10,230)
        self.btn_check_english_words.setText('Check')
        self.btn_check_english_words.setFixedWidth(200)
        self.btn_check_english_words.clicked.connect(self.check_en)

        # Text - check Russian words
        self.text_check_russian_words = QtWidgets.QLabel(self)
        self.text_check_russian_words.setText('Check Russian words')
        self.text_check_russian_words.move(150, 270)
        self.text_check_russian_words.adjustSize()

        # Text - English 3
        self.text_english_3 = QtWidgets.QLabel(self)
        self.text_english_3.setText('English')
        self.text_english_3.move(10, 290)
        self.text_english_3.adjustSize()

        # Text - Russian 3
        self.text_russian_3 = QtWidgets.QLabel(self)
        self.text_russian_3.setText('Russian')
        self.text_russian_3.move(230, 290)
        self.text_russian_3.adjustSize()

        # Text - English word
        self.text_english_word = QtWidgets.QLabel(self)
        self.text_english_word.setText('... -')
        self.text_english_word.move(10, 315)
        self.text_english_word.setFixedWidth(200)

        # Field - check Russian words
        self.textbox_check_russian_words = QtWidgets.QLineEdit(self)
        self.textbox_check_russian_words.move(220, 310)
        self.textbox_check_russian_words.resize(200,40)

        # Button - check Russian words
        self.btn_check_russian_words = QtWidgets.QPushButton(self)
        self.btn_check_russian_words.move(10,360)
        self.btn_check_russian_words.setText('Check')
        self.btn_check_russian_words.setFixedWidth(200)
        self.btn_check_russian_words.clicked.connect(self.check_ru)

        # Text - result 1
        self.text_result = QtWidgets.QLabel(self)
        self.text_result.setText('Result')
        self.text_result.move(200, 435)
        self.text_result.adjustSize()

        # Connect and cursor for database
        self.con = sqlite3.connect('english.db')
        self.cur = self.con.cursor()

        # Memory of words
        self.en = ''
        self.ru = ''

    def add_in_db(self):
        en = self.textbox_add_english_words.text().split(',')
        ru = self.textbox_add_russian_words.text().split(',')

        if len(en) == len(ru):
            for i in range(len(en)):
                self.cur.execute(f"INSERT INTO words VALUES ('{en[i]}','{ru[i]}')")

        self.con.commit()

    def clear_db(self):
        self.cur.execute("DELETE FROM words;")
        self.con.commit()

    def check_en(self):
        if self.text_russian_word.text() != '- ...':
            if self.en == self.textbox_check_english_words.text():
                self.text_result.setText(self.en + ' - ' + self.text_russian_word.text())
                self.text_result.adjustSize()
                self.text_result.move(150, 435)
                self.text_result.setStyleSheet('color: green')
            else:
                self.text_result.setText(self.textbox_check_english_words.text() + ' - ' + self.text_russian_word.text())
                self.text_result.move(150, 435)
                self.text_result.setStyleSheet('color: red')
        self.cur.execute("SELECT * FROM words;")

        words = self.cur.fetchall()
        word = random.choice(words)
        self.text_russian_word.setText(word[1])
        self.en = word[0]

    def check_ru(self):
        if self.text_english_word.text() != '... -':
            if self.ru == self.textbox_check_russian_words.text():
                self.text_result.setText(self.text_english_word.text() + ' - ' + self.ru)
                self.text_result.adjustSize()
                self.text_result.move(150, 435)
                self.text_result.setStyleSheet('color: green')
            else:
                self.text_result.setText(self.text_english_word.text() + ' - ' + self.textbox_check_russian_words.text())
                self.text_result.move(150, 435)
                self.text_result.setStyleSheet('color: red')
        self.cur.execute("SELECT * FROM words;")

        words = self.cur.fetchall()
        word = random.choice(words)
        self.text_english_word.setText(word[0])
        self.ru = word[1]

    def create_table(self):
        self.cur = self.con.cursor()
        try:
            self.cur.execute("SELECT * FROM words;")
        except:
            self.cur.execute("CREATE TABLE words (english, russian);")
        self.con.commit()
        

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.create_table()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()