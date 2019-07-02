a, b, *c, t = 1, 2, 3, 4, 5, 6
print(c)
x = (1, 2, 3)
y = (10, 20, 30)

z = (0, *x, 0, *y, 0)
print(z)
print(len(z))

res = (*x, *x[::-1])
print(res)

