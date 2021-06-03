import abc

class StandartUser(abc.ABC):
    def __init__(self, name):
        self.username = name

class Admin(StandartUser):
    def __init__(self, name):
        super().__init__(name)
        self.role = 'Admin'
    
    def __str__(self):
        return 'Admin - ' + self.username

class User(StandartUser):
    def __init__(self, name):
        super().__init__(name)
        self.role = 'User'
    
    def __str__(self):
        return 'User - ' + self.username

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

    def __str__(self):
        return 'System - ' + str(len(self.__users)) + ' Users - ' + str(len(self.__admins)) + ' Admins'

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

print(system)
print(system.getAdmins()[0])
print(system.getUsers()[0])