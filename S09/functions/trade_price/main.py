from prices import btc

f = lambda p: p[2]-p[1]
out = sorted(btc, key=f, reverse=True)
print(out[:10])

f2 = lambda p: p[-1]
mx = max(btc, key=f2)
print(mx)
