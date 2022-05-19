import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs'

with open(filename,'wb') as f:
    pickle.dump(dogs_dict,f)

with open(filename,'rb') as f:
    new_dict = pickle.load(f)

print(new_dict)
print(new_dict==dogs_dict)
print(type(new_dict))