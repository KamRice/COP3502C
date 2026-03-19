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

    user_input = input("What would you like to do?")
