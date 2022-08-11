class PlayerCharacter:
    # class object attribute
    membership = True

    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age

    def run(self):
        return self

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1+num2


Player1 = PlayerCharacter('Sumeet', 26)
Player2 = PlayerCharacter('Chirag', 24)
Player3 = PlayerCharacter.adding_things(2, 3)
Player2.attack = 50

print(Player1.name)
print(Player2.age)
print(Player1.run().run())
print(Player2.attack)
# return true , It is Class level attribute used by any object
print(Player1.membership)
print(Player2.membership)  # return true

#print(PlayerCharacter.adding_things(4, 5))
# print(Player1.adding_things(3,4))
# we can also create or instantiate object using class method
print(Player3.age)
