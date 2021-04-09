# Breadth First Search (BFS)

## How BFS Works
![BFS](assets/bfs.png)

## BFS Source Code
Template for BFS:
``` Python
def bfs(graph, start, end):
    # Queue to store nodes, we can also use deque. 
    queue = []
    queue.append(start)
    # For graph where nodes could connect to each other.
    visited = set()
    visited.add(start)

    while queue:
        node = queue.pop()
        # Add the current node to visited set.
        visited.add(node)

        process(node)
        # Generate child nodes for the current node.
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # other processing work
```