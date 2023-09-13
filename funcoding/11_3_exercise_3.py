"""
다음과 같은 문장으로 된 lyrics라는 문자열이 있다. 이 문자열을 각 단어별로 구분한 후,
아래 실행 결과와 같이 각 단어와, 그 단어에 대한 대문자 튜플 쌍으로 바꾸어 출력하여라

  lyrics = 'Half of my heart is in Havana'
  실행결과 :
    [('Half', 'HALF'), ('of', 'OF') ... ('Havana', 'HAVANA')]
"""

lyrics = 'Half of my heart is in Havana'
# 1. lyrics 라는 문자열을 split() 메소드로 구분하여 각 단어를 추출한 후 
# for 문안에서 각 단어에 대한 upper() 메소드를 적용하여 구하시오\

r1 = []
l1 = lyrics.split()

for str in l1:
    r1.append((str, str.upper()))

print(r1)



# 2. 「1」과 동일한 내용을 리스트 축약 표현을 사용하여 구하시오　
r2 = [(str, str.upper()) for str in l1]
print(r2)




"""
다음과 같이 10개의 정수를 가진 n_list에서 12의 배수를 모두 찾아서 
new_list라는 리스트에 저장하라

  >> 실행결과:
  n_list = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]
  new_list = [24, 144]

"""

n_list = [44, 66, 34, 24, 144, 98, 38, 568, 234, 345]

# 1) 이를 위하여 for문과 if 조건식을 사용하여 문제를 해결하라
new_list1 = []

for n in n_list:
    if n % 12 == 0:
        new_list1.append(n)

print('#1 : ', new_list1)

# 2) 이를 위하여 filter() 함수와 람다 함수를 사용하여 문제를 해결하라
new_list2 = []

new_list2 = list(filter(lambda n : n % 12 == 0, n_list))
print('#2 : ', new_list2)

# 3) 리스트 축약 표현을 이용하여 위의 문제를 해결하라
new_list3 = []

new_list3 = [n for n in n_list if n % 12 == 0]
print('#3 : ', new_list3)


"""
['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
로 이루어진 리스트로부터 다음과 같은 리스트를 생성하시오

  >> 실행결과 :
    ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

"""

week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# 1) for문과 슬라이싱, upper() 메소드를 사용
new_week1 = []

for str in week:
    new_week1.append(str[:3].upper())
print('#1 : ', new_week1)

# 2) map() 함수와 람다함수를 사용
new_week2 = []

new_week2 = list(map(lambda s : s[:3].upper(), week))
print('#2 : ', new_week2)


# 3) 리스트 축약 표현을 이용
new_week3 = [s[:3].upper() for s in week]
print('#3 : ', new_week3)


