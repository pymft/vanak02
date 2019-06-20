number = 1010


i = 2

while i < number:
    if number % i == 0:
        is_prime = False
        break
    i = i + 1


print("is prime? ", is_prime)
