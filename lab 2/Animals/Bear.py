from Animals.Animal import *
from enums.AnimalName import *


class Bear(Animal):
    animal_name = AnimalName.BEAR

    def __init__(self, height, name, kind, age, weight, homeland, color, condition):
        self.height = height
        Animal.__init__(self, name, kind, age, weight, homeland, color, condition)

    def __str__(self):
        return "Name : " + str(self.name) + " kind: " + str(self.kind) + " the height is " + str(self.height)