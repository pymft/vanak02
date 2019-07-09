a = 10
b = 2
lst = [1, 2, 3, 4]
dct = {'name': 'John', 'last name': 'Smith'}

try:
    val = a / b
    print(val)
    print(lst[1])
    print(dct['last name'])
except IndexError as e:
    print(e.args)
    print("got index error!")
except ZeroDivisionError:
    print("got zero division error!")
except KeyError:
    print("got key err")
finally:
    print("Hello")


print("goodbye!")
