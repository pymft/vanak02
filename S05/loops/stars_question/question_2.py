n = 6
pattern = "*"

i = 1
while i <= n:
    white = " " * (n - i)
    stars = pattern * (2 * i - 1)
    line = white + stars
    print(line)
    i = i + 1


# OUTPUT
#
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
