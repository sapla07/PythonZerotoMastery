# keys in dictionary must be immutable, we cant use a list [123] as key
# value will override if keys are duplicated in Dictionary

User = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user2 = dict(name='Sumeet')  # alternate way to create dictionary

print(user2)

print('age' in User.keys())
print('hello' in User.values())
print(User.items())
