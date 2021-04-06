# Recursion

Template for recursion:

``` Python
def recursion(level, param1, param2, ...):
    # Recursion termination
    if level > MAX_LEVEL:
        print(result)
        return 

    # Process logic in current level
    process_data(level, data)

    # Drill down further level
    recursion(level + 1, param1, param2, ...)

    # After we've solved the problem for the next level, reverse the current level status if needed
    reverse_state(level)
```

Drawbacks:
1. Duplicated calculations.

# Divide and Conquer

Template for Divide and Conquer:

``` Python

def divide_and_conquer(problem, param1, param2, ...):
    # Recursion termination
    if problem is None:
        print(result)
        return 
    
    # Prepare data
    data = prepare_data(problem)
    sub_problems = split_problem(problem_data)

    # Conquer sub-problems
    sub_result_1 = divide_and_conquer(sub_problems[0], param1, param2, ...)
    sub_result_2 = divide_and_conquer(sub_problems[1], param1, param2, ...)
    ...

    # Process and generate the final result
    result = process_result(sub_result_1, sub_result_2, ...)
```