"""
자료형의 값을 저장하는 공간, 변수

- 변수란?
  파이썬에서 사용하는 변수는 객체를 가리키는 것이라고도 말할 수 있다.
  객체란 자료형의 데이터(값)와 같은 것을 의미하는 말이다.

  변수가 가리키는 메모리의 주소는 id() 함수를 사용해 확인 할 수 있다.
"""

# 변수 생성
a = 1
b = 'python'
c = [1, 2, 3]

# 리스트를 복사하고자 할 때
a = [1, 2, 3]
b = a

# a, b가 [1, 2, 3]이라는 리스트 객체를 참조하고 있다.
print(id(a))
print(id(b))
print(a is b)

a[1] = 9 # a[1]를 변경하면 b도 똑같이 변경됨 -> a, b 모두 같은 리스트 객체를 참조하고 있기 때문
print(a)
print(b)

### 다른 주소를 가리키도록 생성하기
#1. [:] 이용하기
a = [1, 2, 3]
b = a[:] # a리스트 요솟값 전체를 b에 대입

a[1] = 9
print(a)
print(b)

#2. copy 모듈 이용하기
from copy import copy
a = [4, 5, 6]
b = copy(a)
print(a is b)

#2-1. 리스트 자료형의 copy함수 이용하기
c = [1, 3, 5]
d = c.copy()
print(d is c)



### 변수를 만드는 여러 가지 방법
# 튜플로 a, b에 값을 대입
a, b = ('hello', 'python')
print(a, b)

# 위와 완전 동일
(c, d) = 'hello', 'python'
print(c, d)

# 리스트로 변수 만들기
[a, b] = ['python', 'hello']
print(a)
print(b)

# 여러 개의 변수에 같은 값을 대입
a = b = 'python'
print(a, b)

# 두 변수의 값을 바꾸기
a = 3
b = 5
a, b = b, a
print(a, b)
