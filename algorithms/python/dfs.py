import sys
sys.path.append("../../") # Relative path to the graph definition
from data_structures.python.graph import create_test_graph

def dfs(graph, start, t):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph.adj[vertex] - visited)
    return visited
    
def recursive_dfs(graph, start, t):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph.adj[start] - visited:
        dfs(graph, next, visited)
    return visited


if __name__ == "__main__":
    test_graph = create_test_graph()
    test_graph.show_graph()
    print(dfs(test_graph, 2, 5))