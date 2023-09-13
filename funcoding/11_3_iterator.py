"""
반복자(iterator)

- 하나 이상의 항목이 포함되어 있는 자료구조에서 데이터를 순차적으로 꺼내어 이용할 수 있는 객체를 반복자 객체라고 함
- 순차적으로 꺼낼 때 next() 함수 혹은 객체의 __next__() 메소드 사용 가능
- 반복가능 자료형은 iter() 함수를 사용하여 반복자 객체로 변환 가능


"""

# 리스트가 반복가능 객체인가 검사
try:
    l = [10, 20, 30]
    iterator = iter(l)
except TypeError:
    print('list는 iterable 객체가 아닙니다.')
else:
    print('list는 iterable 객체입니다.')


# 튜플이 반복가능 객체인가 검사
try:
    t = (10, 20, 30)
    iterator = iter(t)
except TypeError:
    print('tuple은 iterable 객체가 아닙니다.')
else:
    print('tuple은 iterable 객체입니다.')


# 정수형이 반복가능 객체인가 검사
try:
    n = 100
    iterator = iter(n)
except TypeError:
    print('n은 iterable 객체가 아닙니다.')
else:
    print('n은 iterable 객체입니다.')


# all() : 반복 가능한 항목들이 모두 참일 때 참을 반환함
l1 = [1, 2, 3, 4]
l2 = [0, 2, 4, 6]
l3 = [0, 0, 0, 0]

print('all : ' , all(l1))
print('all : ' , all(l2))
print('all : ' , all(l3))

# any() : 임의의 반복 가능한 항목들 중에서 참이 하나라도 있을 경우 참을 반환함
print('any : ', any(l1))
print('any : ', any(l2))
print('any : ', any(l3))

# bool() : 값(리스트)을 부울 값으로 변환한다. 즉 리스트의 항목 유무를 True, False로 알려줌
print('bool : ', bool(l1))
print('bool : ', bool(l2))
print('bool : ', bool(l3))
