def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    n = input('please input the number of Fibonacci: ')
    print('The number of the {0}th Fibonacci is: {1}'.format(n, fib(n)))
