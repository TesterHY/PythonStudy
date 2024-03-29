"""
집합 자료형

집합(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형이다.

"""

### 집합 자료형 생성
s1 = set([1, 2, 3])
print(s1)

# 집합 자료형의 특징
"""
 중복을 허용하지 않는다.
 순서가 없다.

 - 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 요솟값을 얻을 수 있지만,
   set 자료형은 순서가 없기 때문에 인덱싱을 통해 요솟값을 얻을 수 없다.
   만약, set 자료형에 저장돈 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후에 해야 한다.
"""
s2 = set("Hello")
print(s2)

s1 = ([1, 2, 3])
l1 = list(s1)
t1 = tuple(s1)

print('s1 : ' + str(s1) + ', l1[0] : ' + str(l1[0]) +  ', t1[1] : ' + str(t1[1]))


### 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])


# 교집합 구하기 - &
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 구하기 - |
print(s1 | s2)
print(s1.union(s2))

# 차집합 구하기 - -
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))


### 집합 자료형 관련 함수
# 값 1개 추가하기 - add
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러개 추가하기 - update
s1.update([5, 6, 7])
print(s1)

# 특정값 제거하기 - remove
s1.remove(3)
print(s1)
