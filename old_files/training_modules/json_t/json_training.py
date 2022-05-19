import json

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs'

with open(filename,'w') as f:
    json.dump(dogs_dict,f)

with open(filename,'r') as f:
    new_dict = json.load(f)

print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))