"""
##파이썬 내장함수

"""

# abs : 어떤 숫자를 입력받았을 때 그 숫자의 절댓값을 리턴하는 함수
a1 = abs(3)
a2 = abs(-3)
a3 = abs(-1.2)

print(a1, a2, a3)

# all : 
# 반복 가능한 데이터 x를 입력값으로 받으며 이 x의 요소가 모두 참이면 True,
# 거짓이 하나라도 있으면 False를 리턴한다.

b1 = all([1, 2, 3])
b2 = all([1, 2, 3, 0]) # 0은 거짓이므로 False 반환
print(b1, b2)

# any : 
# 반복 가능한 데이터 x를 입력값으로 받으며 이 x의 요소 중 하나라도 참이 있으면 True,
# x가 모두 거짓일 때만 False를 리턴한다. all() 반대.
c1 = any([1, 2, 3, 0])
c2 = any([0, ""]) # 모두 거짓이므로 False 반환
print(c1, c2)

# chr : 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수이다.
print(chr(97))
print(chr(44032))

# dir : 객체가 지닌 변수나 함수를 보여주는 함수이다.
#print(dir([1,2,3]))
#print(dir({'1':'a'}))
#print(dir())

# divmod : 2개의 숫자 a, b를 입력으로 받는다. 그리고 a를 b로 나눈 몫과 나머지를 튜플로 리턴
d1 = divmod(7, 3)
print(d1)

# enumerate : 
# 순서가 있는 데이터(리스트, 튜플, 문자열)을 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
l1 = ['body', 'foo', 'bar']
for i, name in enumerate(l1):
    print(i, name)

# eval : eval(expression)은 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴
e1 = eval('1+2')
e2 = eval("'hi' + 'a'")
print(e1, e2)

# filter : 필터란 '무엇인가를 걸러 낸다'라는 뜻으로 이와 비슷한 기능을 한다.
# filter(함수, 반복 가능한 데이터)
def positive(l):
    result = []
    for i in l:
        if i > 0 :
            result.append(i)
    return result

l2 = [1, -3, 2, 0, -5, 6]
print(positive(l2))
print(l2)

def positive2(x):
    return x > 0

print(list(filter(positive2, l2)))

# hex : 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 리턴하는 함수
print(hex(234))
print(hex(3))

# id : 객체를 입력받아 객체의 고유 주솟값(레퍼런스)를 리턴하는 함수
i1 = 3
print(id(i1))

i2 = i1
print(id(i2))

# input : 사용자 입력을 받는 함수. 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.
#j1 = input("Enter : " )
#print(j1)

# int : 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수이다.
# 만약 정수가 입력되면 그대로 리턴한다.

print(int('3'))
print(int(3.4))

# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다.
# 예를 들어 2진수 '11'의 10진수 값은 아래와 같다
print(int('111', 2))
print(int('11', 16))

# isinstance : isinstance(object, class) 함수는 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받는다.
# 입력으로 받은 객체가 그 클래스의 인스터스인지를 판단하여 참이면 True, 거짓이면 False를 리턴한다.
class Person: pass

p1 = Person()
p2 = 3
print(isinstance(p1, Person))
print(isinstance(p2, Person))

# len : len(s) 는 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다.
len1 = 'Hello'
len2 = [1, 2, 3]
print(len(len1))
print(len(len2))

# list : list(iterable)은 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴하는 함수이다.
print(list('Hello World'))

# map : map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
def two_times1(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result1 = two_times1([1, 2, 3, 4])
print(result1)

def two_times2(x):
    return x * 2

result2 = list(map(two_times2, [1, 2, 3, 4]))
print(result2)

result3 = list(map(lambda a: a*2, [1, 2, 3, 4]))
print(result3)

# max : max(iterable)은 인수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴하는 함수이다.
m1 = [1, 3, 5]
print(max(m1))

# min : min(iterable)은 인수로 반복 가능한 데이터를 입력받아 그 최솟값을 리턴하는 함수이다.
m2 = [2, 4, 6]
print(min(m2))

# oct : oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수이다.
print(oct(34))
print(oct(12345))

# open : open(filename, [mode])은 '파일 이름'과 '읽기 방법'을 입력받아 파일 객체를 리턴하는 함수이다.
# 읽기 방법을 생략하면 기본값인 읽기 모드(r)로 파일 객체를 만들어 리턴한다.
# 쓰기모드 - w 
# 읽기모드 - r 
# 추가모드 - a 
# 바이너리모드 - b : b는 w, r, a와 함꼐 사용한다. 예를 들어 rb는 바이너리 읽기 모드를 의미한다.

# ord : ord(x)는 문자의 유니코드 숫자 값을 리턴하는 함수이다.
# ord 함수는 chr 함수와 반대로 동작한다.
print(ord('a')) 
print(chr(97)) 

# pow : pow(x, y)는 x를 y제곱한 결괏값을 리턴하는 함수이다.
print(pow(2, 3))

# range : range([start,] stop [,step])은 for 문과 함께 자주 사용하는 함수이다.
# 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴한다.
# 인수가 하나일 경우
r1 = list(range(10))
print(r1)

# 인수가 두개일 경우
r2 = list(range(10, 20))
print(r2)

# 인수가 세개일 경우
r3 = list(range(10, 30, 3))
print(r3)

# round : round(number, [, ndigits])는 숫자를 입력받아 반올림해 리턴하는 함수이다.
r4 = round(3.54)
r5 = round(3.14)
print('r4 : ', r4, ', r5 : ', r5)

# sorted : sorted(iterable)은 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.
s1 = [3, 4, 1, 6, 9, 2]
print(sorted(s1))
print(sorted(s1, reverse=True))
print(sorted('sea'))

# str : str(object)는 문자열 형태로 객체를 변환하여 리턴하는 함수이다.
s2 = 12345
print(type(s2))

s2 = str(s2)
print(type(s2))

# sum : sum(iterable)은 입력 데이터의 합을 리턴하는 함수이다.
ss1 = [1, 2, 3, 4, 5]
print(sum(ss1))

# tuple : tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다.
t1 = "abc"
print(tuple(t1))

t2 = [1, 2, 3, 4, 5]
print(tuple(t2))

t3 = (1, 2, 3, 4, 5)
print(tuple(t3))

# type : type(object)는 입력값의 자료형이 무엇인지 알려 주는 함수이다.
print(type(123))
print(type('안녕'))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1:'a', 2:'b'}))
print(type(set(['Hello'])))

# zip : zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수이다.
z1 = [1, 2, 3]
z2 = [4, 5, 6]
z3 = [7, 8, 9]
print(list(zip(z1, z2, z3)))
