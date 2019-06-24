text = input("enter numbers")
numbers = text.split()
my_sum = 0

for val in numbers:
    my_sum = my_sum + int(val)

print(my_sum)
