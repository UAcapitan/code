class User:
    def __init__(self, l, p):
        self.login = l
        self.password = p

    def login_user(self, l, p):
        if self.login == l and self.password == p:
            return True
        else:
            return False

    def show_user_info(self):
        if self.login_user(input('Login: '), input('Password: ')):
            print('User login: ' + self.login)
            print('User password: ' + self.password)
        else:
            print('Error')

user_1 = User('EdMix', 'edmix22')
user_1.show_user_info()