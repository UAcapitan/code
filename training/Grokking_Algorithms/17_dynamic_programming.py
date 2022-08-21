items = {
    "guitar": [1500, 1],
    "music-player": [3000, 4],
    "laptop": [2000, 3],
}

size = 4

def algorithm(items, size):
    cell = []
    for item, data in items.items():
        list_ = []
        for i in range(1, size + 1):
            if data[1] <= i:
                n = i - data[1]
                if n > 0 and len(cell) > 0:
                    list_.append(data[0] + cell[-1][n-1])
                else:
                    list_.append(data[0])
            else:
                list_.append(cell[-1][i-1])
        cell.append(list_)

    return cell[-1][-1]

if __name__ == "__main__":
    print(algorithm(items, size))