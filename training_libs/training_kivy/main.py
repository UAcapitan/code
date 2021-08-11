from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

n = 0

class MyApp(App):
    def build(self):

        f1 = FloatLayout(size=(300,300))
        global n
        f1.add_widget(Button(
            text = str(n),
            on_press = self.click,
            background_color = [0, 1, 0, 1]
        ))

        return f1

    def click(self,i):
        global n
        print('Work')
        n += 1
        i.text = str(n)

if __name__ == '__main__':
    MyApp().run()