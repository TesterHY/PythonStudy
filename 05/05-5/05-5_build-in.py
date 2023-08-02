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