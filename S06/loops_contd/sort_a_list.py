# [1, 100, 7, 34, 1000, 324], []
# [1, 100, 7, 34, 324], [1000]
# [1, 100, 7, 34], [1000, 324]
# [1, 7, 34], [1000, 324, 100]
# [1, 7], [1000, 324, 100, 34]
# [1], [1000, 324, 100, 34, 7]
# [], [1000, 324, 100, 34, 7, 1]

lst = [1, 100, 7, 34, 1000, 324]
sorted_list = []

print(lst, sorted_list)


while lst:
    mx = lst[0]
    for num in lst:
        if num > mx:
            mx = num

    lst.remove(mx)
    sorted_list.append(mx)


print(lst, sorted_list)