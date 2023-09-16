"""
넘파이(NumPy)

- 파이썬의 과학계산을 위한 가장 기본적인 라이브러리
- 행렬, 벡터 연산을 위한 사실상의 표준 라이브러리로 빠른 처리속도가 장점
- 다차원 배열과 행렬 객체가 포함
- pip를 이용하여 cmd 명령행에서 다음과 같이 입력함
"""

import numpy as np

a = np.array([1, 2, 3])

print(a.shape)      # 객체의 형태
print(a.ndim)       # 객체의 차원
print(a.dtype)      # 객체 내부 자료형
print(a.itemsize)   # 객체 내부 자료형이 차지하는 메모리 크기
print(a.size)       # 객체의 전체 크기(항목의 수)


b = np.array([1, 2, 3], dtype='int32')
c = np.array([4, 5, 6], dtype=np.int64)

d = a + b
print(d.dtype)

print(a.max())  # 최대값
print(a.min())  # 최솟값
print(a.mean()) # 평균 값

print('---------------------')

# flatten() -  1차원으로
e = np.array([[1,1], [2,2], [3,3]])
print(e.flatten())

# append()
f = np.array([1, 2, 3])
g = np.array([[4,5,6],[7,8,9]])

print(np.append(f, g))
print(np.append([f], g, axis=0)) # [a]를 통해 2차원 배열로 만듬


# rand()
h = np.random.rand(3, 3) # (3,3) shape의 난수 생성(0~1)
print(h)

# randint()
i = np.random.randint(0, 10, size=10)
print(i)

# 연산
a = np.array([1,2,3])
b = np.array([4,5,6])
c = a + b # shape같을 경우 가능
print(c)

c = np.array([[1,2], [3,4]])
d = np.array([[10,20], [30,40]])

print(c + d)
print(c - d)
print(c * d)
print(c / d)

# 행렬 곱 matmul()
print(np.matmul(c, d))
print(c @ d)

# 2차원 ndarray의 사칙연산
e = np.array([[10,20], [30,40]])
print(e + 1)
print(e - 1)
print(e * 10)
print(e / 10)

# 1에서 9까지의 모든 정수 값을 크기 순서대로 가지는 3X3 크기의 행렬 a를 생성하고,
# 모든 성분의 값이 2인 3X3 크기의 행렬 b를 생성하라
a = np.arange(1, 10, 1).reshape(3,3)
print(a)
b = np.array([[2,2,2], [2,2,2], [2,2,2]])
print(b)

# ndarray의 생성
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.full((2, 3), 100))
print(np.eye(5))
print(np.random.random((2,3)))

# linspace()
print(np.linspace(0, 10, 5))
print(np.linspace(0, 10, 4))

print(np.full((3, 3), 2))


# ndarray의 재구성(reshape)
# np.arrange(0, 10).reshape(2, 5)
# 0~9 까지를 2행 5열의 다차원 행렬로 변환
a1 = np.arange(0, 10).reshape(2,5)
a2 = np.arange(0, 10).reshape(5,2)
print(a1)
print(a2)

# 3차원 배열
a3 = np.arange(0, 24).reshape(4, 3, 2) # 3행 2열이 4개
print(a3)

a4 = np.arange(6).reshape(3, 2)
print(a4)
print(np.transpose(a4)) # 전치; 행과 열을 바꿈

# 문제1.
# arange()함수를 사용하여 1에서 12까지의 원소를 가지는 1차원 배열 a1을 생성하여라.
# 그리고 이 a1 배열을 reshape() 메소드를 사용하여 2행 6열의 행렬로 재구성하여라.
a1 = np.arange(1, 13)
print(a1)

a1 = a1.reshape(2, 6)
print(a1)

# 문제2.
# arange() 함수를 사용하여 1에서 30까지의 원소를 가지는 1차원 배열 a2를 생성하여라.
# 그리고 이 a2 배열을 reshape()메소드를 사용하여 3행 10열의 행렬로 재구성하여라.
a2 = np.arange(1, 31)
print(a2)

