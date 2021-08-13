from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')


n = 0
GREEN_COLOR = [0,1,0,1]

class MyApp(App):
    def build(self):
        global n
        global GREEN_COLOR
        f1 = FloatLayout(size=(300,300))
        f1.add_widget(Button(
            text = str(n),
            on_press = self.click,
            background_color = GREEN_COLOR
        ))

        return f1

    def click(self,i):
        global n
        n += 1
        i.text = str(n)

if __name__ == '__main__':
    MyApp().run()