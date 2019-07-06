import re
f = open('mujir', encoding='utf-8')
text = f.read()
f.close()

pat = r"O\s+(.+?)![\.,]?\s+Exalted.*O\s+(.+?)!?[\.,]?\s+Keep"
result = re.findall(pat, text)
print(result)
