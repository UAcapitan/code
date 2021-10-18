from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import sqlite3
import random
import os

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
        self.text_english_1.move(10, 40)
        self.text_english_1.adjustSize()

        # Text - Russian 1
        self.text_russian_1 = QtWidgets.QLabel(self)
        self.text_russian_1.setText('Russian')
        self.text_russian_1.move(230, 40)
        self.text_russian_1.adjustSize()

        # Field - add English words
        self.textbox_add_english_words = QtWidgets.QLineEdit(self)
        self.textbox_add_english_words.move(10, 60)
        self.textbox_add_english_words.resize(200,40)

        # Field - add Russian words
        self.textbox_add_russian_words = QtWidgets.QLineEdit(self)
        self.textbox_add_russian_words.move(230, 60)
        self.textbox_add_russian_words.resize(200,40)

        # Button - add to database
        self.btn_add_to_database = QtWidgets.QPushButton(self)
        self.btn_add_to_database.move(10,110)
        self.btn_add_to_database.setText('Add to database')
        self.btn_add_to_database.setFixedWidth(200)
        self.btn_add_to_database.clicked.connect(self.add_in_db)

        # Button - clear database
        self.btn_clear_database = QtWidgets.QPushButton(self)
        self.btn_clear_database.move(230,110)
        self.btn_clear_database.setText('Clear database')
        self.btn_clear_database.setFixedWidth(200)
        self.btn_clear_database.clicked.connect(self.clear_db)

        # Text - check English words
        self.text_check_english_words = QtWidgets.QLabel(self)
        self.text_check_english_words.setText('Check English words')
        self.text_check_english_words.move(150, 150)
        self.text_check_english_words.adjustSize()

        # Text - English 2
        self.text_english_2 = QtWidgets.QLabel(self)
        self.text_english_2.setText('English')
        self.text_english_2.move(10, 180)
        self.text_english_2.adjustSize()

        # Text - Russian 2
        self.text_russian_2 = QtWidgets.QLabel(self)
        self.text_russian_2.setText('Russian')
        self.text_russian_2.move(230, 180)
        self.text_russian_2.adjustSize()

        # Field - check English words
        self.textbox_check_english_words = QtWidgets.QLineEdit(self)
        self.textbox_check_english_words.move(10, 200)
        self.textbox_check_english_words.resize(200,40)

        # Text - Russian word
        self.text_russian_word = QtWidgets.QLabel(self)
        self.text_russian_word.setText('- ...')
        self.text_russian_word.move(230, 205)
        self.text_russian_word.setFixedWidth(200)

        # Button - check English words
        self.btn_check_english_words = QtWidgets.QPushButton(self)
        self.btn_check_english_words.move(10,250)
        self.btn_check_english_words.setText('Check')
        self.btn_check_english_words.setFixedWidth(200)
        self.btn_check_english_words.clicked.connect(self.check_en)

        # Text - check Russian words
        self.text_check_russian_words = QtWidgets.QLabel(self)
        self.text_check_russian_words.setText('Check Russian words')
        self.text_check_russian_words.move(150, 290)
        self.text_check_russian_words.adjustSize()

        # Text - English 3
        self.text_english_3 = QtWidgets.QLabel(self)
        self.text_english_3.setText('English')
        self.text_english_3.move(10, 320)
        self.text_english_3.adjustSize()

        # Text - Russian 3
        self.text_russian_3 = QtWidgets.QLabel(self)
        self.text_russian_3.setText('Russian')
        self.text_russian_3.move(230, 320)
        self.text_russian_3.adjustSize()

        # Text - English word
        self.text_english_word = QtWidgets.QLabel(self)
        self.text_english_word.setText('... -')
        self.text_english_word.move(10, 345)
        self.text_english_word.setFixedWidth(200)

        # Field - check Russian words
        self.textbox_check_russian_words = QtWidgets.QLineEdit(self)
        self.textbox_check_russian_words.move(230, 340)
        self.textbox_check_russian_words.resize(200,40)

        # Button - check Russian words
        self.btn_check_russian_words = QtWidgets.QPushButton(self)
        self.btn_check_russian_words.move(10,390)
        self.btn_check_russian_words.setText('Check')
        self.btn_check_russian_words.setFixedWidth(200)
        self.btn_check_russian_words.clicked.connect(self.check_ru)

        # Text - result
        self.text_result = QtWidgets.QLabel(self)
        self.text_result.setText('Result')
        self.text_result.move(200, 445)
        self.text_result.adjustSize()

        # Text - true result
        self.text_true_result = QtWidgets.QLabel(self)
        self.text_true_result.setText('')
        self.text_true_result.move(200, 465)
        self.text_true_result.adjustSize()

        # Connect and cursor for database
        dir = __file__.replace('app.py', 'english.db')

        self.con = sqlite3.connect(dir)
        
        self.cur = self.con.cursor()

        # Memory of words
        self.en = ''
        self.ru = ''

    def add_in_db(self):
        en = self.textbox_add_english_words.text().replace(' ', '').split(',')
        ru = self.textbox_add_russian_words.text().replace(' ', '').split(',')

        if len(en) == len(ru):
            self.textbox_add_english_words.setText('')
            self.textbox_add_russian_words.setText('')
            
            j = 0
            for i in range(len(en)):
                self.cur.execute(f"INSERT INTO words VALUES ('{en[i]}','{ru[i]}')")
                j += 1
            self.text_result.setText(f'Success. {j} words added')
            self.result_styles('green')
        else:
            self.text_result.setText('Error')
            self.result_styles('red')

        self.con.commit()

    def clear_db(self):
        self.cur.execute("DELETE FROM words;")
        self.con.commit()
        self.text_result.setText('Success clean')
        self.result_styles('green')

    def check_en(self):
        if self.text_russian_word.text() != '- ...':
            if self.en == self.textbox_check_english_words.text():
                self.text_result.setText(self.en + ' - ' + self.text_russian_word.text())
                self.text_true_result.setText('')
                self.result_styles('green')
                self.result_true_styles()
            else:
                self.text_result.setText(self.textbox_check_english_words.text() + ' - ' + self.text_russian_word.text())
                self.text_true_result.setText(self.en + ' - ' + self.ru)
                self.result_styles('red')
                self.result_true_styles()
        self.cur.execute("SELECT * FROM words;")

        self.textbox_check_english_words.setText('')

        words = self.cur.fetchall()
        word = random.choice(words)
        self.text_russian_word.setText(word[1])
        self.en = word[0]

    def check_ru(self):
        if self.text_english_word.text() != '... -':
            if self.ru == self.textbox_check_russian_words.text():
                self.text_result.setText(self.text_english_word.text() + ' - ' + self.ru)
                self.text_true_result.setText('')
                self.result_styles('green')
                self.result_true_styles()
            else:
                self.text_result.setText(self.text_english_word.text() + ' - ' + self.textbox_check_russian_words.text())
                self.text_true_result.setText(self.en + ' - ' + self.ru)
                self.result_styles('red')
                self.result_true_styles()

        self.cur.execute("SELECT * FROM words;")

        self.textbox_check_russian_words.setText('')

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

    def result_styles(self, color):
        self.text_result.adjustSize()
        self.text_result.move(int(220-(self.text_result.width() / 2)), 445)
        self.text_result.setStyleSheet('color: ' + color)

    def result_true_styles(self):
        self.text_true_result.adjustSize()
        self.text_true_result.move(int(220-(self.text_true_result.width() / 2)), 465)
        self.text_true_result.setStyleSheet('color: green')

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.create_table()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()