fr = open('input.txt')
num = int(fr.readline())
pattern = fr.readline().strip()
# text = fr.read()
# num, pattern = text.split('\n')
# num = int(num)
# fr.close()




fw = open('output.txt', mode='w')


for i in range(num):
    line = pattern * (i + 1)
    fw.write(line)
    fw.write('\n')

fw.close()
