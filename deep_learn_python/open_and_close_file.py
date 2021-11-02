fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()

with open('foo.txt', 'wb') as reader:
    print(reader.name)
    print(reader.closed)
    print(reader.mode)
