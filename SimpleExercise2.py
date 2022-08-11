Name = input('Enter your name')
Password = input('Enter your Secret Password')

printpass = '*' * len(Password)

print(f'{Name}, your secret password {printpass} is {len(Password)} letter long')
