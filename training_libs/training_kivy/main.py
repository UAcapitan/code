from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(
            text = 'Text',
            on_press = self.click,
            background_color = [0, 1, 0, 1]
        )

    def click(self,i):
        print('Work')
        i.text = 'Test'

if __name__ == '__main__':
    MyApp().run()