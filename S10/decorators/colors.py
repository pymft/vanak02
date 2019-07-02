def cyan(fn):
    def inner(x):
        out = "\033[36m"
        out += fn(x)
        out += "\033[0m"
        return out

    return inner


def red(fn):
    def inner(x):
        out = "\033[31m"
        out += fn(x)
        out += "\033[0m"
        return out

    return inner


def green(fn):
    def inner(x):
        out = "\033[32m"
        out += fn(x)
        out += "\033[0m"
        return out

    return inner


def blue(fn):
    def inner(x):
        out = "\033[34m"
        out += fn(x)
        out += "\033[0m"
        return out

    return inner


@green
def say_hello(name):
    return "Hello " + name


print(say_hello("Jack"))
