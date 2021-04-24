"""
Stack - Daily Temperatures (medium)

Given a list of daily temperatures T, return a list such that, for each day 
in the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 
instead.

For example, given the list of temperatures 
T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be: 
[1, 1, 4, 2, 1, 1, 0, 0].

Note: 
The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100]. 

LeetCode: https://leetcode-cn.com/problems/daily-temperatures/
"""

def daily_temp(temperatures: list) -> list:
    """ Monotonic Decreasing Stack

    In the stack, it's decreasing from bottom to top, where bottom is the 
    largest and top is the smallest. 

    Iterate through the array, if the stack is not empty, compare the current 
    value with the stack top, if the current value is larger than the top, 
    then we shall pop out the stack top, and calculate the distance between 
    indices, which will be the value that we want. If the current number is 
    smaller than the stack top, then push the current number into the stack.

    Time Complexity - O(N) - 
    Space Complexity - O(N) - 
    """
    result = [0] * len(temperatures)
    # Monotonic decreasing stack for indices.
    stack = []

    for i, num in enumerate(temperatures):
        # While the stack is not empty and the current is larger than the 
        # top of the stack, pop out the top, and the distance between 
        # current value's index and the top's index, is the value we want.
        while stack and num > temperatures[stack[-1]]:
            # Pop out the previous value's index which is smaller 
            # than current value.
            prev_index = stack.pop()
            # Calculate he distance between them.
            result[prev_index] = i - prev_index
        
        # Append the current index into the stack.
        stack.append(i)
    
    return result


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temp(temperatures))
