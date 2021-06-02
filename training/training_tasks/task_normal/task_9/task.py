import datetime
now = datetime.datetime.now()

date = input('Date: ')

date = date.split('.')

date_true = True

num = int(date[1])

days_month = '28/29' if num == 2 else 30 if num in [4,6,9,11] else 31 if num in [1,3,5,7,8,10,12] else "Ошибка! Такого месяца нет."

if not(0 < int(date[0]) and int(date[0]) <= days_month):
    date_true = False

if not(int(date[2]) < now.year):
    date_true = False

print(date_true)