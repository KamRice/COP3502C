# Practice Problem 1
def min_terms(value):
    i = 1
    summed_value = 0
    while summed_value < value:
        summed_value += (i ** i) / (2 * i)
        i += 1
    return i - 1


# Practice Problem 2
def fizzbuzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


# fizzbuzz(15)

# Practice Problem 3
def print_square(side_length):
    for i in range(1, side_length + 1):
        # print(f"i:{i}")
        if i == 1 or i == side_length:
            print("*" * side_length)
            continue
        for j in range(1, side_length + 1):
            if j == 1:
                print("*", end='')
            elif j == side_length:
                print("*", sep='')
            else:
                print(" ", sep='', end='')


# Practice Problem 4
def print_pyramid(height):
    for i in range(0, height):
        print(" " * i, sep='', end='')
        for j in range(height - i):
            print("* ", sep='', end='')
        print()