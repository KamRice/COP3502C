import console_gfx


def display_menu():
    print("RLE Menu", "--------", "0. Exit", "1. Load File", "2. Load Test Image", "3. Read RLE String",
          "4. Read RLE Hex String", "5. Read Data Hex String", "6. Display Image", "7. Display RLE String",
          "8. Display Hex RLE Data", "9. Display Hex Flat Data", sep="\n", end="\n\n")


def decode_rle(rle_data):
    pass


def string_to_rle(rle_string):
    split_string = rle_string.split(":")

    print(len(split_string))
    print()
    for index in range(0, len(split_string)):
        print(split_string[index])

    print()
    print()


def main():
    user_input = 1

    print("Welcome to the RLE image encoder:", end="\n\n")
    print("Displaying Spectrum Image:")

    console_gfx.display_image(console_gfx.test_rainbow)

    print("\n\n", end="")

    while user_input:
        display_menu()
        user_input = int(input("Select a menu Option: "))

        if user_input == 1:
            filename = input("Enter name of file to load: ")
            image_data = console_gfx.load_file(filename)
        elif user_input == 2:
            image_data = console_gfx.test_image
            print("Test image data loaded.")
        elif user_input == 3:
            string_to_rle(input("Enter an RLE string to be decoded: "))
        elif user_input == 6:
            if image_data is not None:
                console_gfx.display_image(image_data)


# if __name__ == '__main__':
#   main()

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


# test_list = [3, 2, 5, 4, 4, 4, 5, 5, 5]
# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# test_list = [5, 12, 8, 5, 3, 11, 7, 2, 3, 16, 4]
test_list = [2, 1, 3]
test_string = "abcd3fgh1"

# print(consecutive_fours(test_list))

# sum_by_parity(test_list)

# print(expand_by_index(test_list))

print(numerical_count(test_string))
