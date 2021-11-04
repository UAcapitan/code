import googletrans
import sys
import PyQt5.QtWidgets as qt5

translator = googletrans.Translator()

class TranslateApp(qt5.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setup for main window
        self.resize(500, 450)
        self.move(300, 300)
        self.setWindowTitle('TranslateApp')

        # Menu
        self.menuBar = self.menuBar()
        self.fileMenu = qt5.QMenu("&Main", self)
        self.menuBar.addMenu(self.fileMenu)

        self.save_file_item = self.fileMenu.addAction('Save in file')
        self.save_file_item.triggered.connect(self.save_text)
        self.save_all_file_item = self.fileMenu.addAction('Save all text in file')
        self.save_all_file_item.triggered.connect(self.save_all_text)
        self.all_lang_item = self.fileMenu.addAction('All languages')
        self.all_lang_item.triggered.connect(self.all_languages)
        self.exit_item = self.fileMenu.addAction('Exit')
        self.exit_item.triggered.connect(app.instance().quit)

        self.editMenu = self.menuBar.addMenu("&Update")
        self.about_version_item = self.editMenu.addAction('About this version')
        self.about_version_item.triggered.connect(self.about_version)
        self.open_site_item = self.editMenu.addAction('Open official site')
        self.open_site_item.triggered.connect(self.open_site)
        self.what_is_new_item = self.editMenu.addAction('What`s new?')
        self.what_is_new_item.triggered.connect(self.what_is_new)

        self.helpMenu = self.menuBar.addMenu("&Help")
        self.support_item = self.helpMenu.addAction('Support')
        self.support_item.triggered.connect(self.support)
        self.about_program_item = self.helpMenu.addAction('About program')
        self.about_program_item.triggered.connect(self.about_program)
        self.about_author_item = self.helpMenu.addAction('About author')
        self.about_author_item.triggered.connect(self.about_author)

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
        self.button.clicked.connect(self.translate)

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

    # Function translate text
    def translate(self):
        result = translator.translate(self.text_for_translate.toPlainText(), src=self.text_src.toPlainText(), dest=self.text_dest.toPlainText())
        self.text_translated.setPlainText(result.text)

    # Functions for menu
    def save_text(self):
        self.nw_save_text = AnotherWindow('Save text in file', [400, 400])
        self.nw_save_text.show()

    def save_all_text(self):
        self.nw_save_all_text = AnotherWindow('Save all text in file', [400, 400])
        self.nw_save_all_text.show()

    def all_languages(self):
        self.nw_all_lang = AnotherWindow('All languages', [400, 400])
        self.nw_all_lang.show()

    def about_version(self):
        self.nw_about_version = AnotherWindow('About this version', [400, 150])
        self.nw_about_version.show()

    def open_site(self):
        self.nw_open_site = AnotherWindow('Open site', [400, 150])
        self.nw_open_site.show()

    def what_is_new(self):
        self.nw_what_is_new = AnotherWindow('What`s new?', [400, 200])
        self.nw_what_is_new.show()

    def support(self):
        self.nw_support = AnotherWindow('Support', [400, 250])
        self.nw_support.show()

    def about_program(self):
        self.nw_about_program = AnotherWindow('About program', [400, 200])
        self.nw_about_program.show()

    def about_author(self):
        self.nw_about_author = AnotherWindow('About author', [400, 200])
        self.nw_about_author.show()

    # Function exit
    def exit(self,app):
        sys.exit(app.exec())

# Class for create new window
class AnotherWindow(qt5.QWidget):
    def __init__(self, name: str, size: list):
        super().__init__()
        self.setWindowTitle(name)
        self.resize(size[0], size[1])

if __name__ == '__main__':
    app = qt5.QApplication(sys.argv)
    translate_app = TranslateApp()
    translate_app.exit(app)