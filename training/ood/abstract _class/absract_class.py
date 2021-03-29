from abc import ABC, abstractclassmethod

# pylint: disable=no-member
class Phone(ABC):
    """Absract class for create phone class"""

    def make_photo(self):
        """Method for make photo. Method not work if phone haven`t camera"""
        if self.camera and len(self.photo) > 0:
            photo = self.photo[-1][:-1] + str(int(self.photo[-1][-1]) + 1)
            print(f'Make {photo}')
            self.photo.append(photo)
        elif self.camera and len(self.photo) == 0:
            self.photo.append('image_1')
            print('Make image_1')
        else:
            print('Your phone no have camera')

    def browser_go_in_site(self, url):
        '''Method for browsing'''
        site = post(url)
        if site.status_code == 200:
            print(site)
            self.browser_history.append(url)
        else:
            print('Sorry')

    def browser_open_history(self):
        '''Open history in phone browser'''
        print('-----------------\nBrowser history')
        if len(self.browser_history) > 0:
            for site in self.browser_history:
                print(site)
        else:
            print('No history')

        print('-----------------')
        input()

    def photos_open_list(self):
        '''Open list photos in phone'''
        print('-----------------\nPhotos list')
        if len(self.photo) > 0:
            for photo in self.photo:
                print(photo)
        else:
            print('No photos')

        print('-----------------')
        input()

    def create_user_account(self, name='', login='', password=''):
        if name != '' and login != '' and len(str(password)) >= 8:
            self.name = name
            self.login = login
            self.password = password
            print('\nAccount created')
        else:
            print('\nAccount not created')
        
        if len(str(password)) < 8:
            print('\nYou password little')

    def open_user_profile(self):
        if self.name != '':
            print(f'\nName: {self.name}')
            print(f'Login: {self.login}')
        else:
            print('\nYou don`t have account')

class Xphone(Phone):

    def __init__(self, camera):
        self.camera = camera
        self.photo = []
        self.browser_history = []
        self.name = ''

if __name__ == '__main__':
    xphone_1 = Xphone(camera=True)
    while True:
        print('\n1. Make photo\n2. Open photos\n3. Open site\n4. Open browser history\n5. Create account')
        print('6. Open user profile\n7. Password')
        command = input()
        if command == '1':
            xphone_1.make_photo()
        elif command == '2':
            xphone_1.photos_open_list()
        elif command == '3':
            xphone_1.browser_go_in_site(input('URL: '))
        elif command == '4':
            xphone_1.browser_open_history()
        elif command == '5':
            xphone_1.create_user_account(name=input('Name: '), login=input('Login: '), password=int(input('Password: ')))
        elif command == '6':
            xphone_1.open_user_profile()
        elif command == '7':
            print(f'Password: {xphone_1.password}')

        elif command == 'exit':
            break