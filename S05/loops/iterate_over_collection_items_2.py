text = "It's four in the morning the end of December"
words = text.split()

i = 0

vowels = []
while i < len(words):
    word = words[i]
    i += 1

    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(word)

print(vowels)

