class Pakuri:
    def __init__(self, _species):
        self.species = _species
        self.attack = (len(self.species) * 7) + 9
        self.defense = (len(self.species) * 5) + 17
        self.speed = (len(self.species) * 6) + 13

    def get_species(self):
        return self.species

    def get_attack(self):
        return int(self.attack)

    def get_defense(self):
        return int(self.defense)

    def get_speed(self):
        return int(self.speed)

    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3
        return True

    ########-------------########
    ########  Overrides  ########
    ########-------------########

    def __lt__(self, other):
        return self.species < other
    def __gt__(self, other):
        return self.species > other
    def __eq__(self, other): #I'm not really using this overide currently. But I dont really want to touch this and break anything.
        return self.species == other

