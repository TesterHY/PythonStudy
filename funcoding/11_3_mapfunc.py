"""
맵함수(map function)

반복 가능한 자료형의 각 요소들에 대해서 지정된 매핑 함수를 적용하여 반복 가능한 자료형을 반환

"""

# 리스트의 append()를 이용한 제곱값 리스트 생성

a = [1, 2, 3, 4, 5, 6, 7]
square_a1 = []

for n in a :
    square_a1.append(n**2)

print(square_a1)


def square(x):
    return x**2

square_a2 = []

square_a2 = list(map(square, a))
print(square_a2)


square_a3 = []
square_a3 = list(map(lambda x : x ** 2, a))
print(square_a3)
