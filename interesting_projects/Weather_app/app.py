import tkinter as tk
import pyowm
import datetime
import sys
import json

class App():
    def __init__(self, root, mgr):
        self.root = root
        self.mgr = mgr
        self.dt = datetime.datetime.today()

        self.root.geometry("250x400")
        self.root.title("Weather app")

        self.text = tk.Label(self.root, text='-', font=("Arial", 25))
        self.text.place(x=120, y=150)

        self.day_av = tk.Label(self.root, text='Day average', font=("Arial", 10))
        self.day_av.place(x=88, y=200)

        self.input_text = tk.Text(self.root, height=1, width=10)
        self.input_text.place(x=88, y=320)

        self.button_success = tk.Button(self.root, height=1, width=10, text='Show weather',
        command=self.show_temperature)
        self.button_success.place(x=90, y=350)

        self.day = tk.Label(self.root, text='-', font=("Arial", 15))
        self.day.place(x=185, y=240)

        self.night = tk.Label(self.root, text='-', font=("Arial", 15))
        self.night.place(x=50, y=240)

        self.day_text = tk.Label(self.root, text='Next day', font=("Arial", 10))
        self.day_text.place(x=162, y=270)

        self.night_text = tk.Label(self.root, text='Next night', font=("Arial", 10))
        self.night_text.place(x=26, y=270)

        self.canvas = tk.Canvas(root, width=64, height=64)  
        self.canvas.place(x=93, y=50)    

        self.main_menu = tk.Menu(root) 
        self.root.config(menu=self.main_menu)
        self.extra_menu = tk.Menu(self.main_menu, tearoff=0)
        self.extra_menu.add_command(label="Days", command=self.show_weather_days)
        self.settings_menu = tk.Menu(self.main_menu, tearoff=0)
        self.settings_menu.add_command(label="Main city", command=self.show_main_city)
        self.main_menu.add_cascade(label="Extra", menu=self.extra_menu)
        self.main_menu.add_cascade(label="Settings", menu=self.settings_menu)
        self.main_menu.add_command(label='Exit', command=self.app_exit)

        self.city_name = tk.Label(text='---', font=("Arial", 15))
        self.city_name.place(x=115, y=10)

    def show_temperature(self):
        try:
            self.set_city()
            self.w = self.mgr.forecast_at_place(self.input_text.get("1.0",'end-1c'), '3h')
            daily_forecast = self.w.forecast
            t_3h = 0
            l = 0
            for weather in daily_forecast:
                if int(weather.reference_time('iso')[8:10]) == self.dt.day:
                    t_3h += weather.temperature(unit='celsius')['temp']
                    l += 1

            try:
                self.text.place(x=90, y=150)
                self.text['text'] = str(round(t_3h/l)) + ' °C'
            except:
                self.text['text'] = '-'

            t_3h = 0
            l = 0

            for weather in daily_forecast:
                if int(weather.reference_time('iso')[8:10]) == self.dt.day + 1:
                    if 0 <= int(weather.reference_time('iso')[11:13]) <= 6:
                        t_3h += weather.temperature(unit='celsius')['temp']
                        l += 1

            self.night.place(x=35, y=240)
            self.night['text'] = str(round(t_3h/l)) + ' °C'
            
            t_3h = 0
            l = 0

            for weather in daily_forecast:
                if int(weather.reference_time('iso')[8:10]) == self.dt.day + 1:
                    if 12 <= int(weather.reference_time('iso')[11:13]) <= 18:
                        t_3h += weather.temperature(unit='celsius')['temp']
                        l += 1

            self.day.place(x=165, y=240)
            self.day['text'] = str(round(t_3h/l)) + ' °C'

            self.set_image_weather()
        except:
            self.show_error()

    def set_image_weather(self):
        if self.w.will_have_snow():
            self.img = tk.PhotoImage(file="src/snow.png")
        elif self.w.will_have_hurricane():
            self.img = tk.PhotoImage(file="src/hurricane.png")
        elif self.w.will_have_storm():
            self.img = tk.PhotoImage(file="src/storm.png")
        elif self.w.will_have_tornado():
            self.img = tk.PhotoImage(file="src/tornado.png")
        elif self.w.will_have_fog():
            self.img = tk.PhotoImage(file="src/fog.png")
        elif self.w.will_have_rain():
            self.img = tk.PhotoImage(file="src/rain.png")
        elif self.w.will_have_clouds():
            self.img = tk.PhotoImage(file="src/clouds.png")
        elif self.w.will_have_clear():
            self.img = tk.PhotoImage(file="src/sun.png")


        self.canvas.create_image(0,0, anchor=tk.NW, image=self.img)

    def set_city(self):
        self.city_name['text'] = self.input_text.get("1.0",'end-1c')
        self.city_name.place(x=110-len(self.city_name['text'])*3, y=10)

    def app_exit(self):
        sys.exit()

    def show_error(self):
        self.error_window = tk.Toplevel(self.root)
        self.label_error = tk.Label(self.error_window, text = "Error")

        self.label_error.pack()

    def show_main_city(self):
        self.main_city = tk.Toplevel(self.root)
        self.main_city.geometry("200x70")
        self.main_city_entry = tk.Entry(self.main_city)
        self.main_city_btn = tk.Button(self.main_city, text="Save")

        self.main_city_entry.place(x=40, y=10)
        self.main_city_btn.place(x=83, y=40)
    
    def show_weather_days(self):
        self.weather_days = tk.Toplevel(self.root)
        self.weather_days.geometry("250x400")
        self.weather_days.title("List of weather")


if __name__ == '__main__':
    root = tk.Tk()

    owm = pyowm.OWM('ba5efb246df12da53dec4af7c4583ce7')
    mgr = owm.weather_manager()

    app = App(root, mgr)

    root.mainloop()