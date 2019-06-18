number = 1010


for i in range(2, number):
    if number % i == 0:
        print("is not prime")
        break
else:
     print("prime")

