"""
튜플 자료형

- 리스트는 [], 튜플은 () 으로 둘러싼다.
- 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.

"""

# 튜플 생성
t1 = ()
t2 = (1,) # 1개의 요소만을 가질 때는 요소 뒤에 쉼표(,)를 반드시 붙여야 함
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 소괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))

print(t1, t2, t3, t4, t5)

# 1. 튜플 요솟값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
# del t1[0] # 에러 발생
# t1[0] = 'c' # 에러 발생

# 인덱싱하기
t1 = (1, 2, 'a', 'b')
print(t1[0])

# 슬라이싱하기
t1 = (1, 2, 'a', 'b')
print(t1[1:])

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = 3, 4
t3 = t1 + t2
print(t3)

# 튜플 곱하기
t4 = (3,)
print(t4 * 3)

# 튜플 길이 구하기
t5 = ('a', 'b', 1, 2, 3)
print(len(t5))
