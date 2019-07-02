def colorize(fn):
    def inner(x):
        out = "\033[36;4m"
        out += fn(x)
        out += "\033[0m"
        return out

    return inner


@colorize
def say_hello(name):
    return "Hello " + name


print(say_hello("Jack"))
