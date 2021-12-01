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
        self.now = datetime.datetime.now().strftime("%H")

        self.root.geometry("250x400")
        self.root.title("Weather app")

        self.text = tk.Label(self.root, text='-', font=("Arial", 25))
        self.text.place(x=120, y=150)

        self.day_av = tk.Label(self.root, text='Day average', font=("Arial", 10))
        self.day_av.place(x=88, y=200)

        self.main_city_text = self.open_main_city_in_json()

        self.input_text = tk.Text(self.root, height=1, width=10)
        self.input_text.insert(1.0, self.main_city_text)
        self.input_text.place(x=88, y=320)

        self.button_success = tk.Button(self.root, height=1, width=10, text='Show weather',
        command=self.show_temperature)
        self.button_success.place(x=90, y=350)

        if int(self.now) >= 12:
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
        self.extra_menu.add_command(label="Save weather", command=self.show_save_weather)
        self.settings_menu = tk.Menu(self.main_menu, tearoff=0)
        self.settings_menu.add_command(label="Main city", command=self.show_main_city)
        self.settings_menu.add_command(label="About program", command=self.show_about_program)
        self.main_menu.add_cascade(label="Extra", menu=self.extra_menu)
        self.main_menu.add_cascade(label="Settings", menu=self.settings_menu)
        self.main_menu.add_command(label='Exit', command=self.app_exit)

        self.city_name = tk.Label(text='---', font=("Arial", 15))
        self.city_name.place(x=115, y=10)

        if self.main_city_text != None:
            self.show_temperature()

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

            if int(self.now) >= 12:
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
        if self.w.will_have_hurricane():
            self.img = tk.PhotoImage(file="src/hurricane.png")
        elif self.w.will_have_storm():
            self.img = tk.PhotoImage(file="src/storm.png")
        elif self.w.will_have_tornado():
            self.img = tk.PhotoImage(file="src/tornado.png")
        elif self.w.will_have_fog():
            self.img = tk.PhotoImage(file="src/fog.png")
        elif self.w.will_have_rain():
            self.img = tk.PhotoImage(file="src/rain.png")
        elif self.w.will_have_snow():
            self.img = tk.PhotoImage(file="src/snow.png")
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
        self.btn_error = tk.Button(self.error_window, text='Exit', command=self.error_exit)

        self.label_error.pack()
        self.btn_error.pack()

    def error_exit(self):
        self.error_window.destroy()
        self.app_exit()

    def show_main_city(self):
        self.main_city = tk.Toplevel(self.root)
        self.main_city.geometry("200x70")
        self.main_city_entry = tk.Entry(self.main_city)
        self.main_city_entry.insert(0, self.main_city_text)
        self.main_city_btn = tk.Button(self.main_city, text="Save", command=self.save_main_city_in_json)

        self.main_city_entry.place(x=40, y=10)
        self.main_city_btn.place(x=83, y=40)
    
    def show_weather_days(self):
        self.weather_days = tk.Toplevel(self.root)
        self.weather_days.geometry("250x400")
        self.weather_days.title("List of weather")

        self.label_1 = tk.Label(self.weather_days, text='Date and time')
        self.label_2 = tk.Label(self.weather_days, text='°C')
        self.label_1.place(x=22, y=20)
        self.label_2.place(x=200, y=20)

        self.days_weather_list = tk.Listbox(self.weather_days, width=34, height=20)
        daily_forecast = self.w.forecast
        l = 1
        for weather in daily_forecast:
            text = weather.reference_time('iso')[0:16] + ' ' * 30 + str(weather.temperature(unit='celsius')['temp'])
            self.days_weather_list.insert(l, text)
            l += 1
        self.days_weather_list.place(x=20, y=40)
        self.days_weather_btn = tk.Button(self.weather_days, text='Exit', command=self.weather_days.destroy, width=7)
        self.days_weather_btn.place(x=170, y=370)

    def save_main_city_in_json(self):
        city = self.main_city_entry.get()
        with open('settings.json', 'w') as f:
            json.dump({'city':city}, f)

    def open_main_city_in_json(self):
        try:
            with open('settings.json', 'r') as f:
                main_city = json.load(f)['city']
        except:
            with open('settings.json', 'w') as f:
                json.dump({'city':''}, f)
            with open('settings.json', 'r') as f:
                main_city = json.load(f)['city']
        return main_city

    def show_about_program(self):
        self.about_program = tk.Toplevel(self.root)
        self.about_program.geometry("360x120")
        self.about_program.title("About program")

        self.label_about_program = tk.Label(self.about_program, text='\
The program is made to obtain\n weather data. \
The weather in the specified city is indicated\n for 1 or 2 days ahead. \
You can also get more specific\n information about the weather in the Days\n section. \
The developer of the program is EdMix.')
        self.label_about_program.place(x=20, y=20)

    def show_save_weather(self):
        self.save_weather = tk.Toplevel(self.root)
        self.save_weather.geometry("70x90")
        self.save_weather.title("Save weather")

        self.entry_save_weather = tk.Entry(self.save_weather, width=12)
        self.btn_save_weather = tk.Button(self.save_weather, text='Save weather', command=self.save_weather_in_file)

        self.entry_save_weather.place(x=20, y=20)
        self.btn_save_weather.place(x=20, y=50)

    def save_weather_in_file(self):
        try:
            name_file = self.entry_save_weather.get()
            l = [self.input_text.get("1.0",'end-1c') + '\n\n', 'Date and time   Temperature\n']
            daily_forecast = self.w.forecast
            for weather in daily_forecast:
                text = weather.reference_time('iso')[0:16] + ' ' * 3 + str(weather.temperature(unit='celsius')['temp']) + '\n'
                l.append(text)
            l[-1] = l[-1][0:-1]
            with open(name_file+'.txt', 'w') as f:
                f.writelines(l)
        except:
            self.show_error()
        self.save_weather.destroy()



if __name__ == '__main__':
    root = tk.Tk()

    owm = pyowm.OWM('ba5efb246df12da53dec4af7c4583ce7')
    mgr = owm.weather_manager()

    app = App(root, mgr)

    root.mainloop()