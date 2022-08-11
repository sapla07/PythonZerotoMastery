from unicodedata import name


class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, man, power, email):
        super().__init__(email)  # calling parent init
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, man, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows_left - {self.num_arrows}')


Wizard1 = Wizard('Sumeet', 24, 'sumeet@gmail.com')
Archer1 = Archer('Robin', 100)
print(Wizard1.sign_in())
print(Wizard1.email)


def player_attack(char):
    char.attack()


player_attack(Wizard1)
player_attack(Archer1)

print('OR')

for char in [Wizard1, Archer1]:
    char.attack()
