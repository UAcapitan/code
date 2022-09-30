
it: iter = iter([1,2,3,4,5,6,7])

print(next(it))
print(next(it))
print(next(it))

print()

print(it)

print()

with open("test.txt", "r") as file:
    while True:
        try:
            print(file.__next__()[:-1])
        except:
            break
