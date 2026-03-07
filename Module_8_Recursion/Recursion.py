def factorial(value):
    if value > 0:
        return value * factorial(value - 1)
    return 1


# print(factorial(5))


def recursive_sum(value):
    if value == 0:
        return 0
    else:
        return value + recursive_sum(value - 1)


print()
# print(recursive_sum(6))
# print(2418 // 10)
# print()

test_List = [1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]
test_List2 = [21, 22, [12, [11, 12]]]


def flatten(tgt, out_array):
    for i in range(0, len(tgt), 1):
        if type(tgt[i]) is list:
            # print(tgt[i])
            flatten(tgt[i], out_array)
        else:
            out_array.append(tgt[i])
            # print(tgt)
    return out_array


def flatten_2(tgt, out_array):
    for i in range(len(tgt) - 1, -1, -1):
        if type(tgt[i]) is not list:
            out_array.append(tgt[i])
        else:
            flatten_2(tgt[i], out_array)
    return out_array


print(flatten_2(test_List, []))
print(flatten(test_List, []))
print(flatten_2(test_List2, []))
print(flatten(test_List2, []))


def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5
    while n >= 0:
        n -= 1
        a = b
        b = c
        c = d
        d = a - (c + e)
    return a


print()
print(mystery1(5))


def mystery_puzzle(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total


def mystery2(number, total):
    if number > 1:
        total += number % 10
        number //= 10
        return mystery2(number, total)

    return total


print()
print(mystery_puzzle(49090))
print(mystery2(49090, 0))

print()
print()
print("||| Collatz |||")
print()


def collatz(value):
    if value == 1:
        return str(value)
    elif value % 2 != 0:
        return f"{str(value)} {collatz(int((value * 3) + 1))}"
    else:
        return f"{str(value)} {collatz(int(value / 2))}"


print(collatz(13))
print(collatz(1333))

print("][][][][")


