import re

pattern = re.compile('this')

string = 'Search this inside of this text please! suyash'

a = pattern.search(string)
print(a)
b = pattern.findall(string)
print(b)
c = pattern.fullmatch(string)
print(c)
d = pattern.fullmatch(string)
print(d)