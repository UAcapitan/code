from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer

class MyApp(App):
    def build(self):

        return CodeInput(lexer=HtmlLexer())

    def btn_press(self, instance):
        print('Work')
        instance.text = 'Work'

if __name__ == '__main__':
    MyApp().run()