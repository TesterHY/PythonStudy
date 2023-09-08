"""
##오류 예외 처리 기법

#try-except문
try:
  ...
except [발생오류 [as 오류변수]]:
  ...


# 1. try-except만 쓰는 방법
try:
  ...
except:
  ...

-> 이 경우에는 오류의 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

2. 발생 오류만 포함한 except문
try:
  ...
except 발생오류:
  ...

-> 이 경우는 오류가 발생했을 때 except 문에 미리 정해 놓은 오류와 동일한 오류일 경우에만
   except 블록을 수행한다는 뜻이다.

3. 발생 오류와 오루 변수까지 포함한 except 문
try:
  ...
except 발생오류 as 오류변수:
  ...

-> 이 경우는 오류의 내용까지 알고 싶을 때 사용하는 방법이다.

ex)
try:
 4 / 0
except ZeroDivisionError as e:
 print(e)

-> 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여 except 블록이 실행되고
   오류변수 e에 담기는 오류 메시지를 출력할 수 있다.
   출력되는 오류 메시지는 다음과 같다.
   division by zero



# try-finally 문
 finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
 보통 finally 절은 사용한 리소르를 close해야 할 때 많이 사용한다.

 ex)
 try:
   f = open('foo.txt', 'w')
   # 무언가를 수행한다.

   (... 생략...)
 finally:
   f.close() # 중간에 오류가 발생하더라도 무조건 실행된다.


# 여러 개의 오류 처리하기
try:
  ...
except 발생오류1:
  ...
except 발생오류2:
  ...

# 2개 이상의 오류를 동일하게 처리하기 위해서는 괄호를 사용하여 함께 묶어 처리
ex)
try:
  a = [1,2]
  print(a[3])
  4/0
except (ZeroDivisionError, IndexError) as e:
  print(e)


"""

# try-else문
"""
try문 수행 중 
  오류가 발생하면 except절, 
  오류가 발생하지 않으면 else 절이 수행된다.
"""

try :
    age = int(input('나이를 입력하세요. '))
except :
    print('입력이 정확하지 않습니다.')
else :
    if age <= 18:
        print('미성년자는 출입금지입니다')
    else :
        print('환영합니다.')

# 오류 회피하기
"""
코드를 작성하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있다.
"""
try :
    f = open("nonamefile", 'r')
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
"""
파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.
예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록
만들고 싶은 경우가 있다.
"""
class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()