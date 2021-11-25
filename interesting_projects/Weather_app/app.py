import tkinter as tk
import pyowm

class App():
    def __init__(self, root, mgr):
        self.root = root
        self.mgr = mgr

        self.root.geometry("250x400")

        self.text = tk.Label(self.root, text='-', font=("Arial", 25))
        self.text.place(x=120, y=150)

        self.day_av = tk.Label(self.root, text='Day average', font=("Arial", 10))
        self.day_av.place(x=90, y=200)

        self.input_text = tk.Text(self.root, height=1, width=10)
        self.input_text.place(x=88, y=320)

        self.button_success = tk.Button(self.root, height=1, width=10, text='Show weather',
        command=self.show_temperature)
        self.button_success.place(x=90, y=350)

        self.day = tk.Label(self.root, text='-', font=("Arial", 15))
        self.day.place(x=185, y=240)

        self.night = tk.Label(self.root, text='-', font=("Arial", 15))
        self.night.place(x=50, y=240)

        self.day_text = tk.Label(self.root, text='Day', font=("Arial", 10))
        self.day_text.place(x=175, y=270)

        self.night_text = tk.Label(self.root, text='Night', font=("Arial", 10))
        self.night_text.place(x=40, y=270)

    def show_temperature(self):
        daily_forecast = self.mgr.forecast_at_place(self.input_text.get("1.0",'end-1c'), '3h').forecast
        t_3h = 0
        l = 0
        for weather in daily_forecast:
            print(weather.reference_time('iso'), weather.temperature(unit='celsius')['temp'])
            t_3h += weather.temperature(unit='celsius')['temp']
            l += 1

        self.text.place(x=90, y=150)
        self.text['text'] = str(round(t_3h/l)) + ' °C'

        t_3h = 0
        l = 0

        for weather in daily_forecast:
            t_3h += weather.temperature(unit='celsius')['temp']
            l += 1
            if l == 3:
                break

        self.night.place(x=35, y=240)
        self.night['text'] = str(round(t_3h/l)) + ' °C'
        
        t_3h = 0
        l = 0

        for weather in daily_forecast:
            l += 1
            if l > 3:
                t_3h += weather.temperature(unit='celsius')['temp']

        self.day.place(x=165, y=240)
        self.day['text'] = str(round(t_3h/l)) + ' °C'


if __name__ == '__main__':
    root = tk.Tk()

    owm = pyowm.OWM('ba5efb246df12da53dec4af7c4583ce7')
    mgr = owm.weather_manager()

    app = App(root, mgr)

    root.mainloop()