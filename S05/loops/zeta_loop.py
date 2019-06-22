upper_limit = 1000000

# 1/1**2 + 1/2**2 + 1/3**2

n = 1
zeta = 0


while n < upper_limit:
    zeta = zeta + 1 / n ** 2
    n = n + 1

pi_approximate = (zeta * 6) ** 0.5
print(3.14159265359)
print(pi_approximate)
