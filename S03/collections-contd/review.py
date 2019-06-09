numbers = [100, 200, 300]

list_new = numbers

# lists are mutable
print(numbers)
print(list_new)
numbers[1] = "hello"
print(numbers, list_new, sep="")

num = 1
print(id(num), num)
num = 10
print(id(num), num)

# tuple: immutable
nums = (100, 200, 300)

#         0           1       2        3
#         id          name    lastname birth
person = [1234567890, "John", "Smith", 1980]
person = {"id": 1234567890 , "first name": "John", "last name": "Smith", "birth": 1980}
print(person["last name"])
print(person)
person["nationality"] = "French"
print(person)

# int, float, str, tuple, bool,
