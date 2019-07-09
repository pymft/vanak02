name = "Some Name"
num = 100
val = 10.2

# Some Name, 100, 10.2
# line = name + ", " + str(num) + ", " + str(val)
# line = "{}, {}, {}, {}".format(name, num, val, name)
# line = "{0}, {1}, {2}, {0}".format(name, num, val)
# line = "{n}, {i}, {j}, {n}".format(n=name, i=num, j=val)
# line = "{name}, {num}, {val}, {name}".format(name=name, num=num, val=val)
x = 1_000_000_000
line = f"{name}, {num}, {val}, {x}"

print(line)
