import tkinter as tk
import pyowm

root = tk.Tk()
owm = pyowm.OWM('ba5efb246df12da53dec4af7c4583ce7')
mgr = owm.weather_manager()
daily_forecast = mgr.forecast_at_place('Florida', '3h').forecast
t_3h = 0
l = 0
for weather in daily_forecast:
    # print(weather.reference_time('iso'), weather.temperature(unit='celsius')['temp'])
    t_3h += weather.temperature(unit='celsius')['temp']
    l += 1

t = t_3h / l
print(t)

root.mainloop()