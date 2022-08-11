# list, set, dictionary  comprehensions

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

print('alernate of above progrm')
# list = [param for param in iterable]

my_clist = [char for char in 'hello']
print(my_clist)

my_numlist = [num**2 for num in range(0, 10)]
print(my_numlist)

my_evenlist = [num**2 for num in range(0, 10) if num % 2 == 0]
print(my_evenlist)

print('****************Dictionary comprehension********************')

simple_dict = {'a': 1, 'b': 2}

my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)

just_dict = {num: num*2 for num in [1, 2, 3]}
print(just_dict)
