def summate(*passed_args):
    sum_total = 0
    for argument in passed_args:
        sum_total += argument
    return f"{float(sum_total)}"


"""
print(summate(1, 2, 3))
print(summate())
print(summate(0.5, 0.25, 0.125, 0.0625))
print(summate(1.0, 2.0, ))
print(summate(2, 2, 4))
"""


def print_range(lower, upper):
    for value in range(lower, upper + 1):
        print(value, end="")
        if value < upper:
            print(", ", end="")
    print()


"""
print_range(1, 3)
print_range(3, 6)
"""


def foo(a, b, c=2):
    print(a)
    print(b)
    print(c)


def add():
    x = 15

    def change():
        global x
        x = 20

    change()


add()
print(x)
