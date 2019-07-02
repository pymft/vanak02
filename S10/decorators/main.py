def decorate(fn):
    def inner(x):
        out = "*"
        out += fn(x)
        out += "*"
        return out

    return inner


def say_hello(name):
    return "Hello " + name


say_hello = decorate(say_hello)
print(say_hello("Jack"))