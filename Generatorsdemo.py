# Every iterable is not generator but every generators are iterable

from typing import Iterator


def generator_func(num):
    for i in range(num):
        yield i*2


# for item in generator_func(20):
#    print(item)


g = generator_func(10)
next(g)
print(next(g))
print(next(g))

# Generator under the hood


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break


special_for([1, 2, 3])
