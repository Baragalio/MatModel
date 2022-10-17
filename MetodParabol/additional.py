def a0(x1, f):
    return f(x1)


def a1(x1, x2, f):
    return (f(x2) - f(x1)) / (x2 - x1)


def a2(x1, x2, x3, f):
    return 1 / (x3 - x2) * (((f(x3) - f(x1)) / (x3 - x1)) - ((f(x2) - f(x1)) / (x2 - x1)))


def Xmin(x1, x2, x3, f):
    return 1/2 * (x1 + x2 - a1(x1, x2, f)/a2(x1, x2, x3, f))

# уравнение параболлы
def q(x, x1, x2, x3, f):
    return a0(x1, f) + a1(x1, x2, f) * (x - x1) + a2(x1, x2, x3, f) * (x - x1) * (x - x2)
