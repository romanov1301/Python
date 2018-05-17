class Zoo:
    animals = []

    def __init__(self):
        pass

    def sort_by_kind(self):
        self.animals.sort(key=lambda animal: animal.kind)

    def find_by_age(self, age):
        if age > 5:
            found_animals = []

        for animal in self.animals:
            if animal.age == age:
                found_animals.append(animal)

        return found_animals

    def add_animal(self, animal):
        self.animals += animal

    def print_list(self):
        for animal in self.animals:
            print(animal)
        print("\n")