class Toy:

    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return('Yess??')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())  # calling class Toy instance
print(action_figure['name'])

print('************************************')


class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
