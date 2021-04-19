"""
Class definition for Union Find.

Reference: 

1. [Union-Find算法详解](https://labuladong.github.io/algo/%E7%AE%97%E6%B3%95
%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/UnionFind%E7%AE%97%E6%B3%95%E8%AF%A6%
E8%A7%A3.html)
"""

class UnionFind:
    def __init__(self, length: int):
        # Initialization - initialize the value to be its index.
        self.roots = [i for i in range(length)]
        # Rank - to measure the depth of each tree.       
        self.rank = [0] * length
        # Count for connected components
        self.count = length
    
    def find_root(self, node):
        """ Find the root node for the given node. 
        
        Time Complexity - Worst case O(N)
        """
        root = node
        # Find root node.
        while root != self.roots[root]:
            root = self.roots[root]
        
        # Optimization - path compression.
        # Change each node's parent to root node.
        while node != self.roots[node]:
            self.roots[node], node = root, self.roots[node]
        
        return root

    def connected(self, node1, node2):
        """ Check whether the two nodes are connected (have common root). 
        """
        return self.find_root(node1) == self.find_root(node2)

    def union(self, node1, node2):
        """ Merge two sets into one. """
        node1_root = self.find_root(node1)
        node2_root = self.find_root(node2)
        # self.roots[node2_root] = node1_root
        
        # Union by rank
        # Check whether the two nodes belong to the same root.
        if node1_root != node2_root:
            if self.rank[node1_root] > self.rank[node2_root]:
                self.roots[node2_root] = node1_root
            elif self.rank[node1_root] < self.rank[node2_root]:
                self.roots[node1_root] = node2_root
            else:
                self.roots[node2_root] = node1_root
                self.rank[node1_root] += 1
            # Reduce the count for connected components
            self.count -= 1


if __name__ == "__main__":
    union_find = UnionFind(5)
    union_find.union(2, 3)
    print(f"2 and 3 are connected: {union_find.connected(2, 3)}")
    print(f"2 and 4 are connected: {union_find.connected(2, 4)}")
    union_find.union(2, 4)
    print(f"2 and 4 are connected: {union_find.connected(2, 4)}")
    print(f"4's root node is: {union_find.find_root(4)}")
    print(f"Connected components: {union_find.count}")
    print(f"Current roots: {union_find.roots}")