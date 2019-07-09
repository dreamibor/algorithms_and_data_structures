class Graph():
    """ Graph stored using adjacent list. """
    def __init__(self, v):
        if v <= 1: raise ValueError("Graph has wrong number of vertices!")
        self.v = v # Number of vertices
        self.adj = [[] for i in range(self.v)]

    def add_edge(self, start, terminal):
        # Undirected graphs's edge will be saved twice
        self.adj[start].append(terminal)
        self.adj[terminal].append(start)

    def show_graph(self):
        # TODO: A better function to visualise graphs in text
        print("Vertex - Connected Vertices")
        for i in range(self.v):
            print("{:6d} - {}".format(i, self.adj[i]))

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

# TODO: Adjacent Matrix

