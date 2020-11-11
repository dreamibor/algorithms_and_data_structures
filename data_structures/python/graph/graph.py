from collections import defaultdict


class Graph():
    """ Graph stored using adjacent list. """
    def __init__(self, v):
        if v <= 1: raise ValueError("Graph has wrong number of vertices!")
        self.v = v # Number of vertices
        self.adj = defaultdict(set)

    def add_edge(self, start, terminal):
        # Undirected graphs's edge will be saved twice
        self.adj[start].add(terminal)
        self.adj[terminal].add(start)

    def show_graph(self):
        # TODO: A better function to visualise graphs in text
        print("Vertex - Connected Vertices")
        for k, v in self.adj.items():
            print("{:6d} - {}".format(k, v))


def create_test_graph():
    graph = Graph(8)
    graph.add_edge(0,1)
    graph.add_edge(0,3)
    graph.add_edge(1,2)
    graph.add_edge(1,4)
    graph.add_edge(2,5)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(4,6)
    graph.add_edge(5,7)
    graph.add_edge(6,7)
    return graph

if __name__ == "__main__":
    graph = create_test_graph()
    graph.show_graph()


# TODO: Adjacent Matrix

