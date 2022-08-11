
# Rule of Scope in order
# 1 - start with local
# 2 - Parent local
#3 - Global
# 4 - built in python functions


a = 1


def start():
    a = 5
    return a


print(start())
print(a)
print('----------------------------------')


def parent():
    a = 10

    def child():
        return a
    return child()


print(parent())
print(a)
print('----------------------------------')


def Head():
    def tail():
        return a
    return tail()


print(Head())
print(a)
print('----------------------------------')


def Top():
    def Bottom():
        return sum
    return Bottom()


print(Top())
print(a)


# global keyword example
print('----------------------------------')
total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))
print('----------------------------------')

total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())

# nonlocal example - where inner func duplicate variable replace outer func (parent func) variable
print('----------------------------------')


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
