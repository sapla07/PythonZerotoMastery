from functools import reduce

# 1 Capitalize all of the pet names and print the list
print('*************Map***********************')
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capital_pets(item):
    return item.capitalize()


print(list(map(capital_pets, my_pets)))
# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
print('*************Zip***********************')
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
#sorted_my_numbers = sorted(my_numbers)
print(list(zip(my_strings, sorted(my_numbers))))

# 3 Filter the scores that pass over 50%
print('*************Filter***********************')
scores = [73, 20, 65, 19, 76, 100, 88]


def score_filter(item):
    return item > 50


print(list(filter(score_filter, scores)))
# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print('*************Reduce***********************')


def calculate_total(acc, item):
    return acc+item


print(reduce(calculate_total, my_numbers+scores, 0))
