from prices import btc
f = lambda p: p[2] - p[1]

# out = []
#
# for p in btc:
#     out.append(f(p))

# out =[f(k) for k in btc]
out = list(map(f, btc))
print(type(out))
# for d in out:
#     print(d)

print(out.__sizeof__())