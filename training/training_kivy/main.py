from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(
            text='This is my first button', 
            font_size=30,
            on_press=self.btn_press
        )

    def btn_press(self, instance):
        print('Work')

if __name__ == '__main__':
    MyApp().run()