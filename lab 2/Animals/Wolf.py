from Animals.Animal import *
from enums.AnimalName import *


class Wolf(Animal):
    animal_name = AnimalName.WOLF

    def __init__(self, length_of_fur, name, kind, age, weight, homeland, color, condition):
        self.length_of_fur = length_of_fur
        Animal.__init__(self, name, kind, age, weight, homeland, color, condition)

    def __str__(self):
        return "Name : " + str(self.name) + " kind: " + str(self.kind) + " the length of fur is " + str(self.length_of_fur)