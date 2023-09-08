import circle

def main():
    r = float(input("반지름 입력 : "))
    ar = circle.ar_circle(r)
    print("넓이 : ", ar)

    ci = circle.ci_circle(r)
    print("둘레 : ", ci)

main()


"""
1. import 
import circle

2. 필요한 함수만
from circle import ar_circle
from circle import ci_circle
from circle import ar_circle, ci_circle

3. 닉네임
from circle import ci_circle as cc
-> function을 cc로 호출

import circle as cc
-> 클래스를 cc로 호출




"""