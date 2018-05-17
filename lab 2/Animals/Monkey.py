from Animals.Animal import *
from enums.AnimalName import *


class Monkey(Animal):
    animal_name = AnimalName.MONKEY

    def __init__(self, amount_of_children, name, kind, age, weight, homeland, color, condition):
        self.amount_of_children = amount_of_children
        Animal.__init__(self, name, kind, age, weight, homeland, color, condition)

    def __str__(self):
        return "Name : " + str(self.name) + " kind: " + str(self.kind) + " the amount of children is " + str(self.amount_of_children)