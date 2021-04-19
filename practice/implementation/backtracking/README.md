# Backtracking

Essentially, backtracking is DFS, is a way of brute force exhaustion.

解决一个回溯问题，实际上就是一个决策树的遍历过程。
1. 路径：也就是已经做出的选择。
2. 选择列表：也就是你当前可以做的选择。
3. 结束条件：也就是到达决策树底层，无法再做选择的条件。

Backtracking template:

``` Python
result = []

def backtrack(路径, 选择列表):
    # 递归终止
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```
其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」。

典型问题：
1. 全排列
2. N 皇后问题

## Pruning

Pruning is used a lot in backtracking to reduce the search space.

Problems:
[x] [N-Queens](https://leetcode-cn.com/problems/n-queens/)
[x] [N-Queens II](https://leetcode-cn.com/problems/n-queens-ii/)
[x] [Valid Sudoku](https://leetcode-cn.com/problems/valid-sudoku/)
[x] [Sudoku Solver](https://leetcode-cn.com/problems/sudoku-solver/)

## Reference
1. [回溯算法详解](https://labuladong.github.io/algo/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3%E4%BF%AE%E8%AE%A2%E7%89%88.html)