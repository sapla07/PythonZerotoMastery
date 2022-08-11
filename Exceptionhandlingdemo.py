

from decimal import DivisionByZero
from multiprocessing.sharedctypes import Value


while True:
    try:
        age = int(input('What is your age?'))
        10/age
        print(age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('Enter number greater than 0')
    else:
        print('Thank you!')
        break


def sum(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum(1, 0))
