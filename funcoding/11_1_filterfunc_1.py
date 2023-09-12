"""
필터함수(filter function)

- 반복 가능한 요소들을 함수에 넣어 그 리턴값이 참인 것만 묶어서 반환

"""

# 19세 이상의 값이 들어오면 True, 그렇지 않으면 False를 반환
def adult_func(n):
    if n >= 19:
        return True
    else:
        return False

ages = [34, 39, 20, 18, 13, 54]
print('성년 리스트 : ')

for a in filter(adult_func, ages):
    print(a, end = ' ')


for a in filter(lambda x: x >= 19, ages):
    print(a, end = ' ')
    