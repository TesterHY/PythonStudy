"""
#예외 만들기

프로그램을 수행하다가 특수한 경우에만 예외 처리를 하려고 종종 예외를 만들어서 사용한다.

"""

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


try:
    say_nick('sara')
    say_nick('바보')
except MyError:
    print("허용되지 않는 별명입니다")

try:
    say_nick('sara')
    say_nick('바보')
except MyError as e:
    print(e)

