import re

text = """40,      10.0, 0.0, 0.0
1,5.0, 10.0, 0.0
2,7.5, 10.0, 0.0
3, 10.0, 10.0, 0.0"""

pat = r"(\d+),\s*([\d\.]+),\s*([\d\.]+),\s*([\d\.]+)"

result = re.findall(pat, text)
print(result)
