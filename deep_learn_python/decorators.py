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

# user = User('Max')
# print(user.name)
# user.name = 'Maxim'
# del user.name

# decorator ----------------------------------------------

def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a, b):
    return a + b

# print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

