import calendar

month = calendar.month(2021,11)
print(month)

year = calendar.calendar(2021)
print(year)

html_year = calendar.HTMLCalendar(0).formatyear(2021)
with open('calendar.html', 'w') as f:
    f.write(html_year)
print(html_year)