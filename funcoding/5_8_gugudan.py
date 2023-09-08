"""
구구단 프로그램 작성

1. 사용자로부터 정수 입력을 받아들인다. (가정 : 입력은 반드시 정수로 받음)
2. 만약 입력이 2보다 작거나 9보다 큰 정수가 들어올 경우, 적절한 입력(2이상 9이하의 정수) 이 들어올 때까지 계속해서 사용자에게 입력을 받아들인다.
3. 적절한 입력이 들어왔다면, 입력에 해당하는 구구단을 출력하고, 다른 구구단을 사용자가 계속해서 보고 싶은지 확인한다.
(가정: 입력은 영문 소문자y 혹은n만 받음).
 - 만약 사용자가 y를 입력한다면, 위 스텝 1로 돌아간다.
 - 만약 사용자가 n을 입력한다면, 프로그램을 종료한다.
"""

def gugudan(num):
    print('%d단 출력 :' %num)
    for i in range(1, 10):
        print('%d X %d = %d' % (num, i, num*i))

while True:
    gugudanNo = input("어떤 구구단을 원하시나요? (2단부터 9단까지만 가능)")

    if gugudanNo.isdigit():
        if 2 <= int(gugudanNo) <= 9:
            gugudan(int(gugudanNo))
            
            isMore = input('계속 하기를 원하시나요? (y/n)')
            if isMore == 'y':
                continue
            else :
                print('구구단 프로그램을 종료합니다.')
                break
    



