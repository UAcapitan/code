# Orange color - 1
# Green color - 10
# Little size - 1
# Big size - 10

# [name, color, size]
fruits = [
    ['tangerine', 2, 2],
    ['tangerine', 1, 1],
    ['tangerine', 1, 3],
    ['tangerine', 3, 3],
    ['tangerine', 4, 2],
    ['tangerine', 2, 5],
    ['tangerine', 5, 2],

    ['apple', 6, 10],
    ['apple', 7, 9],
    ['apple', 9, 5],
    ['apple', 10, 7],
    ['apple', 8, 9],
    ['apple', 5, 7],
    ['apple', 7, 5],
]

data = ['unknown', 3, 2]

def algorithm(fruits, data):
    # Data in all: [distance, index of element]
    all = []
    for i in fruits:
        all.append([((data[1]-i[1])**2 + (data[2]-i[2])**2)**0.5, len(all)])

    nearest = sorted(all, key=lambda x: x[0])

    names = []

    for i in nearest[:int(len(fruits)**0.5)]:
        names.append(fruits[i[1]][0])

    data[0] = max(set(names), key=names.count)

    return data

if __name__ == "__main__":
    print(algorithm(fruits, data))