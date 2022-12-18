
colors = ['white', 'black']
sizes = ['S', 'M', "L"]

t_shirts = [(color, size) for color in colors for size in sizes]
t_shirts_gen = ((color, size) for color in colors for size in sizes)

print(t_shirts)
for t_shirt in t_shirts_gen:
    print(t_shirt)
