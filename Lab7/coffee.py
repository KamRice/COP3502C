from data import data as old_data
from convert import convert


def main():
    print("Welcome! Here is our menu:")
    print()

    data = convert(old_data)

    for category in data:
        print(category)
        print("-" * len(category))
        for item_name in data[category]:
            print(item_name)
        print()

    order = input("What would you like: ")

    price = -1
    for category in data:
        if order not in data[category]:
            continue
        price = data[category][order]

    if price == -1:
        print("I'm sorry, we don't serve that.")
        return

    print(f"Alright, that will be ${price:.2f}")


if __name__ == "__main__":
    main()