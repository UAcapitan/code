
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

if __name__ == "__main__":
    shoes = {"price": 14900}
    print(apply_discount(shoes, 0.25))

    print(apply_discount(shoes, 2.0))
