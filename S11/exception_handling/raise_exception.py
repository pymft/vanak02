def fact(n):
    out = 1
    while n > 0:
        out *= n
        n -= 1

    return out


print(fact(5.1))