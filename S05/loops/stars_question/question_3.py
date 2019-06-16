n = 6
pattern = "*"

i = 1
while i <= n:
    white = " " * (n - i)
    if i % 2 == 1:
        stars = pattern * (2 * i - 1)
    else:
        mid_whites = " " * (2 * i - 3)
        stars = pattern + mid_whites + pattern

    line = white + stars
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
