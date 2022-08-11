import enum
from multiprocessing.reduction import duplicate


is_Friend = True
can_message = "message allowed" if is_Friend else "message not allowed"
print(can_message)


print(ord('a'))
print(ord('A'))
print('a' > 'A')

# short circuiting
# if one condition in OR operator is true, then OR ignore rest expression evaluation and directly execute action
# if one condition in and operator is false, then AND ignore rest expression evaluation and execute action inside block

is_Magician = True
is_expert = False

if is_Magician and is_expert:
    print("You are master magician")
elif is_Magician and not is_expert:
    print("Atleast, you're getting there")
else:
    print("you need magic power")

print(int('1') == 1)
# == checks for equality of value
# 'is' keyword check for location, since list [1,2,3] is at different memory space than [1,2,3] it return false

print('***************************************')
print('coding exercise')

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in mylist:
    sum += i

print(sum)
print('***************************************')

for _ in range(2):
    print(list(range(10)))
print('***************************************')

for i, num in enumerate(list(range(100))):
    if(num == 50):
        print(i)
print('***************************************')

i = 0
while(i < 50):
    print(i)
    i += 1
    if(i == 5):
        break
else:
    print("done all work")  # else only execute once while test condition fail
# If while terminate abnormally usig break statement, else will not execute
print('---------------------------------------')
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for pixel in picture:
    for num in pixel:
        if(num):
            print('*', end='')
        else:
            print(' ', end='')
    print('')

print('---------------------------------------')

my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for ele in my_list:
    if(my_list.count(ele) > 1):
        if ele not in duplicates:
            duplicates.append(ele)

print(duplicates)
