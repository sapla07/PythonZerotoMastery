def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fibonacci(10):
    print(x)

fibonacci(10)
# 0 1 1 2 3 5 8
