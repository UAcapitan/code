# Experiment was successful

training = [
    [[5,10,5,5], 5],
    [[10,10,10,10], 10],
    [[10,5,5,5], 5],
    [[10,5,10,10], 10],
    [[10,5,5,10], 10],
    [[10,10,5,10], 10],
    [[5,5,5,5], 5]
]

data1 = [5,10,10,10]
data2 = [5,10,5,5]

def algorithm(training, data):
    all = []

    for i in training:
        n = 0
        for j in range(len(i[0])):
            n += (data[j] - i[0][j]) ** 2
        all.append([n**0.5, len(all)])

    nearest = sorted(all, key=lambda x: x[0])[:3]
    results = [training[i[1]][1] for i in nearest]

    return max(set(results), key=results.count)

if __name__ == "__main__":
    print(algorithm(training, data1))
    print(algorithm(training, data2))