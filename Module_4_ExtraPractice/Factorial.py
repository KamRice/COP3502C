userInput = int(input("Give Int (must be non negative integer): "))
index = 1
factorial = 1

while index <= userInput:
    factorial *= index
    index += 1

print(factorial)