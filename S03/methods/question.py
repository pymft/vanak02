text_1 = "hello"
text_2 = "HELLO"
word = "hi"

text2 = text_1.upper()
word.upper()

lst = [1, 2, 3]
lst_aug = [5, 8, 11, 1, 1, 1]
print(id(lst), lst)

lst.append(100)
print(id(lst), lst)

lst.extend(lst_aug)
print(id(lst), lst)

lst.insert(2, 100)
print(id(lst), lst)

lst.remove(100)
print(id(lst), lst)

out = lst.pop()
print(id(lst), lst, out)


# lst.index

repeats = lst.count(1)
print(repeats)


