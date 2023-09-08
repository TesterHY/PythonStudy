"""
임의의 실수 a,b,c가 주어졌을 때, 2차방정식 ax^2+bx+c=0의 근을 구하는 알고리즘을 작성한 뒤,
코드로 구현하라.
- 단, 제곱근의 계산을 위해서 math 모듈의 sqrt()란 함수를 사용할 수 잇다.

1. det <- b*b-4ac를 계산
2. det 음수이면 허근이 나오므로 오류를 반환
3. det 0이면 중근
4. 두 개의 근(-b(+-)sqrt(det))/2a
"""

import math

a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c :"))

det = b*b-4*a*c

if det < 0:
    print("판별식이 0보다 작습니다.")
elif det == 0:
    print("중근 : ", -1*b/(2*a))
else:
    print("X1 : ", (-1*b+math.sqrt(det))/(2*a))
    print("X2 : ", (-1*b-math.sqrt(det))/(2*a))