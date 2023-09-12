def add1(x, y):
    return x+y
print(add1(100, 200))

add2 = lambda x, y: x+y
print(add2(100, 200))

print((lambda x, y: x+y)(100, 200))


def sub(a, b):
    return a-b

# 일반적으로 
print('{} - {} = {}'.format(200, 100, sub(200, 100)))

# 람다 함수
print('{} - {} = {}'.format(200, 100, (lambda a, b: a-b)(200,100)))