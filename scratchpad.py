import math


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


x = 0


def scope_test():
    x = 15

    def change():
        global x
        x = 20

    change()


sum_all = lambda *args: sum(args)

# print(sum_all(1 , 2))

add1 = lambda val: val + 1


def magic(num, a_list):  # illustrate difference between an immutable variable "Num" and a mutable variable "a_list"
    num += 4
    a_list[1] = 4
    # a_list = [100, 102] #declared but not used.


# x = 2
seq_nums = [6, 9, 12]
magic(x, seq_nums)
# print(x, seq_nums)

"""
So for the magic() function above, the important concept is that the List object "a_list" is a MUTABLE object, 
which means that it is passed by reference as opposed to a IMMUTABLE object which is passed by value.

So the list seq_nums is declared, then passed to the magic() function as a REFERENCE, meaning that 
it is REFERRING to the already declared instance of the list. So seq_num is passed to magic(), it is altered 
at index 1 to set the value to 4. Then the seq_num variable is re-declared as a new list and no longer refers to the
seq_num of the global space. The function ends and the newly declared local instance of seq_num cease to exist. 

While num is passed as a VALUE, meaning that is is given as a straight value without ever connecting to the
global instance of num. So any changes or operations made on Num will not affect the global space num. Once 
magic() executes the local space instance of the num parameter (a Value) is trashed.

"""


def count_vowels(text):
    vowels = 'aeiou'
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


# print(count_vowels("yippee"))

def min_terms(value):
    i = 1
    summed_value = 0
    while summed_value < value:
        summed_value += (i ** i) / (2 * i)
        i += 1
    return i - 1


# print(min_terms(10000))

def star_triangles(num):
    for n in range(num):
        print("*" * n, sep='')


# star_triangles(5)

def reversed_start_triangles(num):
    for n in range(num):
        print("*" * (num - n), sep='')


# reversed_start_triangles(5)

def transform_numbers(num):
    for n in range(1, num + 1):
        if math.sqrt(n) % 1 == 0:
            if n % 2 == 0:
                print("EvenSquare")
            else:
                print("Square")
        else:
            print(n)


# transform_numbers(55)

def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


# print(is_prime(90))

def identical_digits(num):
    for n in range(num, 91):
        print(n, end=" ")
        if n // 10 == n % 10:
            break


#identical_digits(66)
