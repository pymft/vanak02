n = 10
pattern = "#"
whitespace_pattern = "."

i = 1
while i <= n:
    white = whitespace_pattern * (n - i)
    if i % 2 == 1:
        stars = pattern * (2 * i - 1)
    else:
        mid_whites = " " * (2 * i - 3)
        stars = pattern + mid_whites + pattern

    line = white + stars + white
    print(line)
    i = i + 1


# OUTPUT
#
#      *
#     * *
#    *****
#   *     *
#  *********
# *         *
