
registry = set()

def register(active=True):
    def decorate(func):
        print("Running")
        if active:
            registry.add(func)
        else:
            registry.discard(func)
    
        return func
    
    return decorate


if __name__ == "__main__":
    @register()
    def test_1():
        return None

    print(registry)

    @register(active=True)
    def test_2():
        return None

    print(registry)

    @register(active=False)
    def test_3():
        return None

    print(registry)