a2 = a2.reshape(3, 10)
print(a2)

# 다차원 배열의 축
# 1차원 : 가로, 2차원 : 가로, 세로, 3차원 : 가로, 세로, 높이
# axis0 : ↓、axis1 : →

b = np.arange(0, 6).reshape(3, 2)
print(b)
print(b.sum()) # 행렬의 모든 원소의 합
print(b.sum(axis=0)) # 0축 방향 원소의 합
print(b.sum(axis=1)) # 1축 방향 원소의 합

# 0축 방향 원소의 최솟값
print(b.min(axis=0))

# 1축 방향 원소의 최솟값
print(b.min(axis=1))

# 0축 방향 원소의 최댓값
print(b.max(axis=0))

# 1축 방향 원소의 최댓값
print(b.max(axis=1))

# insert() 함수
c = np.array([1, 3, 4])
print(c)
c = np.insert(c, 1, 2) # c의 1번째 인덱스에 2를 입력한 것을 c에 대입
print(c)

c = np.array([[1,1], [2,2], [3,3]])
print(c)

c = np.insert(c, 1, 4, axis=0) # y축
print(c)

c = np.insert(c, 1, 4, axis=1) # x축
print(c)


# 문제1.
# 1에서 100까지의 랜덤 정수 15개를 np.random.randint()를 통해서 생성하여라.
# 이렇게 생성한 정수 값들을 (3, 5)의 shape을 가지는 행렬 a에 다음과 같이 저장하여 출력하여라.
q1 = np.random.randint(0, 100, 15).reshape(3, 5)
print(q1)

# 문제2.
# 문제1에서 생성한 행렬에 대한 열방향의 최댓값, 최솟값, 평균을 출력
q1_max_0 = q1.max(axis=0)
q1_min_0 = q1.min(axis=0)
q1_avg_0 = q1.mean(axis=0)

print('열방향 최댓값 : ', q1_max_0)
print('열방향 최솟값 : ', q1_min_0)
print('열방향 평균 : ', q1_avg_0)

# 문제3.
# 문제1에서 생성한 행렬에 대한 행방향의 최댓값, 최솟값, 평균을 출력
q1_max_1 = q1.max(axis=1)
q1_min_1 = q1.min(axis=1)
q1_avg_1 = q1.mean(axis=1)

print('행방향 최댓값 : ', q1_max_1)
print('행방향 최솟값 : ', q1_min_1)
print('행방향 평균 : ', q1_avg_1)


### 배열의 인덱싱과 슬라이싱
# 1차원 배열의 인덱싱
a = np.array([1, 2, 3])
print(a[0], a[1], a[2])
print(a[-1], a[-2], a[-3])

print('--------------------------')
# 1차원 배열에서 여러 개의 원소를 인덱싱하기
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a[np.array([0, 1])])
print(a[np.array([0, 2, 4])])

print('--------------------------')
# 넘파이의 슬라이싱
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(a)
print(a[1:5]) # 슬라이싱 구간[시작:끝] 인덱스
print(a[1:]) # 1번 인덱스부터 끝까지
print(a[:]) # 전체를 슬라이싱
print(a[::2]) # 양수 2의 스텝
print(a[::-1]) # 음수 1의 스텝

print('--------------------------')
# 문제1.
# 1에서 10까지의 원소를 가지는 1차원 배열 a를 생성하여라.
# 이 a를 인덱싱하여 [2, 4, 6, 8]의 원소를 가진 배열 b를 생성하여 다음과 같이 출력
a = np.arange(1, 11)
b = a[np.array([1, 3, 5, 7])]
c = np.array([ a[i] for i in range(len(a))
              if i % 2 == 1
              if i < len(a) - 1
              ])
print(a)
print(b)
print(c)


