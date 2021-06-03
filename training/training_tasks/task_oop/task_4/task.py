import abc

class StandartUser(abc.ABC):
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

class System:
    def __init__(self):
        self.__users = []
        self.__admins = []
    
    def setAdmin(self, obj):
        self.__admins.append(obj)
    
    def getAdmins(self):
        return self.__admins
    
    def setUser(self, obj):
        self.__users.append(obj)
    
    def getUsers(self):
        return self.__users

system = System()

system.setAdmin(Admin('Ivan'))
system.setUser(User('Pasha'))

print(system.getAdmins()[0].username + ' - ' + system.getAdmins()[0].role)
print(system.getUsers()[0].username + ' - ' + system.getUsers()[0].role)

try:
    print(system.__admins[0].username + ' - ' + system.__admins()[0].role)
except:
    print('Error')

try:
    print(system.__users[0].username + ' - ' + system.__users()[0].role)
except:
    print('Error')