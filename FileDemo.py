from tokenize import maybe


my_file = open('test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# reads multiple line in file till end of file and create list
# print(my_file.readlines())
# print(my_file.readline())  # read single in a file

# my_file.close()

with open('test.txt', mode='w') as my_file:
    text = my_file.write('hey it\'s me')
    print(text)
