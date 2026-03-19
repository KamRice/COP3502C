from pakuri import Pakuri


class Pakudex:
    def __init__(self, _capacity=20):
        self.capacity = _capacity
        self.size = 0
        self.species_array = []

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        return self.species_array

    def get_stats(self, species):
        if species in self.species_array:
            return [self.species_array[species].get_attack(), self.species_array[species].get_defense(), self.species_array[species].get_speed()]
        return None

    def sort_pakuri(self):
        self.species_array.sort()

    def add_pakuri(self, species):
        if isinstance(species, Pakuri):
            self.species_array.append(species)

    def evolve_species(self, species):
        if self.species_array[species].evolve():
            return True
        return False
