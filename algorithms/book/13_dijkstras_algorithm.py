graph = {
	"a": {
		"b":7,
		"c":2
	},
	"b": {
		"a":7,
		"c":2,
		"f":3
	},
	"c": {
		"a":2,
		"b":2
	},
	"f": {
		"b":3
	}
}


def algorithm(graph, start, finish, type_return='distance'):
	list_ = [['', start, 0]]

	n = 0

	for i in list_:
		for j in graph[i[1]]:
			k = [k for k in list_ if (k[0] == i[1] and k[1] == j) or (k[0] == j and k[1] == i[1])]
			list_.append([i[1], j, i[2] + graph[i[1]][j]])
			if k:
				if k[0][2] >= i[2] + graph[i[1]][j]:
					list_.pop(list_.index(k[0]))
				else:
					list_.pop(-1)

	match type_return:
		case 'distance':
			return [i for i in list_ if i[1] == finish][0][2]
		case 'way':
			way = [[i for i in list_ if i[1] == finish][0][1]]
			while way[-1] != start:
				way.append(sorted([i for i in list_ if i[1] == way[-1]], key=lambda i: i[2])[0][0])
			return way
		case 'all':
			way = [[i for i in list_ if i[1] == finish][0][1]]
			while way[-1] != start:
				way.append(sorted([i for i in list_ if i[1] == way[-1]], key=lambda i: i[2])[0][0])
			return [way, [i for i in list_ if i[1] == finish][0][2]]

print(algorithm(graph, "a", "f", "distance"))
print(algorithm(graph, "a", "f", "way"))
print(algorithm(graph, "a", "f", "all"))