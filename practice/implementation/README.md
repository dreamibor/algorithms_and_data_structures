# Algorithm Templates

## 1. Backtracking (Recursion)

``` Python
def backtracking(level, param1, param2, ...):
    # Recursion termination
    if level > MAX_LEVEL:
        process(result)
        return None
    
    # Process data
    process_data(level, data)

    # Drill down
    # Could have multiple branches here, such as bianry tree 
    # or the traversing a grid (up, down, left, right). 
    backtracking(level + 1, new_param1, new_param2, ...)

    # Recover the current level's state if necessary
    reverse_state(level, ...)
```

## 2. Depth First Search (DFS)

``` Python
visited = set()

def dfs(node):
    # Recursion termination 
    # Reached the end of array or grid, or out of the range.
    if level > MAX_LEVEL:
        return None

    # Add the current node to visited.
    visited.add(node)

    # Explore all child nodes.
    for next_node in node.children():
        # Avoid traversing nodes have been visited
        if next_node not in visited:
            dfs(next_node)
```

## 3. Breadth First Search (BFS)

``` Python
def bfs(node):
    queue = [node]
    visited = set()
    
    while queue:
        # Pop out a new node and add it into visited list.
        node = queue.pop(0)
        visited.add(node)

        # Process data
        process_data(node)

        # Explore all child nodes.
        for next_node in node.children():
            # Avoid traversing nodes have been visited
            if next_node not in visited:
                queue.append(next_node)
```

## 4. Dynamic Programming (DP)

``` Python
# Define DP states
dp = [[0] * n for i in range(m)]

# Initialization
dp[0][0] = x
dp[0][1] = y

# DP
for i in range(m):
    for j in range(n):
        dp[i][j] = min/max(dp[i-1][j], dp[i][j-1], ...)

return dp[m][n]
```

## 5. Binary Search
To be used in sorted arrays:

``` Python
left, right = 0, n - 1

while left <= right:
    mid = left + (right - left) // 2

    if arr[mid] == target:
        # Found the target
        return or break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

## 6. Two Pointers

``` Python
# Sort the array first.
arr.sort()

left, right = 0, n - 1

while left < right:
    current_val = arr[left] + arr[right]

    if current_val > target:
        right -= 1
    elif current_val < target:
        left += 1
    else:
        return left or right.
```

## Reference

1. [Algorithm Templates](https://www.pluralsight.com/guides/algorithm-templates:-introduction)