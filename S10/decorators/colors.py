def colorize(color_name):
    color_map = {'red': 1,
                 'green': 2,
                 'yellow': 3,
                 'blue': 4,
                 'cyan': 6,
                 'purple': 5,
                 'gray': 7}
    def color(fn):
        def inner(x):
            out = "\033[3" + str(color_map[color_name]) + "m"
            out += fn(x)
            out += "\033[0m"
            return out

        return inner
    return color


def red(fn):
    def inner(x):
        out = fn(x)
        if out.startswith("\033["):
            # change color
            pass
        else:
            out = "\033[31m" + out + "\033[0m"

        return out

    return inner


@colorize('yellow')
def say_hello(name):
    return "Hello " + name


print(say_hello("Jack"))

# weird_result = colorize('red')(say_hello)("Jack")
# print(weird_result)
