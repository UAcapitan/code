import googletrans
import sys
import PyQt5.QtWidgets as qt5

translator = googletrans.Translator()

class TranslateApp(qt5.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup for main window
        self.resize(500, 500)
        self.move(300, 300)
        self.setWindowTitle('TranslateApp')

        # Name app
        self.label = qt5.QLabel('Translator', self)
        self.label.move(10,5)

        # Src label
        self.label_src = qt5.QLabel('Src', self)
        self.label_src.move(25,40)

        # Dest label
        self.label_dest = qt5.QLabel('Dest', self)
        self.label_dest.move(275,40)

        # Field for src
        self.text_src = qt5.QPlainTextEdit(self)
        self.text_src.insertPlainText('')
        self.text_src.move(25,70)
        self.text_src.resize(200,30)

        # Symbol between fields
        self.label_sym = qt5.QLabel('->', self)
        self.label_sym.move(242,70)

        # Field for dest
        self.text_dest = qt5.QPlainTextEdit(self)
        self.text_dest.insertPlainText('')
        self.text_dest.move(275,70)
        self.text_dest.resize(200,30)

        # Text after main field
        self.label_input = qt5.QLabel('Input your text', self)
        self.label_input.move(25,110)
        self.label_input.resize(200, 20)
        
        # Field for text for translate
        self.text_for_translate = qt5.QPlainTextEdit(self)
        self.text_for_translate.insertPlainText('')
        self.text_for_translate.move(25,140)
        self.text_for_translate.resize(450,100)

        # Button for translate
        self.button = qt5.QPushButton('Translate', self)
        self.button.move(200,260)

        # Label before button
        self.label_input = qt5.QLabel('v', self)
        self.label_input.move(249,290)

        # Field for translated text
        self.text_translated = qt5.QPlainTextEdit(self)
        self.text_translated.insertPlainText('')
        self.text_translated.move(25,330)
        self.text_translated.resize(450,100)
        self.text_translated.setReadOnly(True)

        self.show()

    def translate(self, t, src, dest):
        result = translator.translate(t, src=src, dest=dest)
        self.text_translated.setPlainText(result.text)
        return result.text

    def exit(self,app):
        sys.exit(app.exec())

if __name__ == '__main__':
    app = qt5.QApplication(sys.argv)
    translate_app = TranslateApp()
    print(translate_app.translate('Привет! Как дела? Что нового у тебя?', 'ru', 'en'))
    translate_app.exit(app)