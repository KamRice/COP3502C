def fibonacci(upperbound):
    lower = 0
    upper = 1
    for i in range(2, upperbound + 1):
        step = lower + upper
        lower = upper
        upper = step
    return lower


def is_prime(value):
    if value > 1:
        for i in range(2, value):
            if value % i == 0:
                return False
        return True
    return False


def print_prime_factors(value):
    i = 2
    print(f"{value} = ", sep='', end='')
    while i < value + 1:
        if value % i == 0 and i != value:
            print(f"{i} * ", sep='', end='')
            value = value / i
        elif i == value:
            print(f"{i}")
            value = value / i
        else:
            i += 1
