import collections


with open('wasteland.txt', mode='r', encoding='utf-8') as f:
    text = f.read()

words = text.lower().split()

res_new = collections.defaultdict(lambda : 0)

res = {}
for w in words:
    res[w] += 1
