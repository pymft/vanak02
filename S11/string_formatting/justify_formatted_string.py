x = -10.987654
y = 20.123456
z = -30.3

# print(f"({x},{y},{z})")
# print(f"({x:10},{y:10},{z:10})")
# print(f"({x:<10},{y:>10},{z:^10})")
# print(f"({x:<10.2f},{y:>10.2f},{z:^10.2f})")
# print(f"({x:<+10.2f},{y:>+10.2f},{z:^+10.2f})")
# print(f"({x:<+10.2E},{y:>+10.1e},{z:^+10})")

# for i in range(10):
#     pat = "*" * (2 * i + 1)
#     print(f"{pat:^21}")

#
# char = "*"
# n = 20
# for i in range(n):
#     print(f"{char*(2*i+1):^21}")

char = "*"
n = 10
width = 2 * n + 1
for i in range(n):
    print(f"{char*(2*i+1):^{width}}")
