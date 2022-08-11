#Fundamentals Data Types

from numbers import Complex


int
float
bool
str
Complex #number
set
list
tuple
dict

#Classes -> Custom Types

#Specialized Data Types , example - Modules

None

print('*****************************')
print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2/4))

print(2 ** 3) #power
print(4 // 3) #returns Integer
print(6 % 4) #return remainder

#Operator Precedence
#()
#** (power)
#* /
# + -
print('*****************************')
print(bin(5)) #convert int to binary
print(int('0b101', 2)) #convert binary to int
print('*****************************')
#define constants using uppercase letter eg. PI = 3.14
#dont use double underscore, number at initials of variable

a,b,c= 1,2,3
print(a)
print(b)
print(c)

#augmented assignment operator
print('*****************************')
some_value = 5 #always initialise first while using augmented assignment operator
some_value += 2
print(some_value)


print('*****************************')
#Escape Sequences

weather = "\t It\'s \"kind of\" sunny \n hope you have good day!"
print(weather)

print('*****************************')
print('Formatted String')
name='jhon'
age=55

print(f'Hi {name}. You are {age} years old')
print('Hi {}. You are {} years old'.format(name, age))
print('Hi {1}. You are {0} years old'.format(name, age))
print('Hi {new_name}. You are {age} years old'.format(new_name='Shourya', age=43))

print(bool(None))