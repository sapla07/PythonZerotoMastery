class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


Cat1 = Cat('Rini', 10)
Cat2 = Cat('Shiri', 12)
Cat3 = Cat('Snowy', 8)

catList = [Cat1.age, Cat2.age, Cat3.age]


def OldCat(age):
    return max(age)


print(OldCat(catList))
