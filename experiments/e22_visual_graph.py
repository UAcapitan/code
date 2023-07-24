
import networkx
import matplotlib.pyplot as plt


graph = networkx.Graph()
graph.add_nodes_from([1,2,3,4,5,6,7])
graph.add_edge(1,2)
graph.add_edge(1,7)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(4,5)
graph.add_edge(5,7)
graph.add_edge(6,7)

if __name__ == "__main__":
    networkx.draw(graph)
    plt.show()
