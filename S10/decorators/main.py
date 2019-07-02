def decorate(fn):
    # fun = lambda x: f(x)
    def inner(x):
        out = fn(x)
        out = "*" + out + "*"
        return out

    return inner


def say_hello(name):
    return "Hello " + name


print(say_hello("Jack"))
say_hello_new = decorate(say_hello)
print(say_hello_new("Jack"))