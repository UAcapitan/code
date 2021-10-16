fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

my_list = [i for i in range(1,11)]
print(my_list)

m2 = [i*j for i in range(1, 11) for j in range(10, 110, 10)]
print(m2)

test = [155,703,38,581,2,4,389,3593,5793,579,5748,58385,748,57993,759,5784,57908]
m3 = [i for i in test if i < 100]
print(m3)

test = ['Kiev', 'Moscow', 'Lviv']
cities = [i.lower() for i in test]
print(cities)

cities = [i for i in cities if len(i) < 5]
print(cities)

shop = ['Fruit','Fruit','Fruit','Fruit','Water', 'Fruit', 'Vegetable', 'Fruit', 'Fruit']
fruits = [i if i == 'Fruit' else 'Not fruit' for i in shop]
print(fruits)