#if문 
"""
기본 구조

if 조건문:
 수행할 문장1
 수행할 문장2
 ...
else
 수행할 문장3
 수행할 문장4
 ...

-> 인덴트 중요!
"""

### 비교 연산자
"""
x < y : x가 y보다 작다.
x > y : x가 y보다 크다.
x == y : x와 y가 같다.
x != y : x와 y가 같지 않다.
x >= y : x가 y보다 크거나 같다.
x <= y : x가 y보다 작거나 같다.
"""

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
if money >= 3000 :
    print('택시를 타고 가라')
else:
    print('걸어가라')


# and, or, not
"""
x or y : x와 y 둘 중 하나만 참이어도 참이다.
x and y : x아 y 모두 참이어야 참이다.
not x : x가 거짓이면 참이다.
"""

# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
card = True
if money or card:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# in, not in
"""
x in 리스트, x not in 리스트
x in 튜플, x not in 튜플
x in 문자열, x not in 문자열
"""
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])


# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타고 가라')
else:
    print('걸어가라')

# pass - 아무 일도 하지 않게 설정하고 싶을 때
# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')

# 한줄로 작성하기
if 'money' in pocket: pass
else: print('카드를 꺼내라')



# elif - 다양한 조건
# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('택시를 타고 가라')
elif card:
    print('택시를 타고 가라')
else:
    print('걸어가라')

### 조건보 표현식
# score가 60 이상일 경우 message에 success, 아닐 경우 failure
score = 70
message = ''
if score >= 60:
    message = 'success'
else:
    message = 'failure'
print(message)

# 조건부 표현식(conditional expression)으로 표현
message = 'success' if score >= 60 else 'failure'
print(message)
