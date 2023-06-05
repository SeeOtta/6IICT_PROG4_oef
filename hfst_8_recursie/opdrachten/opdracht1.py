""" Los de reeks van Fibonacci recursief op. """

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(2))     # 1
print(fib(4))     # 3
print(fib(10))    # 55
print(fib(25))    # 75025
