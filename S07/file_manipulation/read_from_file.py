f = open('input.txt', mode='r')

for i in range(5):
    f.seek(24*i)
    text = f.read(2)
    print(text)

f.close()