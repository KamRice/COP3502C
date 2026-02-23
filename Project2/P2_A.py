import console_gfx

user_Input = 1


def display_menu():
    print("RLE Menu", "--------", "0. Exit", "1. Load File", "2. Load Test Image", "3. Read RLE String",
          "4. Read RLE Hex String", "5. Read Data Hex String", "6. Display Image", "7. Display RLE String",
          "8. Display Hex RLE Data", "9. Display Hex Flat Data", sep="\n", end="\n\n")


def decode_rle(rle_data):
    rle_members = rle_data.split(":")

    for index in range(0, len(rle_members), 2):
        print(f"{index}: {rle_members[index]} instances of {rle_members[index + 1]}")3


if __name__ == '__main__':
    print("Welcome to the RLE image encoder:", end="\n\n")
    print("Displaying Spectrum Image:")

    console_gfx.display_image(console_gfx.test_rainbow)

    print("\n\n", end="")

    while user_Input:
        display_menu()
        user_Input = int(input("Select a menu Option: "))

        if user_Input == 1:
            filename = input("Enter name of file to load: ")
            image_Data = console_gfx.load_file(filename)
        elif user_Input == 2:
            image_Data = console_gfx.load_file(console_gfx.test_image)
            print("Test image data loaded.")
        elif user_Input == 3:
            decode_rle(input("Enter an RLE string to be decoded: "))
        elif user_Input == 6:
            console_gfx.display_image(image_Data)
