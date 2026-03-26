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
        return self.species_array

    def get_stats(self, species):
        if species in self.species_array:
            return [self.species_array[species].get_attack(), self.species_array[species].get_defense(), self.species_array[species].get_speed()]
        return None

    def sort_pakuri(self):
        self.species_array.sort()
        return "Pakuri have been sorted!"

    def add_pakuri(self, new_species):
        if self.size >= self.get_capacity():  # Room left for new pakuri.
            return "Error: Pakudex is full!"

        if self.does_pakuri_exist(new_species):  # Is not duplicate Species
            return "Error: Pakudex already contains this species!"

        if not new_species:  # valid string, not just empty.
            return None

        self.get_species_array().append(Pakuri(new_species))
        self.size += 1
        return f"Pakuri species {new_species} successfully added!"

    def evolve_species(self, species):
        species = self.does_pakuri_exist(species)

        if species:  # Does Species exist in Pakudex
            species.evolve()
            return f"{species.species} has evolved!"
        return "Error: No such Pakuri!"

    # Helpers #
    def does_pakuri_exist(self, species_to_check):

        if self.get_size() <= 0:
            return False

        for spec in self.get_species_array():
            if spec.species == species_to_check:
                return spec;

        return False
