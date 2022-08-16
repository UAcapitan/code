from datetime import date, datetime

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

graph_hard = {
	"a": {
		"b":2,
		"c":4
	},
	"b": {
		"a":2,
		"m":4,
		"c":3,
		"d":7
	},
	"c": {
		"a":4,
		"b":3,
		"k":4
	},
	"d": {
		"b":7,
		"k":1,
		"t":7
	},
	"k": {
		"c":4,
		"d":1,
		"l":8
	},
	"l": {
		"k":8,
		"t":9
	},
	"m": {
		"b":4,
		"t":7,
		"n":1
	},
	"n": {
		"m":1,
		"f":15
	},
	"f": {
		"n":15,
		"t":3
	},
	"t": {
		"d":7,
		"m":7,
		"l":9,
		"f":3
	}
}

# Timer decorator for rate of speed of algorithm
def timer(func):
	def wrap(*args):
		t1 = datetime.now()
		func(*args)
		print(datetime.now() - t1)
	return wrap

# My try to make Dijkstra's algorithm
@timer
def algorithm(graph, start, finish, type_return='distance'):
	list_ = [['', start, 0]]

	for i in list_:
		for j in graph[i[1]]:
			# k = list(filter(lambda k: (k[0] == i[1] and k[1] == j) or (k[0] == j and k[1] == i[1]), list_))
			k = []
			for k1 in list_:
				if (k1[0] == i[1] and k1[1] == j) or (k1[0] == j and k1[1] == i[1]):
					k.append(k1)
					break
			# k = [k for k in list_ if (k[0] == i[1] and k[1] == j) or (k[0] == j and k[1] == i[1])]
			list_.append([i[1], j, i[2] + graph[i[1]][j]])
			if k:
				if k[0][2] >= i[2] + graph[i[1]][j]:
					list_.pop(list_.index(k[0]))
				else:
					list_.pop(-1)

	match type_return:
		case 'distance':
			return sorted([i for i in list_ if i[1] == finish], key=lambda i: i[2])[0][2]
		case 'way':
			way = [[i for i in list_ if i[1] == finish][0][1]]
			while way[-1] != start:
				way.append(sorted([i for i in list_ if i[1] == way[-1]], key=lambda i: i[2])[0][0])
			return list(reversed(way))
		case 'all':
			way = [[i for i in list_ if i[1] == finish][0][1]]
			while way[-1] != start:
				way.append(sorted([i for i in list_ if i[1] == way[-1]], key=lambda i: i[2])[0][0])
			return [list(reversed(way)), sorted([i for i in list_ if i[1] == finish], key=lambda i: i[2])[0][2]]

# Dijkstra's algorithm from web
@timer
def algorithm_from_web(graph, start, finish):
	nodes = graph.keys()
	distances = graph

	unvisited = {node: None for node in nodes}
	visited = {}
	current = start
	currentDistance = 0
	unvisited[current] = currentDistance

	while True:
		for neighbour, distance in distances[current].items():
			if neighbour not in unvisited: continue
			newDistance = currentDistance + distance
			if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
				unvisited[neighbour] = newDistance
		visited[current] = currentDistance
		del unvisited[current]
		if not unvisited: break
		candidates = [node for node in unvisited.items() if node[1]]
		current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

	return visited[finish]

# algorithm(graph, "a", "f", "distance")

algorithm(graph_hard, "a", "f", "distance")

# algorithm_from_web(graph, "a", "f")

algorithm_from_web(graph_hard, "a", "f")