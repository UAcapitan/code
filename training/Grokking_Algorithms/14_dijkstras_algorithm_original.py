graph = {
    "start": {
        "a":6,
        "b":2        
    },
    "a": {
        "fin":1
    },
    "b": {
        "a":3,
        "fin":5
    },
    "fin": {

    }
}

def algorithm(graph, start):
    infinity = float("inf")
    costs = {
        i:infinity for i in graph.keys() if i != start
    }
    for i in graph[start].keys():
        costs[i] = graph[start][i]

    parents = {
        i:None for i in graph.keys() if i != start
    }

    for i in graph[start].keys():
        parents[i] = start

    processed = []

    return

if __name__ == "__main__":
    print(algorithm(graph, "start"))