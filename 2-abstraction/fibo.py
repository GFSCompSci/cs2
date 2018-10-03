import sys

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    for i in range(2,n): a, b = b, a+b
    print b


if __name__ == "__main__":
    fib(int(sys.argv[1]))
