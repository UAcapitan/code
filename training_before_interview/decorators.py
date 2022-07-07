def test(f):
    def wrapTest():
        print('This is work')
        f()
        print("This is end")
    return wrapTest

@test
def new_test():
    print('I am working')