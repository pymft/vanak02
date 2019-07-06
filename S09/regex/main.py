import re
import urllib.request

def read_from_site(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    fp = urllib.request.urlopen(req)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return mystr



pat = r"\b\w+@[\w\.]+\b"
text = read_from_site("https://www.mtu.edu/mechanical/people/faculty-staff/")

print(text)
res = re.findall(pat, text)
print(res)