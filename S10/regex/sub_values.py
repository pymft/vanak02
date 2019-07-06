import re

text = "06/07/1990"
pat = r"(\d\d)/(\d\d)/(\d\d\d\d)"
new_pat = r"\2-\1-\3"
result = re.findall(pat, text)
converted = re.sub(pat, new_pat, text)
print(result)
print(converted)
