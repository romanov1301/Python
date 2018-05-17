from Animals.Lion import *
from Animals.Wolf import *
from Zoo import *
from Animals.Monkey import *
from Animals.Bear import *


if __name__ == '__main__':
    zoo = Zoo()

    lion = Lion(0.6, "Mark", "Indian", 5, 84, "India", "brown", "healthy")
    wolf = Wolf(0.1, "Leo", "Mexican", 7, 70, "Mexica", "grey", "healthy")
    monkey = Monkey(2, "Molly", "African", 4, 32, "Africa", "brown", "healthy")
    bear = Bear(2.1, "Tedd", "White", 12, 104, "Antarctica", "white", "healthy")

    zoo.animals = [lion, wolf, monkey, bear]
    print("Previous list:")
    zoo.print_list()

    zoo.sort_by_kind()
    print("Sorted list")
    zoo.print_list()