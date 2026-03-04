def convert(unconverted_data):
    new_data = {"Drink": {}, "Food": {}}

    for menu_category in unconverted_data:
        if menu_category["type"] == "Food":
            new_data["Food"][menu_category["name"]] = menu_category["price"]
        elif menu_category["type"] == "Drink":
            new_data["Drink"][menu_category["name"]] = menu_category["price"]

    return new_data
