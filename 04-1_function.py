"""
#함수란 무엇인가?
 - 입력값을 가지고 어떤 일을 수행한 후 그 결과물을 내어 놓는 것이 함수가 하는 일
 - 반복적으로 사용되는 가치 있는 부분을 한 뭉치로 묶어 어떤 입력값을 주었을 떄 어떤 결과값을 리턴해 주는 방식으로 사용

#파이썬 함수의 구조
def 함수이름(매개변수):
 수행할 문장1
 수행할 문장2
 ...
"""

# Sample - 함수의 이름은 add이고 입력으로 2개의 값을 받으며 리턴값(출력값)은 2개의 입력값을 더한 값이다.
def add(a, b):
    return a + b

a, b = 3, 4
c = add(a, b)
print(c)

# 매개변수와 인수
# 매개변수 = parameter, 인수 = arguments

# def add(a, b):     -> a, b 는 매개변수(parameter)
#     return a + b
# print(add(3,4))    -> 3, 4 는 인수

"""
#여러 개의 입력값을 받는 함수 만들기
def 함수이름(*매개변수):
 수행할 문장
 ...

"""
# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3))
print(add_many(1,2,3,4,5))

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1,2,3)
print(result)

result = add_mul('mul', 2,2,2)
print(result)

#키워드 매개변수, kwargs
# 매개변수 이름 앞에 **을 붙이면 매개변수는 딕셔너리가 되고 모든 Key=Value형태의 입력값이 그 딕셔너리에 저장된다.
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

#함수의 리턴값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result) # 결과값으로 (7, 12)라는 튜플 값을 가지게 된다.

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print('나의 이름은 %s 입니다.' % name)
    print('나이는 %d살 입니다.' % old)
    if man:
        print('남자입니다')
    else :
        print('여자입니다')

say_myself('Shiu', 7)
say_myself('Sara', 15, False)


# lambda 예약어
# lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.
# 보통 함수를 한 줄로 간결하게 만들 때 사용한다.
# 사용법
# 함수이름 = lambda 매개변수1, 매개변수2, ...: 매개변수를 이용한 표현식

add = lambda a, b: a + b
result = add(5, 6)
print(result)

mul = lambda a, b: a * b
result = mul(7, 8)
print(result)