print('--------------------------')
# 문제2.
# 문제 1에서 생성한 배열 a를 슬라이싱하여 다
# 다음과 같은 배열 b, c, d, e, f를 생성
"""
b = [6 7 8 9 10]
c = [7 8 9 10]
d = [1 2 3]
e = [1 3 5 7 9]
f = [10 8 6 4 2]
"""

a = np.arange(1, 11)
print('a ', a)
print('b ', a[5:])
print('c ', a[6:])
print('d ', a[:3])
print('e ', a[::2])
print('f ', a[::-2])


print('--------------------------')
# 2차원 배열의 인덱싱
a = np.arange(0, 6).reshape(3, 2)
print(a)
print(a[0,0])
print(a[1,1])

print('--------------------------')
# 3차원 배열의 인덱싱

# 깊이4, 행3, 열2
a = np.arange(0, 24).reshape(4, 3, 2)
print(a)
print(a[3, 1, 1])


print('--------------------------')
# 3차원 배열의 인덱스와 concatenate()함수

a = np.arange(0, 24).reshape(4, 3, 2)
print(a)

print(a[0])
print(a[0, 0])
print(a[0, 2])
print(np.concatenate((a[0, 0], a[0, 2]), axis=0))


print('--------------------------')
# 문제 1.
# (4,3,2) 형태의 3차원 배열을 다음과 같이 인덱스와 원소값이 나타나도록
# 출력

a = np.arange(0, 24).reshape(4, 3, 2)

print('{:13s}{:5s}'.format('index', 'element'))

for i in np.ndindex(a.shape):
    print('{}{:7d}'.format(i, a[i]))

print('--------------------------')
# 문제2
# concatenate()함수 사용하여 배열만들기
a = np.arange(0, 24).reshape(4, 3, 2)
print(a)


# array([0, 1, 6, 7])
print(np.concatenate((a[0,0], a[1, 0]), axis=0))

# array([0, 1, 14, 15])
print(np.concatenate((a[0,0],a[2,1]), axis=0))

print(np.concatenate((a[0], a[1]), axis=0))

print(np.concatenate((a[0], a[1]), axis=1))

print('--------------------------')
## 2차원 배열의 슬라이싱
a = np.arange(0, 9).reshape(3, 3)
print(a)

print(a[0])         # 0번째 행의 모든 요소
print(a[1, :])      # 1번째 행의 모든 요소
print(a[:, 1])      # 1번째 열의 모든 요소
print(a[0, 0:2])    # 0번째 행의 0열, 1열 요소
print(a[0, :2])     # 0번째 행의 <2 까지 열 요소

# 2 x 2 배열 얻기
print(a[0:2, 0:2])
print(a[1:, 1:])


print('--------------------------')
# 문제1.
# 0에서 15까지의 연속적인 값을 원소로 가지는 4x4크기의 2차원 배열 a를 생성
# 이 a에 대하여 인덱싱과 슬라이싱을 적용하여 다음과 같은 b, c, d, e 배열을 구하여라

a = np.arange(16).reshape(4, 4)
print(a)

# b = [ 1 5 9 13]
print('b ', a[:, 1])

# c = [ 9 10 11 ]
print('c ', a[2, 1:])

# d = [[ 0 1] [ 4 5]]
print('d ', a[:2, :2])

# e = [[ 5 6] [ 9 10]]
print('e ', a[1:3, 1:3])

# 문제2.
# 문제 1에서 생성한 배열 a를 슬라이싱하고 평탄화 연산을 하여
# 다음과 같은 배열 f, g, h를 생성하여라

# f = [ 0 1 2 4 5 6 ]
print('f ', a[0:2, 0:3].flatten())

# g = [ 8 9 10 11 12 13 14 15 ]
print('g ', a[2:, :].flatten())

# h = [ 5 6 7 13 14 15 ]
print('h ', np.concatenate((a[1, 1:], a[3, 1:])).flatten())
