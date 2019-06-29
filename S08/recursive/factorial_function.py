import sys


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)



if __name__ == '__main__':
    # sys.setrecursionlimit(100)
    print(factorial(100))
