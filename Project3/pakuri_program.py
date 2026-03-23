from pakuri import *
from pakudex import *


def display_menu():
    # @formatter:off
    print("Pakudex Main Menu\n" +
              "-----------------\n" +
              "1. List Pakuri\n" +
              "2. Show Pakuri\n" +
              "3. Add Pakuri\n" +
              "4. Evolve Pakuri\n" +
              "5. Sort Pakuri\n" +
              "6. Exit\n\n")
    # @formatter:on


def get_user_input():
    user_input = input("What would you like to do? ")

    try:
        int(user_input)
    except ValueError:
        return get_user_input()
    if 0 < int(user_input) <= 6:
        return int(user_input)
    else:
        return get_user_input()


def list_pakuri(pakudex):
    print("Pakuri in Pakudex:")
    pakudex_list = pakudex.get_species_array()

    if len(pakudex_list) > 0:

        for index in range(0, len(pakudex_list)):
            print(f"{index + 1}. {pakudex_list[index].species}")
    else:
        print("No Pakuri in Pakudex yet!")

def add_new_pakuri(species):
    new_species = input("Enter the name of the species to add: ")



def show_pakuri_info(pakudex, species):
    pakudex_list = pakudex.get_species_array()
    if len(pakudex_list) > 0:

        for index in range(0, len(pakudex_list)):

            if pakudex_list[index].species == species:
                print(f"\nSpecies: {pakudex_list[index].species}")
                print(f"Attack: {pakudex_list[index].get_attack()}")
                print(f"Defense: {pakudex_list[index].get_defense()}")
                print(f"Speed: {pakudex_list[index].get_speed()}")
                return
        else:
            print("Error: No such Pakuri!")


if __name__ == '__main__':
    print("Welcome to Pakudex: Tracker Extraordinaire!\n", end='')
    dex = Pakudex(input("Enter max capacity of the Pakudex: "))
    print(f"The Pakudex can hold {dex.capacity} species of Pakuri.\n")

    obj = Pakuri("pika")
    obj1 = Pakuri("CharChar")
    obj2 = Pakuri("Bulby")

    dex.add_pakuri(obj)
    dex.add_pakuri(obj1)
    dex.add_pakuri(obj2)

display_menu()

user_Input = get_user_input()

if user_Input == 1:
    list_pakuri(dex)
elif user_Input == 2:
    show_pakuri_info(dex, input("Enter the name of the species to display: "))
elif user_Input == 3:
    pass
elif user_Input == 4:
    pass
elif user_Input == 5:
    pass
elif user_Input == 6:
    pass
