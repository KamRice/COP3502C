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


def show_pakuri_info(tgt_dex, species):
    if tgt_dex.get_size() <= 0:
        print("Error: No such Pakuri!")
        return

    species = tgt_dex.does_pakuri_exist(species)
    if species:
        print(f"\nSpecies: {species.species}")
        print(f"Attack: {species.get_attack()}")
        print(f"Defense: {species.get_defense()}")
        print(f"Speed: {species.get_speed()}")
        return

    else:
        print("Error: No such Pakuri!")


def add_new_pakuri(tgt_dex, species):
    if tgt_dex.get_size() >= tgt_dex.get_capacity():
        return "Error: Pakudex is full!"

    if tgt_dex.does_pakuri_exist(species):
        return "Error: Pakudex already contains this species!"

    tgt_dex.add_pakuri(species)
    return f"Pakuri species {species} successfully added!"


if __name__ == '__main__':
    print("Welcome to Pakudex: Tracker Extraordinaire!\n", end='')
    dex = Pakudex(input("Enter max capacity of the Pakudex: "))
    print(f"The Pakudex can hold {dex.get_capacity()} species of Pakuri.\n")

    display_menu()

    user_Input = get_user_input()

    while True:
        if user_Input == 1:
            list_pakuri(dex)
        elif user_Input == 2:
            show_pakuri_info(dex, input("Enter the name of the species to display: "))
        elif user_Input == 3:
            print(dex.add_pakuri(input("Enter the name of the species to add: ")))
        elif user_Input == 4:
            print(dex.evolve_species(input("Enter the name of the species to evolve: ")))
        elif user_Input == 5:
            print(dex.sort_pakuri())
        elif user_Input == 6:
            break

        display_menu()

        user_Input = get_user_input()
