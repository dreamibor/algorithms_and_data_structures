"""
DFS / BFS / Union Find - Number of Islands (medium)

Description:
Given an m x n 2d grid map of '1's (land) and '0's (water), return the 
number of islands.

An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of the 
grid are all surrounded by water.

Example:
Input: 
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

LeetCode Link: https://leetcode-cn.com/problems/number-of-islands/
"""


def num_of_islands_flood_fill(grid: list) -> int:
    """ Flood Fill

    Iterate all nodes, if the node is land (node == 1), we increase 
    the count of lands by 1, and then colorize its land neighbours 
    recursively (set all land nodes around it to 0).

    To colorize its neighbours recursively, we can use DFS and BFS.

    DFS:
    Recursively mark the current node as 0, and drill down to its 
    neighbour nodes whose value is 1.

    BFS:
    Add the current node's neighbours (value == 1) into a queue, and 
    keep adding the neighbours' neighbours into the quque.

    Time Complexity - O(M*N) - M and N are the number of rows and 
    columns of the grid.
    Space Complexity - O(M*N) - The worst case, all are 1s (lands).
    """
    # Edge cases - empty row or column.
    if not grid or not grid[0]: return 0

    # Define four moving directions, right, left, down, up,
    moving_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, columns = len(grid), len(grid[0])
    # Track visited nodes.
    visited = set()

    def _is_valid(row, col):
        """ Check whether (row, col) is valid. """
        # Index out of range
        if row < 0 or row >= rows or col < 0 or col >= columns:
            return False
        # If the element is 0 or the element has been visited.
        if grid[row][col] == '0' or (row, col) in visited:
            return False
        
        return True

    def flood_fill_dfs(row, col):
        """ Flood Fill with DFS
        
        Whence find a node with value 1, flood all it's neighbours,
        colorizing all 1s to be 0, or here add them into the visited 
        cell, so it will be invalid next time.
        """
        # Recursion termination
        if not _is_valid(row, col):
            return 0
        
        # Add the node to visited, equivalent to colorizing the node 
        # to 0.
        visited.add((row, col))

        for x, y in moving_directions:
            # Flood it's surrounding nodes.
            flood_fill_dfs(row + x, col + y)
        
        return 1

    def flood_fill_bfs(row, col):
        """ Flood Fill with BFS

        Space Complexity - O(min(M, N)) - for the queue.
        """
        # Check whether the current node is valid
        if not _is_valid(row, col):
            return 0

        # BFS - queue, add the first node into the queue.
        queue = [(row, col)]
        visited.add((row, col))

        while queue:
            cur_row, cur_col = queue.pop(0)
            # Explore the four directions, add them into the queue 
            # if valid.
            for dx, dy in moving_directions:
                new_row, new_col = cur_row + dx, cur_col + dy

                if _is_valid(new_row, new_col):
                    # Add to visited, so it's not valid next time.
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
        
        return 1

    # One line counting. 
    # count = sum([flood_fill_dfs(i, j) 
    #           for i in range(rows) \
    #           for j in range(columns)])
    
    count = 0
    for i in range(rows):
        for j in range(columns):
            # count += flood_fill_dfs(i, j)
            count += flood_fill_bfs(i, j)
    
    return count

#########################################################################
#                          Union Find for Grid                          #
#########################################################################
class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        # 1D array for the root nodes.
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        # Count of connected components
        self.count = 0

        # Initialization
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
    
    def find(self, i):
        """ Recursively find the root node. """
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        # Union by rank.
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            # Update the connected components' count.
            self.count -= 1

def num_of_islands_union_find(grid: list) -> int:
    """ Union Find

    Merge all nodes with 1 to their corresonding root, and count the 
    connected components in the graph / grid. 

    1. Initialization
    For all nodes that are 1, assign it's parent to itself. So the 
    number of total connected components equals to the number of 1s.

    2. Iterate all nodes, if the value is 1, merge it with adjacent 
    nodes. So that the numebr of connected components will reduce.

    Time Complexity - O(M * N * α(MN)) - M and N are the number of rows
    and columns. When we optimize the union find with path compression 
    and union by rank, the single operation's time complexity is α(MN), 
    where α(x) is inverse Ackermann function. When x is in the range of 
    human being's observable range (3.28×10^80), the value shall be 
    less than 5, so we can take it as constant. 
    Space Complexity - O(M * N) - For the union find array.
    """
    # Edge cases
    if not grid or not grid[0]: return 0

    union_find = UnionFind(grid)
    moving_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, columns = len(grid), len(grid[0])

    # Iterate each element in the grid.
    for i in range(rows): 
        for j in range(columns):
            # Skip if it's 0.
            if grid[i][j] == "0":
                continue
            
            # If the node is 1, try to merge / union it with neighbours.
            for x, y in moving_directions:
                new_row, new_col = i + x, j + y
                # Check whether the index and the element are valid.
                if 0 <= new_row < rows and 0 <= new_col < columns \
                    and grid[new_row][new_col] == "1":
                    # Union the node with its neighbour who is also 1.
                    union_find.union(i * columns + j, \
                                    new_row * columns + new_col)

    return union_find.count


if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"Number of islands: {num_of_islands_flood_fill(grid)}")
    print(f"Number of islands: {num_of_islands_union_find(grid)}")

    grid = [
        ["1","1","0","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Number of islands: {num_of_islands_flood_fill(grid)}")
    print(f"Number of islands: {num_of_islands_union_find(grid)}")