def extract_data(fname):
    data = open(fname).read()
    lines = data.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',', ' ').split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return lines


def is_triangle(sides):
    if len(sides) != 3:
        return False

    a, b, c = sides

    if a < b + c and b < a + c and c < a + b:
        return True

    return False


def type_of_triangle(triangle):
    types = []
    if is_triangle(triangle):




if __name__ == '__main__':

    fname = "./../../../S07/triangles/inp.txt"

    triangles = extract_data(fname)
    count = 0

    for triangle in triangles:
        if is_triangle(triangle):
            count += 1

    print(count)
