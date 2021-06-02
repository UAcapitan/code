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

class System:
    def __init__(self):
        self.users = []
        self.admins = []
    
    def setAdmin(self, obj):
        self.admins.append(obj)
    
    def getAdmins(self):
        return self.admins
    
    def setUser(self, obj):
        self.users.append(obj)
    
    def getUsers(self):
        return self.users

system = System()

system.setAdmin(Admin('Ivan'))
print(system.getAdmins()[0].username + ' - ' + system.getAdmins()[0].role)
system.setUser(User('Pasha'))
print(system.getUsers()[0].username + ' - ' + system.getUsers()[0].role)