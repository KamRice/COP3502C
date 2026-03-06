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


def decimal_to_hex(decimal):
    if decimal <= 9:
        return decimal
    else:
        if decimal == 10:
            return "A"
        if decimal == 11:
            return "B"
        if decimal == 12:
            return "C"
        if decimal == 13:
            return "D"
        if decimal == 14:
            return "E"
        if decimal == 15:
            return "F"
    return None


def to_hex_string(data):
    output_str = ''

    for member in range(0, len(data), 2):
        print(f"{data[member]}")
        output_str += f"{data[member]}{decimal_to_hex(data[member + 1])}"
    return output_str


def count_runs(flat_data):
    print(f"Analyze: {flat_data}")
    print()

    current_member_value = flat_data[0]
    current_run = 1
    run_count = 0

    for member in range(1, len(flat_data)):
        print(f"{flat_data[member]} : {flat_data[member - 1]}")
        current_member_value = flat_data[member]
        if current_member_value == flat_data[member - 1] and current_run < 16:
            current_run += 1
            print(f"current_run += 1 --> streak: {current_run}")
        else:
            run_count += 1
            current_run = 1
            print(f"KILL current_run --> streak: {current_run}")
            print(f"run_count += 1 ---> count: {run_count}")
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
        if current_member_value == flat_data[member - 1]:
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


def string_to_data(rle_string):
    if len(rle_string) % 2 != 0:
        return []

    output_list = []

    # Change range to range(2, len(rle_string), 2) for image dimensions?
    for members in range(0, len(rle_string), 2):
        if 48 <= ord(rle_string[members]) <= 57:
            output_list.append(int(rle_string[members]))
        else:
            output_list.append(int(hex_string_decode(rle_string[members])))

        if 48 <= ord(rle_string[members + 1]) <= 57:
            output_list.append(int(rle_string[members + 1]))
        else:
            output_list.append(int(hex_string_decode(rle_string[members + 1])))

    return output_list


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


rle_test_string = "1Aff3f3A64"
test_case1 = "1912101f101f101f101f101f101f101f101f101f"
test_case2 = "26f0f04029"
test_case3 = "1914f1f161"
test_case4 = "16181f1e1d1c1b1a191817161514131211101f1e1d1c1b1a191817161514131211101f1e1d1c1b1a19181716151413121110"
test_case5 = "11f0f03029"

print(encode_rle([9, 9, 9, 9, 2, 2, 1, 0]))

# print(get_decoded_length((string_to_data(rle_test_string))))
# print()
# print(encode_rle(decode_rle(string_to_data(rle_test_string))))
# print()
# print(decode_rle(string_to_data(test_case1)))
# print()
# print(decode_rle(string_to_data(test_case2)))
# print()
# print(decode_rle(string_to_data(test_case3)))
# print()
# print(decode_rle(string_to_data(test_case4)))
# print()
# print(decode_rle(string_to_data(test_case5)))
# print()
