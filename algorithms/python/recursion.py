def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

print(fibonacci(5))
print(fib(50))