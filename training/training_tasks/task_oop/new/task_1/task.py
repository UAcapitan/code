class StandartUser:
    def __init__(self, name):
        self.username = name

class Admin(StandartUser):
    def __init__(self, name):
        super().__init__(name)
        self.role = 'Admin'

class User(StandartUser):
    def __init__(self, name):
        super().__init__(name)
        self.role = 'User'

admin = Admin('Ivan')
user = User('Pasha')

print(admin.username + ' - ' + admin.role)
print(user.username + ' - ' + user.role)