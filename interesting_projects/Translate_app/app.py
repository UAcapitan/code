import googletrans
import sys
import PyQt5.QtWidgets as qt5
import webbrowser

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

    # Functions for open menu windows
    def save_text(self):
        self.nw_save_text = AnotherWindow('Save text in file', [400, 115])
        self.nw_save_text.label_address = qt5.QLabel('Address for save file', self.nw_save_text)
        self.nw_save_text.label_address.move(10,10)
        self.nw_save_text.text_address = qt5.QPlainTextEdit(self.nw_save_text)
        self.nw_save_text.text_address.insertPlainText('D://text.txt')
        self.nw_save_text.text_address.move(10,30)
        self.nw_save_text.text_address.resize(380,30)
        self.nw_save_text.button_save = qt5.QPushButton('Save', self.nw_save_text)
        self.nw_save_text.button_save.move(250,70)
        self.nw_save_text.button_save.clicked.connect(self.save_in_file_button)
        self.nw_save_text.show()

    def save_all_text(self):
        self.nw_save_all_text = AnotherWindow('Save text in file', [400, 115])
        self.nw_save_all_text.label_address = qt5.QLabel('Address for save file', self.nw_save_all_text)
        self.nw_save_all_text.label_address.move(10,10)
        self.nw_save_all_text.text_address = qt5.QPlainTextEdit(self.nw_save_all_text)
        self.nw_save_all_text.text_address.insertPlainText('D://text_all.txt')
        self.nw_save_all_text.text_address.move(10,30)
        self.nw_save_all_text.text_address.resize(380,30)
        self.nw_save_all_text.button_save = qt5.QPushButton('Save', self.nw_save_all_text)
        self.nw_save_all_text.button_save.move(250,70)
        self.nw_save_all_text.button_save.clicked.connect(self.save_all_in_file_button)
        self.nw_save_all_text.show()

    def all_languages(self):
        self.nw_all_lang = AnotherWindow('All languages', [200, 400])
        
        all_lang = ''
        for k, v in googletrans.LANGUAGES.items():
            all_lang += k + ' - ' + v + '\n'

        self.nw_all_lang.all_lang = qt5.QPlainTextEdit(self.nw_all_lang)
        self.nw_all_lang.all_lang.insertPlainText(all_lang)
        self.nw_all_lang.all_lang.move(10,10)
        self.nw_all_lang.all_lang.resize(180,380)
        self.nw_all_lang.all_lang.setReadOnly(True)
        self.nw_all_lang.show()

    def about_version(self):
        self.nw_about_version = AnotherWindow('About this version', [400, 60])
        self.nw_about_version.label_text = qt5.QLabel('Version', self.nw_about_version)
        self.nw_about_version.label_text.move(10,10)
        self.nw_about_version.label_version = qt5.QLabel('1.00', self.nw_about_version)
        self.nw_about_version.label_version.move(10,30)
        self.nw_about_version.show()

    def open_site(self):
        self.nw_open_site = AnotherWindow('Open site', [400, 70])
        self.nw_open_site.label_text = qt5.QLabel('Official site', self.nw_open_site)
        self.nw_open_site.label_text.move(10,10)
        self.nw_open_site.button_open = qt5.QPushButton('Open', self.nw_open_site)
        self.nw_open_site.button_open.move(10,30)
        self.nw_open_site.button_open.clicked.connect(self.open_official_site)
        self.nw_open_site.show()

    def what_is_new(self):
        self.nw_what_is_new = AnotherWindow('What`s new?', [400, 80])
        self.nw_what_is_new.label_text = qt5.QLabel('New Updates', self.nw_what_is_new)
        self.nw_what_is_new.label_text.move(10,10)
        self.nw_what_is_new.label_updates = qt5.QLabel('- Working menu windows\n- Saving translations with the original text', self.nw_what_is_new)
        self.nw_what_is_new.label_updates.move(10,30)
        self.nw_what_is_new.show()

    def support(self):
        self.nw_support = AnotherWindow('Support', [400, 70])
        self.nw_support.label_text = qt5.QLabel('Support mail:', self.nw_support)
        self.nw_support.label_text.move(10,10)
        self.nw_support.all_lang = qt5.QPlainTextEdit(self.nw_support)
        self.nw_support.all_lang.insertPlainText('ua.capitan@gmail.com')
        self.nw_support.all_lang.move(10,30)
        self.nw_support.all_lang.resize(380,30)
        self.nw_support.all_lang.setReadOnly(True)
        self.nw_support.show()

    def about_program(self):
        self.nw_about_program = AnotherWindow('About program', [400, 115])
        self.nw_about_program.label_text = qt5.QLabel('About program', self.nw_about_program)
        self.nw_about_program.label_text.move(10,10)
        self.nw_about_program.label_about = qt5.QLabel('This is program for translating text. Also\nyou can save translated text in file.\nYou can see all possible language\nin menu item `All languages`.', self.nw_about_program)
        self.nw_about_program.label_about.move(10,30)
        self.nw_about_program.show()

    def about_author(self):
        self.nw_about_author = AnotherWindow('About author', [400, 80])
        self.nw_about_author.label_text = qt5.QLabel('About author', self.nw_about_author)
        self.nw_about_author.label_text.move(10,10)
        self.nw_about_author.label_author = qt5.QLabel('I am Ed. I am Python developer. You can\nsee my portfolio in menu item `Official site`.', self.nw_about_author)
        self.nw_about_author.label_author.move(10,30)
        self.nw_about_author.show()

    # Function for save in files
    def save_in_file_button(self):
        with open(self.nw_save_text.text_address.toPlainText(), 'a') as f:
            f.write(self.text_translated.toPlainText() + '\n\n')
        self.nw_save_text.hide()

    def save_all_in_file_button(self):
        with open(self.nw_save_all_text.text_address.toPlainText(), 'a') as f:
            f.write(self.text_for_translate.toPlainText() + '\n\n')
            f.write(self.text_translated.toPlainText() + '\n\n-------------------------------------------\n\n')
        self.nw_save_all_text.hide()

    # Open official site
    def open_official_site(self):
        webbrowser.open('http://edmix.herokuapp.com/')

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