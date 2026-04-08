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
              "6. Exit\n")
    # @formatter:on


def get_user_input():
    user_input = input("What would you like to do? ")

    try:
        int(user_input)
    except ValueError:
        print("Unrecognized menu selection!\n")
        display_menu()
        return get_user_input()
    if 0 < int(user_input) <= 6:
        return int(user_input)
    else:
        print("Unrecognized menu selection!\n")
        display_menu()
        return get_user_input()


def list_pakuri(pakudex):
    print("Pakuri In Pakudex:")
    pakudex_list = pakudex.get_species_array()

    if len(pakudex_list) > 0:

        for index in range(0, len(pakudex_list)):
            print(f"{index + 1}. {pakudex_list[index].species}")
        print("")
    else:
        print("No Pakuri in Pakudex yet!")


def show_pakuri_info(tgt_dex, species):
    if tgt_dex.get_size() <= 0:
        print("Error: No such Pakuri!\n")
        return

    species = tgt_dex.does_pakuri_exist(species)

    if species:
        print(f"\nSpecies: {species.species}")
        print(f"Attack: {species.get_attack()}")
        print(f"Defense: {species.get_defense()}")
        print(f"Speed: {species.get_speed()}\n")
        return

    else:
        print("Error: No such Pakuri!\n")


def add_new_pakuri(tgt_dex):
    if tgt_dex.get_size() >= tgt_dex.get_capacity():
        print("Error: Pakudex is full!\n")
        return False

    tgt_species_to_add = input("Enter the name of the species to add: ")

    if tgt_dex.does_pakuri_exist(tgt_species_to_add):
        return False

    tgt_dex.add_pakuri(tgt_species_to_add)
    print(f"Pakuri species {tgt_species_to_add} successfully added!\n")
    return True


if __name__ == '__main__':
    print("Welcome to Pakudex: Tracker Extraordinaire!\n", end='')
    while True:
        try:
            tgt_size = int(input("Enter max capacity of the Pakudex: "))
            if tgt_size <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid size.")
    dex = Pakudex(tgt_size)
    print(f"The Pakudex can hold {dex.get_capacity()} species of Pakuri.\n")

    display_menu()

    user_Input = get_user_input()

    while True:
        if user_Input == 1:
            list_pakuri(dex)
        elif user_Input == 2:
            show_pakuri_info(dex, input("Enter the name of the species to display: "))
        elif user_Input == 3:
            add_new_pakuri(dex)
        elif user_Input == 4:
            tgt_species = input("Enter the name of the species to evolve: ")
            if dex.evolve_species(tgt_species):
                print(f"{tgt_species} has evolved!\n")
            else:
                print("Error: No such Pakuri!\n")
        elif user_Input == 5:
            print(dex.sort_pakuri())
        elif user_Input == 6:
            print("Thanks for using Pakudex! Bye!")
            break

        display_menu()

        user_Input = get_user_input()
