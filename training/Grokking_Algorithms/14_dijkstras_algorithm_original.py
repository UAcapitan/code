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
    # Costs
    infinity = float("inf")
    costs = {
        i:infinity for i in graph.keys() if i != start
    }
    for i in graph[start].keys():
        costs[i] = graph[start][i]

    # Parents
    parents = {
        i:None for i in graph.keys() if i != start
    }
    for i in graph[start].keys():
        parents[i] = start

    # Processed
    processed = []

    # Main part of algorithm

    def find_lowest(costs):
        lowest_costs = float("inf")
        lowest_costs_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_costs and node not in processed:
                lowest_cost = cost
                lowest_costs_node = node
            return lowest_costs_node

    node = find_lowest(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest(costs)

    return costs, parents

if __name__ == "__main__":
    for i in algorithm(graph, "start"):
        print(i)