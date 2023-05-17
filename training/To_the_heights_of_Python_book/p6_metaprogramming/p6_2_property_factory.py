
def quantity(storage_name):
    
    def gty_getter(instance):
        return instance.__dict__[storage_name]
    
    def gty_setter(instance, value):
        print("Working")
        print(type(value))
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError("Value must be > 0")
    
    return property(gty_getter, gty_setter)


class LineItem:
    weight = quantity("weight")
    price = quantity("price")
    print("Works")
    print(type(weight))

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

        print(type(weight))

    def subtotal(self):
        return self.weight * self.price
    

if __name__ == "__main__":
    LineItem("Item", 10, 3)