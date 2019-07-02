from time import ctime



def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    f = open('output.log', mode='a')
    f.write(ctime() + " | fact | " + str(n) + " | " + str(fact) + "\n")
    f.close()
    return fact

def mysum(a, b):
    out = a + b
    f = open('output.log', mode='a')
    f.write(ctime() + " | mysum | " + str((a, b)) + " | " + str(out) + "\n")
    f.close()
    return out


factorial(10)
mysum(10, 20)
factorial(2)
factorial(5)