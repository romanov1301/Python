from Animals.Animal import *
from enums.AnimalName import *


class Lion(Animal):
    animal_name = AnimalName.LION

    def __init__(self, length_of_tail, name, kind, age, weight, homeland, color, condition):
        self.length_of_tale = length_of_tail
        Animal.__init__(self, name, kind, age, weight, homeland, color, condition)

    def __str__(self):
        return "Name : " + str(self.name) + " kind: " + str(self.kind) + " the length of tail is " + str(self.length_of_tale)