text = "all work and no play makes Jack a dull boy"

res = text.isupper()
print(res)


res = text.startswith("all work")
# text[:8] == "all work"
print(res)

new_text = text.replace("Jack", "John")
print(new_text)

res = text.split()
print(res)

text.lower()