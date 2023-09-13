"""
리스트 축약표현(list comprehension)

- map, filter의 기능 구현 가능
- 람다식의 본체가 될 표현식을 그대로 사용. 따라서 람다 함수를 따로 정의할 필요가 없음

    [ {표현식} for {변수} in {반복자/연속열} if {조건 표현식}]

    - 표현식 : 반복가능 객체의 각 요소에 대해서 적용되는 수식
    - for {} in {} : 반복가능 객체의 순환하느 기능
    - if : 필터의 기능
- 리스트 축약문법에서 다음과 같이 if 조건 표현식은 생략 가능함

    [ {표현식} for {변수} in {반복자/연속열} ]

"""

a = [1, 2, 3, 4, 5, 6, 7]
# 맵과 람다 함수를 이용한 리스트의 제곱 구하기
result1 = list(map(lambda x : x**2, a))
print(result1)

# 리스트 축약 표현식을 이용한 리스트의 제곱 구하기
result2 = [x**2 for x in a]
print(result2)


# 리스트 축약 표현식과 range를 이용한 리스트의 제곱 구하기
result3 = [x**2 for x in range(1, 8)]
print(result3)

# 문자열 각각을 대문자로 바꾸는 기능
st = 'Hello World'
s_list = [ x.upper() for x in st]
print(s_list)
