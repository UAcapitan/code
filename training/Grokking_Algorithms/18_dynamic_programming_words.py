words = ['test', 'rest']

def algorithm(words):
    word1, word2 = words
    cell = []
    for i in range(len(word1)):
        list_ = []
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                if i == 0 or j == 0:
                    list_.append(1)
                else:
                    list_.append(cell[-1][j-1] + 1)
            else:
                list_.append(0)
        cell.append(list_)

    result = []
    for i in cell:
        result += i

    return cell, max(result)

if __name__ == "__main__":
    table, max_ = algorithm(words)
    print(table)
    print(max_)