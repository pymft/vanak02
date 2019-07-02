lst = [(1, 2), 1, 2, 4, -5, 3, 6, -8]
# ls2 = [abs(7), abs(1), abs(2), abs(4), abs(-5), abs(3), abs(6), abs(-8)]
f = lambda x: abs(2-x)
ls2 = [f(7), f(1), f(2), f(4), f(-5), f(3), f(6), f(-8)]
#     [5, 1, 0, 2, 7, 1, 4, 10]
print(lst)
# lst.sort()
out = sorted(lst, key=f)
print(lst)
print(out)
