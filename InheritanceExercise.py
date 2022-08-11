class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Moyi(Cat):
    def sing(self, sounds):
        return f'{sounds}'


myCats = [Simon('Simon', 10), Sally('Sally', 8), Moyi('Moyi', 9)]

my_pets = Pets(myCats)

my_pets.walk()
