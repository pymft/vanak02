def fib(n):
    if n in (0, 1):
        return n
    res = fib(n-1) + fib(n-2)
    return res

if __name__ == '__main__':
    for i in range(20):
        print(fib(i), end=' ')

    # OUTPUT:
    # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181