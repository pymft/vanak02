n = 6
pattern = "*"
whitespace_pattern = " "

i = 1
while i <= n:
    stars = pattern * (2 * i - 1)
    line = stars.center(2*n - 1)
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
