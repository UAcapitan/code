from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')


n = 0
GREEN_COLOR = [0,1,0,1]

class MyApp(App):
    def build(self):
        global n
        global GREEN_COLOR
        b1 = BoxLayout()
        b1.add_widget(Button(
            text = str(n),
            on_press = self.click,
            background_color = GREEN_COLOR,
            background_normal = '',
            size_hint = (.5,.25),
            pos = (100,200)
        ))
        b1.add_widget(Button(
            text = str(n),
            on_press = self.click,
            background_color = GREEN_COLOR,
            background_normal = '',
            size_hint = (.5,.25),
            pos = (100,200)
        ))

        return b1

    def click(self,i):
        global n
        n += 1
        i.text = str(n)

if __name__ == '__main__':
    MyApp().run()