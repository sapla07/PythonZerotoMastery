# Higher Order functions are functions that accept the parameter and return function from a function
# example Map is Higher Order fucntion because it accepts function as parameter and so similarly
# filter and reduce also Higher Order function

# Decorator are simply a function that wraps another function and enhances or changes it
from time import time


def my_decorator(func):
    def wrap_func():
        print('**************')
        func()
        print('**************')
    return wrap_func


@my_decorator
def hello():
    print('Hello, I am Sumeet')


@my_decorator
def greet():
    print('How are you?')


# hello()
# greet()
# my_decorator(hello)() -> run this after removing @decorator from hello()

# enhanced decorators to accept parameters


def enhance_decorators(func):
    def wrap_func(*args, **kwargs):
        print('**************')
        func(*args, **kwargs)
        print('**************')
    return wrap_func


@enhance_decorators
def hello2(greeting, emoji=':)'):
    print(greeting, emoji)


# hello2('hiii')

print('******************UseFul Example**********************')


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i*5


long_time()
