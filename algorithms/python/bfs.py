import sys
import queue
sys.path.append("../../") # Relative path to the graph definition
from data_structures.python.graph import create_test_graph

def bfs(graph, s, t):
	if s == t: return None
	# Mark visited vertices.
	visited = []
	visited.append(s)

	# Vertices already visisted, but the connected vertices are still not visited.
	vertices_queue = queue.Queue()
	vertices_queue.put(s)

	while not vertices_queue.empty():
		curr = vertices_queue.get()
		for vertex in graph.adj[curr]:
			if vertex not in visited:
				visited.append(vertex)
				if vertex == t:
					return visited # TODO： print shortest path
				vertices_queue.put(vertex)

	# Visited path
	print("Visited path: {}".format(visited))

	# Make the program more Pythonic


if __name__ == "__main__":
    test_graph = create_test_graph()
    test_graph.show_graph()
    print(bfs(test_graph, 2, 5))