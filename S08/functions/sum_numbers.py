def my_sum(*numbers):
    s = 0
    for num in numbers:
        s += num
    return s


val = my_sum(1, 2, 1, 2, 2, 33, 4, 5, 6, 7)
print(val)
