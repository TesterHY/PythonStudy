# for
"""
기본 구조

for 변수 in 리스트( 또는 튜플, 문자열):
 수행할 문장1
 수행할 문장2
 ...

"""

# 1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 2. 다양한 for문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first) in a:
    print(first)

for (first, last) in a:
    print(first + last)

# 3. for문의 응용
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다.
# 합격인지, 불합격인지 결과를 보여 주시오
marks = [90, 25, 67, 45, 80] # 학생들의 시험 점수 리스트
number = 0 # 학생에게 붙여줄 번호

for mark in marks:
    number = number + 1

    if mark >= 60:
        print('%d번 학생은 합격입니다.' % number)
    else:
        print('%d번 학생은 불합격입니다.' % number)

# range함수
a = range(11)
print(a)

sum = 0
for i in range(1, 11):
    sum += i

print(sum)


# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = ' ')
    print('')

### list comprehension 사용하기
a = [1, 2, 3, 4]
result = []

# a의 요솟값에 3을 곱한 값을 result에 담기
for num in a:
    result.append(num * 3)
print(result)

# 위와 동일(list comprehension 사용)
result2 = [num * 3 for num in a]
print(result2)

result3 = [num * 3 for num in a if num % 2 == 0]
print(result3)

### list comprehension 문법
"""
# 1개
[표현식 for 항목 in 반복가능객체 if 조건문]

# 2개 이상도 가능
[표현식 for 항목1 in 반복가능객체1 if 조건문1]
      for 항목2 in 반복가능객체2 if 조건문2
      ...
      for 항목n in 반복가능객체n if 조건문n]
"""

# 구구단의 모든 결과를 리스트에 담기
result4 = [x * y for x in range(2, 10)
                for y in range(1, 10)]
print(result4)
