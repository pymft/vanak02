lst = [1, 100, 7, 34, 1000, 324]

indx = 0

for i in range(len(lst)):
    if lst[i] > lst[indx]:
        indx = i

print()