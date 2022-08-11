'''
def sum(num1, num2):
    def another_func(n1, n2):
        return n1+n2
    return another_func(num1, num2)

print(sum(10,20))
'''


def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(18)


def test(a):
    '''
    Info: test and print params
    '''
    print(a)


help(test)
'or'
# It print comment which is inside function, this is called as docSign
print(test.__doc__)


# *args (as many params as we want), **kwargs
# rule: params, args, default params , kwargs
# *args - return tuple
# **kwargs - return dictionary
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('Andy', 1, 2, 3, 4, 5, num1=5, num2=10))


def highest_even(li):
    max = 0
    for ele in li:
        if(ele % 2 == 0):
            if(ele > max):
                max = ele
    return max


print(highest_even([10, 2, 3, 4, 8, 11]))


# walrus operator ( := ) ->  assign values to variable as part of larger experssion
print('-----------------------------------------')
greet = 'SumeetSapla'

if((n := len(greet)) > 10):
    print(f'name has {n} letters')

while((n := len(greet)) > 1):
    print(n)
    greet = greet[:-1]

print(greet)
