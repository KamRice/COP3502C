def digit_sum(val):
    # print(f"round: {val} -- val // 10: {val // 10} -- {val // 10 * 10}")
    if val > 1:
        print(val % (val // 10 * 10))
        return val % (val // 10 * 10) + digit_sum((val // 10))
    return 1


print(digit_sum(323))

# What is the smallest case?
# first digit of given value
# What do I return there?
# an int
# How do I make the problem smaller?
# floor divide by 10
# What does the recursive call return?
# an int
# How do I use that return value?
# add it to the previous value
# Am I definitely getting closer to stopping?
# im getting closer to my grave.
