from kivy.app import App
from kivy.uix.button import Button

n = 0

class MyApp(App):
    def build(self):
        global n
        return Button(
            text = str(n),
            on_press = self.click,
            background_color = [0, 1, 0, 1]
        )

    def click(self,i):
        global n
        print('Work')
        n += 1
        i.text = str(n)

if __name__ == '__main__':
    MyApp().run()