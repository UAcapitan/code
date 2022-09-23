
symbols = "$%*#&^!"

codes1 = []
for symbol in symbols:
    codes1.append(ord(symbol))

codes2 = [ord(symbol) for symbol in symbols]

codes3 = (ord(symbol) for symbol in symbols)

print(codes1 == codes2)
print(codes2 == codes3)

for i in codes3:
    # print(i)
    pass

# Iterator vs generator
colors = ['white', 'black']
sizes = ['S', 'M', "L"]

t_shirts = [(color, size) for color in colors for size in sizes]
t_shirts_gen = ((color, size) for color in colors for size in sizes)

print(t_shirts)

for t_shirt in t_shirts_gen:
    print(t_shirt)
