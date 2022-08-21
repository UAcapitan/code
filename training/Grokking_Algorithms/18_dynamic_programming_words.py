# words = ['test', 'rest']
words = ['tttpppaaa', 'tctpppnaa']

def algorithm(words):
    word1, word2 = words
    cell = []
    for i in range(len(word1)):
        list_ = []
        for j in range(len(word2)):
            if word1[i] == word2[j]:
                if i == 0:
                    list_.append(1)
                else:
                    list_.append(cell[-1][i-1] + 1)
            else:
                if i == 0 or len(list_) == 0:
                    list_.append(0)
                else:
                    list_.append(list_[-1])
        cell.append(list_)


    return cell[-1][-1]

if __name__ == "__main__":
    print(algorithm(words))