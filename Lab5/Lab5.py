def hex_char_decode(digit):
    # Determine if digit is decimal numeric
    if 48 <= ord(digit) <= 57:
        return int(digit)
    else:
        if digit.upper() == "A":
            return 10
        if digit.upper() == "B":
            return 11
        if digit.upper() == "C":
            return 12
        if digit.upper() == "D":
            return 13
        if digit.upper() == "E":
            return 14
        if digit.upper() == "F":
            return 15


def hex_string_decode(hex):
    value = 0

    # Format provided hex if needed
    hex = hex.upper()

    if hex[0:2] == "0X":
        hex = hex[2:len(hex) + 1]

    current_term = len(hex) - 1

    for char in hex:
        value += 16 ** current_term * hex_char_decode(char)
        current_term -= 1

    return value


def binary_string_decode(binary):
    value = 0

    binary = binary.upper()

    if binary[0:2] == "0B":
        binary = binary[2:len(binary) + 1]

    current_term = len(binary) - 1

    for char in binary:
        value += 2 ** current_term * int(char)
        current_term -= 1
    return value


def binary_to_hex(binary):
    value = ""
    decimal_value = binary_string_decode(binary)
    if decimal_value == 0:
        return 0
    while int(decimal_value) >= 1:
        if int(decimal_value) % 16 == 10:
            value = "A" + value
        elif int(decimal_value) % 16 == 11:
            value = "B" + value
        elif int(decimal_value) % 16 == 12:
            value = "C" + value
        elif int(decimal_value) % 16 == 13:
            value = "D" + value
        elif int(decimal_value) % 16 == 14:
            value = "E" + value
        elif int(decimal_value) % 16 == 15:
            value = "F" + value
        else:
            value = str(int(decimal_value % 16)) + value

        decimal_value /= 16

    return value


""" --- MAIN LOOP --- """

active = True

while active:
    print("Decoding Menu", "-------------", "1. Decode hexadecimal", "2. Decode binary",
          "3. Convert binary to hexadecimal", "4. Quit", sep="\n", end="\n\n")

    userResponse = int(input("Please enter an option: "))
    if userResponse == 1:
        targetNumericString = input("Please enter the numeric string to convert: ")
        print(f"Result: {hex_string_decode(targetNumericString)}\n")
    elif userResponse == 2:
        targetNumericString = input("Please enter the numeric string to convert: ")
        print(f"Result: {binary_string_decode(targetNumericString)}\n")
    elif userResponse == 3:
        targetNumericString = input("Please enter the numeric string to convert: ")
        print(f"Result: {binary_to_hex(targetNumericString)}\n")
    else:
        print("Goodbye!")
        active = False
