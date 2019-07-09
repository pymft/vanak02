class NegativeValueOfFactorialError(ArithmeticError):
    pass


class InvalidTypeFactorialError(TypeError):
    pass


def fact(n):
    if not type(n) == int:
        raise InvalidTypeFactorialError(f"invalid type for variable n ( {type(n)} )")

    if n < 0:
        raise NegativeValueOfFactorialError(f"negative value n={n} ")

    out = 1
    while n > 0:
        out *= n
        n -= 1

    return out



try:
    res = fact("salam")
    # res = fact(10.1)
    # res = fact(-100)
    print(res)
except NegativeValueOfFactorialError as e:
    print(e.args[0])
except InvalidTypeFactorialError as e:
    print(e.args[0])


