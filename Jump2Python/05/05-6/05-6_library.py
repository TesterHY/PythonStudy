# datetime.date
import datetime
day1 = datetime.date(2011,11,3)
day2 = datetime.date(2023,8,4)
diff = day2 - day1
print(diff.days)

day3 = datetime.date(2023, 8, 4)
print(day3.weekday())  # 0:월요일
print(day3.isoweekday()) # 1:월요일

# time.time() : UTC(universal time coordinated, 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 리턴하는 함수
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴해 준다.
import time
print(time.time())

# time.localtime : time.time()이 리턴한 실숫값을 사용해서 년, 월, 일, 시 분, 초 ...의 형태로 바꾸어 주는 함수이다.
print(time.localtime(time.time()))
print(time.localtime())

# time.asctime : time.localtime가 리턴된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수
print(time.asctime(time.localtime(time.time())))
print(time.asctime())

# time.ctime : 항상 현재 시간만 리턴
print(time.ctime())

# time.strftime : 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
# time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
"""
포맷코드	설명	예
%a	요일의 줄임말	Mon
%A	요일	Monday
%b	달의 줄임말	Jan
%B	달	January
%c	날짜와 시간을 출력함.	Thu May 25 10:13:52 2023
%d	일(day)	[01,31]
%H	시간(hour): 24시간 출력 형태	[00,23]
%I	시간(hour): 12시간 출력 형태	[01,12]
%j	1년 중 누적 날짜	[001,366]
%m	달	[01,12]
%M	분	[01,59]
%p	AM or PM	AM
%S	초	[00,59]
%U	1년 중 누적 주(일요일 시작)	[00,53]
%w	숫자로 된 요일	[0(일), 6(토)]
%W	1년 중 누적 주(월요일 시작)	[00,53]
%x	현재 설정된 지역에 기반한 날짜 출력	05/25/23
%X	현재 설정된 지역에 기반한 시간 출력	17:22:21
%Y	연도 출력	2023
%Z	시간대 출력	대한민국 표준시
%%	문자 %	%
%y	세기 부분을 제외한 연도 출력	01
"""
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%c'))

# time.sleep : 주로 루프 안에서 많이 사용. 일정한 시간 간격을 두고 루프를 실행할 수 있다.
# for i in range(10):
#     print(i)
#     time.sleep(1)


# math.gcd : 최대 공약수(gcd, greates common divisor)를 구할 때
import math
print(math.gcd(60, 100, 80))

# math.lcm : 최소 공배수(lcm, least common multiple)를 구할 때
print(math.lcm(15, 25))

# random : 난수를 발생시키는 모듈
import random
print(random.random()) # 0.0~1.0 난수 리턴
print(random.randint(1, 100)) # 1~100 난수 리턴

# itertols.zip_longest : 같은 개수의 자료형을 묶는 파이썬 내장 함수인 zip 함수와 똑같이 동작한다.
# 하지만 itertools.zip_logest() 함수는 전달한 반복 가능 객체(*iterables)의 길이가 서로 다르다면
# 긴 객체의 길이에 맞춰 fillvalue에 설정한 값을 객체에 채울 수 있다.
students = ['Sara', 'Shiu', 'HY', 'Aka', 'Jack', 'Bit']
snacks = ['candy', 'jelly', 'chocolate']

result1 = zip(students, snacks)
print(list(result1))

import itertools
result2 = itertools.zip_longest(students, snacks, fillvalue='potato chips')
print(list(result2))


# itertools.permutation
# itertools.permutation(iterable, r) 은 반복 가능 객체 중에서 r개를 선택한 순열을 이터레이터로 리턴하는 함수
# 1, 2, 3이라는 숫자가 적힌 3장의 카드에서 2장의 카드를 꺼내 만들 수 있는 2자리 숫자를 모두 구하려면 어떻게 해야 할까?
# (1,2), (1,3), (2,1), (2,3), (3,1), (3,2) 로 6가지
result3 = itertools.permutations(['1', '2', '3'], 2)
print(list(result3))

# [1,2,3]이라느 3장의 카드 중 순서에 상관없이 2장을 뽑는 경우의 수는 모두 3가지(조합)
# (1,2), (2,3), (1,3)
result4 = itertools.combinations(['1', '2', '3'], 2)
print(list(result4))

# 1~45 중 서로 다른 숫자 6개를 뽑는 로또 번호의 모든 경우의 수(조합)를 구하고 그 개수를 출력하려면 어떻게 해야 할까?
lotto = itertools.combinations(range(1, 46), 6)
#print(len(list(lotto)))

# 같은 숫자를 허용하는 중복 조합은 
lotto2 = itertools.combinations_with_replacement(range(1, 46), 6)
#print(len(list(lotto2)))

#functools.reduce(function, iterable) : 함수(function)를 반복 가능한 객체(iterable)의 요소에 차례대로(왼쪽에서 오른쪽으로)
# 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수이다.
def add(data):
    result = 0
    for i in data:
        result += i
    return result
data = [1, 2, 3, 4, 5]
result = add(data)
print(result)

