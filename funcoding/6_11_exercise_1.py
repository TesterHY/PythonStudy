"""
1. 사용자로부터 양의 정수를 입력받고,
   그 만큼의 로또번호를 생성하는 프로그램을 작성하시오.
"""

import random

# 로또번호 리스트
lotto = []
# 게임번호
no = 0

no = input("얼마나 많은 게임을 원하나요? ")

if no.isdigit():
    for i in range(int(no)):
        lotto = random.sample(range(1, 46), 6)
        lotto.sort()
        
        print("로또번호 %d : " % (i+1), end="")

        for j in lotto:
            print("%2d " %j, end = ' ')
        
        print()
