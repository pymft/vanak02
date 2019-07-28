import os


# os.system("notepad")
# with os.popen("ipconfig") as cmd:
#     text = cmd.read()

# print(text)

for i in range(2, 100):
    os.mkdir(f"src/folder{i:02}")

