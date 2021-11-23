import tkinter as tk
import pyowm

class App():
    def __init__(self, root, mgr):
        self.root = root
        self.mgr = mgr

        self.root.geometry("250x400")

        self.text = tk.Label(self.root, text='-', font=("Arial", 25))
        self.text.place(x=120, y=150)

        self.input_text = tk.Text(self.root, height=1, width=10)
        self.input_text.place(x=88, y=320)

        self.button_success = tk.Button(self.root, height=1, width=10, text='Show weather')
        self.button_success.place(x=90, y=350)

    def show_temperature(self):
        daily_forecast = self.mgr.forecast_at_place('Kiev', '3h').forecast
        t_3h = 0
        l = 0
        for weather in daily_forecast:
            # print(weather.reference_time('iso'), weather.temperature(unit='celsius')['temp'])
            t_3h += weather.temperature(unit='celsius')['temp']
            l += 1

        return t_3h / l


if __name__ == '__main__':
    root = tk.Tk()

    owm = pyowm.OWM('ba5efb246df12da53dec4af7c4583ce7')
    mgr = owm.weather_manager()

    app = App(root, mgr)

    root.mainloop()