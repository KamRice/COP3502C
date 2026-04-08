from pakuri import Pakuri


class Pakudex:
    def __init__(self, _capacity=20):
        self.capacity = _capacity
        self.size = 0
        self.species_array = []

    def get_size(self):
        return int(self.size)

    def get_capacity(self):
        return int(self.capacity)

    def get_species_array(self):
        if self.size <= 0:
            return None
        return self.species_array

    def get_stats(self, species):
        if species in self.species_array:
            ind = self.species_array.index(species)
            return [self.species_array[ind].get_attack(), self.species_array[ind].get_defense(), self.species_array[ind].get_speed()]
        return None

    def sort_pakuri(self):
        self.species_array.sort()
        return "Pakuri have been sorted!\n"

    def add_pakuri(self, new_species):
        if self.size >= self.get_capacity():  # Room left for new pakuri.
            print("Error: Pakudex is full!")
            return False

        if self.does_pakuri_exist(new_species):  # Is not duplicate Species
            return False

        if not new_species:  # valid string, not just empty.
            return None

        self.species_array.append(Pakuri(new_species))
        self.size += 1
        return True

    def evolve_species(self, species):
        species = self.does_pakuri_exist(species)

        if species:  # Does Species exist in Pakudex
            species.evolve()
            return True
        return False

    ########-------------########
    ########   Helpers   ########
    ########-------------########

    def does_pakuri_exist(self, species_to_check):

        if self.get_size() <= 0:
            return False

        for spec in self.get_species_array():
            if spec.species == species_to_check:
                return spec;

        return False

    ########-------------------------########
    ######## Hexadecimal Conversions ########
    ########-------------------------########

    def hex_char_decode(self, digit):
        # Determine if digit is decimal numeric
        if 48 <= ord(digit) <= 57:
            return int(digit)

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

        return 15

    def hex_string_decode(self, hex):
        value = 0

        # Format provided hex if needed
        hex = hex.upper()

        if hex[0:2] == "0X":
            hex = hex[2:len(hex) + 1]

        current_term = len(hex) - 1

        for char in hex:
            value += 16 ** current_term * self.hex_char_decode(char)
            current_term -= 1

        return value
