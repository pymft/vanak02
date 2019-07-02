from prices import btc

f = lambda p: p[-1] > 700

# out = list(filter(f, btc))
# out = [p for p in btc if f(p)]
out = [p for p in btc if p[-1] > 700]
print(out)
