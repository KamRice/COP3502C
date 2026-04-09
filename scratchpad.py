#####################
### Linear Search ###
#####################

# my_books = ["The Supper Club", "1984", "Responsive Web Design", "The Great Gatsby"]
#
#
# def linear_search(books, target):
#     for i in range(0, len(books)):
#         if books[i].upper() == target.upper():
#             return i + 1
#     return -1
#
#
# print(linear_search(my_books, "asd"))
# print(linear_search(my_books, "The fake Gatsby"))
# print(linear_search(my_books, "Responsive Web Design"))
# print(linear_search(my_books, "THE SUPPER CLUB"))
# print(linear_search(my_books, "The Great Gatsby"))

#####################
### Binary Search ###
#####################

dummy_data = [3, 9, 15, 22, 28, 34, 41, 47, 53, 66, 72, 79, 85, 91, 92, 98, 104, 110, 113, 117, 123, 130, 136, 142, 149,
              155, 161, 168, 174, 175, 176, 180, 187]


def binary_search(data, tgt):
    print(f"index: {int(len(data) / 2)} -- {data[int(len(data) / 2)]}")
    if data[int(len(data) / 2)] == tgt:
        return int(len(data) / 2)
    if int(len(data) / 2) == 1:
        return -1
    elif data[int(len(data) / 2)] > tgt:
        print(f"\nRemaining Elements: {len(data)}")
        return binary_search(data[0:int(len(data) / 2)], tgt)
    else:
        print(f"\nRemaining Elements: {len(data)}")
        return binary_search(data[int(len(data) / 2): int(len(data))], tgt)


binary_search(dummy_data, 121)
