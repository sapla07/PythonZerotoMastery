# Pure function definition
# 1 - It should give same output after running mulitple times
# 2 - It should affect program outside function
from functools import reduce
my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by_2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print('***************Map**********')
print(list(map(multiply_by_2, my_list)))
print('*************filter**********')
print(list(filter(only_odd, my_list)))
print('***************Zip**********')
print(list(zip(my_list, your_list)))
print('*************Reduce**********')
print(reduce(accumulator, my_list, 10))
# since Map doesn't affect/change outside my_list hence it behave like pure function
print(my_list)
