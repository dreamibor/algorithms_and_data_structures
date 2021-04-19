"""
DFS / BFS / Union Find - Number of Provinces (medium)

There are n cities. Some of them are connected, while some are not. If city 
a is connected directly with city b, and city b is connected directly with 
city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no 
other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if 
the ith city and the jth city are directly connected, and isConnected[i][j] 
= 0 otherwise.

Return the total number of provinces.

Example:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

LeetCode: https://leetcode-cn.com/problems/number-of-provinces/
"""

def num_of_provinces_dfs(isConnected: list) -> int:
    """ DFS - Flood Fill
    
    Time Complexity - O(N^2) - N is the number of cities, we need to iterate 
    each element in the matrix.
    Space Complexity - O(N) - An extra set `visited` to record the nodes have 
    been visited, the recursion call stack shall not exceed n.
    """
    # Edge cases
    if not isConnected or not isConnected[0]: return 0

    # The number of rows and columns are the same (equals to the number of 
    # cities).
    n = len(isConnected)
    # Set to track visited cities.
    visited = set()

    def _dfs(row):
        for col in range(n):
        # Check whether the two cities are connected and
        # whether the city has been visited.
            if isConnected[row][col] == 1 and col not in visited:
                # Add the city to visited list.
                visited.add(col)
                _dfs(col)
        return 1

    # count = 0
    # # Iterate through each city.
    # for i in range(n):
    #     # If it has not been visited, then DFS to its neighbour cities.
    #     if i not in visited:
    #         _dfs(i)
    #         count += 1
    # return count

    return sum([_dfs(i) if i not in visited else 0 for i in range(n)])

def num_of_provinces_bfs(isConnected: list) -> int:
    """ BFS - Flood Fill

    Time Complexity - O(N^2) - N is the number of cities, we need to iterate 
    each element in the matrix.
    Space Complexity - O(N) - For `visited` set to record visited nodes, the 
    number of elements in the queue will not exceed n.
    """
    # Edge cases
    if not isConnected or not isConnected[0]: return 0
    
    # The number of rows and columns are the same (equals to the number of 
    # cities).
    n = len(isConnected)
    visited = set()

    def _bfs(row):
        """ BFS to iterate traverse all cities."""
        queue = [row]

        while queue:
            row_n = queue.pop(0)
            # Mark the city as visited.
            visited.add(row_n)
            # Add all neighbour cities into queue.
            for col_n in range(n):
                if isConnected[row_n][col_n] == 1 and col_n not in visited:
                    queue.append(col_n)
        return 1
    
    # count = 0
    # for i in range(n):
    #     if i not in visited:
    #         _bfs(i)
    #         count += 1
    # return count

    # One-line
    return sum([_bfs(i) if i not in visited else 0 for i in range(n)])


def num_of_provinces_uf(isConnected: list) -> int:
    """ Union Find

    Time Complexity - O(N^2*logN) - N is the number of cities. We need to 
    iterate through the elements in the matrix, so the time complexity is 
    O(N^2), for cities are connected, we will do two finds and one unoin, 
    for Union Find using path compression, the worst case is O(logN), so 
    the total time complexity is O(N^2*logN), or in average O(N^2*α(n)). 
    α(n) is inverse Ackermann function, can be treated as a small constant.
    Space Complexity - O(N) - For the Union Find roots array.
    """
    n = len(isConnected)
    # Initialization for Union Find array.
    roots = [i for i in range(n)]

    def find(i):
        # Find root node for i.
        while i != roots[i]:
            i = roots[i]
        return i

    def union(x, y):
        # Union x and y.
        root_x = find(x)
        root_y = find(y)
        roots[root_y] = root_x
    
    for i in range(n):
        for j in range(i + 1, n):
            # If two cities are connected, then they are in the same
            # province, so union / merge them.
            if isConnected[i][j] == 1:
                union(i, j)
            
    return sum([roots[i] == i for i in range(n)])

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(f"Number of provinces (DFS): {num_of_provinces_dfs(isConnected)}")
    print(f"Number of provinces (BFS): {num_of_provinces_bfs(isConnected)}")
    print(f"Number of provinces ( UF): {num_of_provinces_uf(isConnected)}")

    isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    print(f"Number of provinces (DFS): {num_of_provinces_dfs(isConnected)}")
    print(f"Number of provinces (BFS): {num_of_provinces_bfs(isConnected)}")
    print(f"Number of provinces ( UF): {num_of_provinces_uf(isConnected)}")
