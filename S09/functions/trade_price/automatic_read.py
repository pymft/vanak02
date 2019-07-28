import urllib.request


def read_from_site(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    with urllib.request.urlopen(req) as fp:
        mybytes = fp.read()

    mystr = mybytes.decode("utf8")


    return mystr


# scrapy

raw_data = read_from_site("https://api.pro.coinbase.com/products/BTC-USD/candles/5m")
btc = eval(raw_data)
f = lambda p: p[2]-p[1]
out = sorted(btc, key=f, reverse=True)
print(out[:10])

f2 = lambda p: p[-1]
mx = max(btc, key=f2)
print(mx)
