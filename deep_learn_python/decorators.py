# getter, setter, deleter --------------------------------

class User():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Get name')
        return self._name

    @name.setter
    def name(self, value):
        print('Set name')
        self._name = value

    @name.deleter
    def name(self):
        print('Delete name')
        del self._name

user = User('Max')
print(user.name)
user.name = 'Maxim'
del user.name

