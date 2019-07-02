n = 6
pattern = "*"


print(" "*(n-1) + pattern)
i = 2

while i < n:
    white = " " * (n - i)
    mid_whites = " " * (2 * i - 3)
    stars = pattern + mid_whites + pattern
    line = white + stars
    print(line)
    i = i + 1

print(pattern * (2 * n - 1))

# OUTPUT
#
#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********
