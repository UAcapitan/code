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

# decorator example 1-------------------------------------

def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a, b):
    return a + b

# print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

# decorators example 2 -----------------------------------

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

# cities("Nairobi", "Accra")

