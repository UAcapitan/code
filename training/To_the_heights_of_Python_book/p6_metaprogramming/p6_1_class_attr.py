class Class:
    data = "some text"

    @property
    def prop(self):
        return "some another text"
    
obj = Class()

print(vars(obj))
print(obj.data)
obj.data = "bar"
print(vars(obj))
print(obj.data)

print(Class.data)
print(Class.prop)
print(obj.prop)

try:
    obj.prop = "foo"
except Exception as e:
    print(e)

print(obj.prop)

obj.__dict__["prop"] = "foo"

print(vars(obj))

Class.prop = "baz"
print(obj.prop)

print(obj.data)
print(Class.data)

Class.data = "new"

print(obj.data)
print(Class.data)

del Class.data

print(obj.data)

try:
    print(Class.data)
except Exception as e:
    print(e)
