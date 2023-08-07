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
