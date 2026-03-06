import console_gfx


def display_menu():
    print("RLE Menu", "--------", "0. Exit", "1. Load File", "2. Load Test Image", "3. Read RLE String",
          "4. Read RLE Hex String", "5. Read Data Hex String", "6. Display Image", "7. Display RLE String",
          "8. Display Hex RLE Data", "9. Display Hex Flat Data", sep="\n", end="\n\n")


def to_hex_string(data):
    output_str = ''

    for member in range(0, len(data), 2):
        output_str += f"{decimal_to_hex(data[member])}{decimal_to_hex(data[member + 1])}"
    return output_str


def count_runs(flat_data):
    # print(f"Analyze: {flat_data}")
    # print()

    current_member_value = flat_data[0]
    current_run = 1
    run_count = 0

    for member in range(1, len(flat_data)):
        # print(f"{flat_data[member]} : {flat_data[member - 1]}")
        current_member_value = flat_data[member]
        if current_member_value == flat_data[member - 1] and current_run < 16:
            current_run += 1
            # print(f"current_run += 1 --> streak: {current_run}")
        else:
            run_count += 1
            current_run = 1
            # print(f"KILL current_run --> streak: {current_run}")
            # print(f"run_count += 1 ---> count: {run_count}")
    run_count += 1
    return run_count


def encode_rle(flat_data):
    # print(f"Analyze: {flat_data}")
    # print()

    output_list = []
    current_member_value = flat_data[0]
    current_run = 1

    for member in range(1, len(flat_data)):
        # print(f"{flat_data[member]} : {flat_data[member - 1]}")
        current_member_value = flat_data[member]
        if current_member_value == flat_data[member - 1] and current_run < 15:
            current_run += 1
            # print(f"current_run += 1 --> streak: {current_run}")
        else:
            # print(f"{current_run}, {current_member_value}")
            output_list.append(current_run)
            output_list.append(flat_data[member - 1])
            current_run = 1
            # print(f"KILL current_run --> streak: {current_run}")
    output_list.append(current_run)
    output_list.append(flat_data[len(flat_data) - 1])
    return output_list


def get_decoded_length(rle_data):
    decoded_length = 0
    for member in range(0, len(rle_data), 2):
        decoded_length += rle_data[member]

    return decoded_length


def decode_rle(rle_data):
    # print(f"Analyze: {rle_data}")
    # print()

    output_list = []

    if len(rle_data) % 2 != 0:
        return []
    for members in range(0, len(rle_data), 2):
        # print(f"Member pair: {members}")
        # print(f"{rle_data[members]} - {rle_data[members + 1]}")
        for i in range(0, int(rle_data[members])):
            output_list.append(rle_data[members + 1])
    # print()
    return output_list


def string_to_data(rle_string):
    if len(rle_string) % 2 != 0:
        return []

    output_list = []

    for member in range(0, len(rle_string), 2):
        if 48 <= ord(rle_string[member]) <= 57:
            output_list.append(int(rle_string[member]))
        else:
            output_list.append(int(hex_string_decode(rle_string[member])))

        if 48 <= ord(rle_string[member + 1]) <= 57:
            output_list.append(int(rle_string[member + 1]))
        else:
            output_list.append(int(hex_string_decode(rle_string[member + 1])))

    return output_list


def to_rle_string(rle_data):
    pass


def string_to_rle(rle_string):
    split_string = rle_string.split(":")

    print(len(split_string))
    print()
    for index in range(0, len(split_string)):
        print(split_string[index])

    print()
    print()
    rle_string.split(":")


"""
Main
"""


def main():
    user_input = 1

    print("Welcome to the RLE image encoder!", end="\n\n")
    print("Displaying Spectrum Image:")

    console_gfx.display_image(console_gfx.test_rainbow)

    print()

    while user_input:
        display_menu()
        user_input = int(input("Select a Menu Option: "))

        if user_input == 1:
            filename = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(filename)
        elif user_input == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif user_input == 3:
            image_data = input("Enter an RLE string to be decoded: ")
            decode_rle(string_to_rle(image_data))
        elif user_input == 6:
            if image_data is not None:
                console_gfx.display_image(image_data)


"""
Hex/Decimal/Binary Helpers
"""


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


def hex_string_decode(hex_char):
    value = 0

    # Format provided hex if needed
    hex_char = hex_char.upper()

    if hex_char[0:2] == "0X":
        hex_char = hex_char[2:len(hex_char) + 1]

    current_term = len(hex_char) - 1

    for char in hex_char:
        value += 16 ** current_term * hex_char_decode(char)
        current_term -= 1

    return value


def decimal_to_hex(decimal):
    if decimal <= 9:
        return decimal
    else:
        if decimal == 10:
            return "a"
        if decimal == 11:
            return "b"
        if decimal == 12:
            return "c"
        if decimal == 13:
            return "d"
        if decimal == 14:
            return "e"
        if decimal == 15:
            return "f"
    return None


"""
Follow along practices.
"""


def consecutive_fours(input_list):
    streak = 1

    for member in range(1, len(input_list) - 1):
        if input_list[member] == input_list[member + 1]:
            streak += 1
            if streak == 4:
                return True
        else:
            streak = 1

    return False


def sum_by_parity(input_list):
    output_value = [0, 0]
    for member in range(0, len(input_list)):
        if member % 2 == 0:
            output_value[0] += input_list[member]
        else:
            output_value[1] += input_list[member]
    print(output_value)


def expand_by_index(input_list):
    output_value = []

    for member in range(0, len(input_list)):
        for i in range(input_list[member]):
            output_value.append(member)

    return output_value


def numerical_count(string):
    count = 0
    for char in string:
        if char.isdigit():
            count += 1
    return count

# if __name__ == '__main__':
#     main()
