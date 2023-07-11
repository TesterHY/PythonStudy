"""
불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.
 - True, False 는 파이썬 예약어로, 첫 문자를 항상 대문자로 작성해야한다.
"""

### 사용법
a = True
b = False
print(type(a))
print(type(b))

# 조건문의 리턴값으로도 사용된다.
print(1==1)

"""
자료형의 참과 거짓

- 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 (= "", [], (), {}) 거짓이 되고
  비어 있지 않으면 참이 된다.
- 숫자에서는 그 값이 0 일 때 거짓이 된다.
"""