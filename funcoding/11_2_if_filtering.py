"""
if 조건식을 이용한 필터링

"""

ages = [34, 39, 20, 18, 13, 54]

# list()함수, filter()함수, 람다 함수를 이용한 필터링
adult_ages = list(filter(lambda x : x > 19, ages))
print(adult_ages)

# 리스트 축약표현을 이용한 필터링
print([age for age in ages if age > 19])

# 0에서 9까지 숫자를 포함하는 리스트
print('0에서 9까지 숫자를 포함하는 리스트 : ', [x for x in range(0, 10)])

# 0에서 9까지 숫자의 제곱값
print('0에서 9까지 숫자의 제곱값 : ' , [x**2 for x in range(0, 10)])

# 0에서 9까지 숫자 중 짝수
print('0에서 9까지 숫자 중 짝수 : ', [x for x in range(0, 10) if x % 2 == 0])

# 0에서 9까지 숫자 중 홀수
print('0에서 9까지 숫자 중 홀수 : ', [x for x in range(0, 10) if x % 2 != 0])

# 0에서 9까지 숫자 중 짝수의 제곱값
print('0에서 9까지 숫자 중 짝수의 제곱값 : ', [x**2 for x in range(0, 10) if x % 2 == 0])

# 0에서 9까지 숫자 중 홀수의 제곱값
print('0에서 9까지 숫자 중 홀수의 제곱값 : ', [x**2 for x in range(0, 10) if x % 2 != 0])



# 두 리스트를 곱하여 새 리스트를 생성하는 코드
product_xy = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        product_xy.append(x * y)

print(product_xy)

# 리스트 축약을 이용한 두 리스트의 곱하기 기능
product_ab = [x * y for x in [1, 2, 3] for y in [4, 5, 6]]
print(product_ab)