import functools
result2 = functools.reduce(lambda x, y: x+y, data)
print(result2)

# 최댓값 구하기
num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y : x if x > y else y, num_list)
min_num = functools.reduce(lambda x, y : x if x < y else y, num_list)
print(max_num, min_num)

# operator.itemgetter : sorted와 같은 함수의 key 매개변수에 적용하여 다양한 기준으로 정렬할 수 있도록 도와주는 모듈
from operator import itemgetter
students = [
    ('jane', 22, 'A'),
    ('dave', 32, 'B'),
    ('sally', 12, 'B'),
]

# 튜플의 요소로 정렬
result = sorted(students, key=itemgetter(1)) # 두 번째 요소로 정렬
print(result)

students2 = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

# 딕셔너리 키를 사용하여 정렬
result = sorted(students2, key=itemgetter('age'))
print(result)


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students3 = [
    Student('jane', 22, 'A'),
    Student('dave', 32, 'B'),
    Student('sally', 17, 'C'),
]

# 클래스 객체 정렬 -> attrgetter()
from operator import attrgetter
result = sorted(students3, key=attrgetter('age'))
print(result)

# shutil : 복사하거나 이동할 떄 사용하는 모듈
import shutil
# shutil.copy("copy moto", "copy saki")
# shutil.move("copy moto", "copy saki")

# glob : 특정 디렉토리에 있는 파일들을 리스트로 만들기
import glob
filelist = glob.glob("c:/Dev/PythonWorkspace/PythonStudy/05/*.py")
print(filelist)

# pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle

# dump함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

# dump로 저장한 파일을 load를 사용해서 원래 있던 딕셔너리 객체 그대로 불러오는 예
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()

## os : 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해 주는 모듈
# os.environ : 환경변수
import os
print(os.environ['PATH'])


# os.getcwd : 현재 디렉터리 위치 리턴
print(os.getcwd())

# os.chdir : 디렉터리 위치 변경
# os.chdir("C:/Dev")
# print(os.getcwd())

# os.system : 시스템 명령어 호출
print(os.system("ls"))

# os.popen : 실행한 시스템 명렁어의 결괏값 돌려받기
f = os.popen("ls")
print(f.read())

# os.mkdir(디렉토리) : 디렉터리 생성
# os.rmdir(디렉토리) : 디렉터리 삭제. 단, 디렉터리가 비어 있어야 삭제할 수 있다.
# os.remove(파일) : 파일 삭제
# os.rename0(src, dst) : src라는 이름의 파일을 dst라는 이름으로 바꾼다.

# zipfile : 여러 개의 파일을 zip형식으로 합치거나 이를 해제할 때 사용하는 모듈
# a.txt, b.txt, c.txt 를 mytext.zip이라는 파일을 만들고 이 파일을 원래의 텍스트 파일 3개로 해제하는 프로그램을 만들려면?
import zipfile

# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip :
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해제하기
# with zipfile.ZipFile('mytext.zip') as myzip :
#     myzip.extractall()

# 특정 파일만 해제하기
# with zipfile.ZipFile('mytext.zip') as myzip :
#     myzip.extract('a.txt')

# 압축하여 묶기
"""
compression 
 ZIP_STORED : 압축하지 않고 파일을 zip으로만 묶는다. 속도가 빠르다.
 ZIP_DEFLATED : 일반적인 zip 압축으로 속도가 빠르고 압축률은 낮다 (호환성이 좋다)
 ZIP_BZIP2 : bzip2 압축으로 압축률이 높고 속도가 느리다.
 ZIP_LAMA : lzma 압축으로 압축률이 높고 속도가 느리다(7zip과 동일한 알고리즘으로 알려져 있다)

compressionlevel 은 압축수준을 의미하는 숫자값으로 1은 속도가 가장 빠르지만 압축률이 낮고, 9는 속도는 가장 느리지만 압축률이 높다
"""
# with zipfile.ZipFile('compressionMytext.zip', 'w', compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip :
#     myzip.write('a.txt')
#     myzip.write('b.txt')
#     myzip.write('c.txt')



# tempfile : 파일을 임시로 만들어서 사용할 때 유용한 모듈
import tempfile

# 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 리턴
# filename = tempfile.mkstemp()
# print(filename)

# f = tempfile.TemporaryFile()
# print(f.name)
# f.close()

# json : JSON 데이터를 쉽게 처리하고자 사용하는 모듈
import json
with open('myinfo.json') as f:
    data = json.load(f)

print(type(data))
print(data)

with open('myinfo2.json', 'w') as f:
    json.dump(data, f)

d = {"name":"사라", "birth":"0323", "age":7}
json_data = json.dumps(d) # json 문자열 생성
print(json_data)

print(json.loads(json_data)) # json 문자열 불러오기

json_data2 = json.dumps(d, indent=2, ensure_ascii=False)
print(json_data2)


# webbrowser : 파이썬 프로그램에서 시스템 브라우저를 호출할 때 사용하는 모듈
import webbrowser

# webbrowser.open_new('http://python.org')
webbrowser.open('http://python.org')
