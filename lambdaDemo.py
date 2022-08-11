from functools import reduce

my_list = [1, 2, 3]
#syntax , lambda param : action(param)
print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc+item, my_list))


print('****************Exercise*****************')

# squares
my_list = [5, 4, 3]
print(list(map(lambda item: item*item, my_list)))

# List Sorting based on second item in tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
