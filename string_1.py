a = "Life is too short, you need python"
b = "a"
c = "123"

d = 'python is fun'
e = """Hello
Python
"""
f = '''Hello
World
'''


print(a)
print(b)
print(c)

print(d)
print(e)
print(f)

g = '"Python is very easy." he says'
print(g)

h = "I eat {0} apples".format(3)
print(h)

i = "I eat %d apples" %3
print(i)

# 문자열 포매팅
j = 'I ate {number} apples. so I was sick for {day} days.'.format(number=10, day=3)
print(j)

# 문자열 인덱스
k = "Life is too short, You need Python"
print(k[0], k[1])

# 문자열 슬라이싱
print(k[0:4])

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.
l = "Error is %d%%." % 99
print(l)

# %10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을
# 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미
m = "%10sShiu" % "Hello"
print(m)

# %-10s는 전체 길이가 10개인 문자열 공간에서 대입되는 값을
# 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미
n = "%-10sShiu" % "Hello"
print(n)

#소수점 표현하기
o1 = "%0.4f" % 3.42132434
print(o1)

o2 = 3.42134234
print("{0:0.5f}".format(o2))

# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고
# 문자열의 총 자릿수를 10으로 맞출 수 있다.
# 빈 공간을 a로 채움
a1 = "{0:a<10}".format("hi")
print(a1)

# :>10 표현식을 사용하면 치환되는 문자열을 오른쪽으로 정렬하고
# 문자열의 총 자릿수를 10으로 맞출 수 있다.
# 빈 공간을 a로 채움
a2 = "{0:a>10}".format("hi")
print(a2)

# :^를 사용하면 가운데 정렬
# 빈 공간을 =로 채움
a3 = "{0:=^10}".format("hi")
print(a3)

# f문자열 포매팅
f_name = 'Shiu'
f_age = 7
print(f'나의 이름은 {f_name}입니다. 나이는 {f_age}입니다.')
print(f'나는 내년이면 {f_age + 1} 살이 됩니다.')

f_dic = {'name':'Sara', 'age':15}
print(f'나의 이름은 {f_dic["name"]} 입니다. 나이는 {f_dic["age"]} 입니다.')

f_left = f'{"hi":<10}'
f_right = f'{"hi":>10}'
f_center = f'{"hi":^10}'

print(f_left)
print(f_right)
print(f_center)

# count
c1 = "Hello"
print(c1.count('l'))

# find
f1 = "Python is the best choice"
print(f1.find('b'))
print(f1.find('k'))

# 문자열 삽입
j1 = 'abcdefg'
print(",".join(j1))
print("\t".join(j1))

# upper, lower
str1 = 'My Name is Sara'
print(str1.upper())
print(str1.lower())

# 공백 지우기
str2 = '  Hello Every One   '
print(str2.lstrip()) # 왼쪽 공백 지우기
print(str2.rstrip()) # 오른쪽 공백 지우기
print(str2.strip()) # 양쪽 공백 지우기


# 문자열 나누기 - split
str3 = "Life is too short"
print(str3.split())

str4 = "a:b:c:d:e"
print(str4.split(":"))

