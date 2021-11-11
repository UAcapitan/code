class Car:
    model = 'BMW'
    engine = 1.6

    def drive(self):
        print("Let's go")
    
    def stop(self):
        print('Stop')

a1 = Car()
getattr(a1, 'drive')()
a1.stop()