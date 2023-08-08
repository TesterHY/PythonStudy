#traceback : 프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈
import traceback

def a():
    return 1/0

def b():
    a()

def main():
    try:
        b()
    except:
        print("Error!")
        print(traceback.format_exc())

main()