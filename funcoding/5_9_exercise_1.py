"""
1. 튜플 혹은 문자열을 인자로 전달하면, 이를 리스트로 바꿔주는 함수를 만들어보자.
예를 들어서 to_list라는 이름으로 함수를 만들었다면 다음과 같이 동작해야 한다.

ds = (1,2,3) # 튜플 생성
ds = to_list(ds) # 튜플 전달 및 리스트 반환
ds
[1, 2, 3]

ds = "hello" # 문자열 생성
ds = to_list(ds) # 문자열 전달 및 리스트 반환
ds
['h', 'e', 'l', 'l', 'o']
"""

def to_list(param):
    return list(param)

ds = (1, 2, 3)
ds = to_list(ds)
print(ds)

ds = "hello"
ds = to_list(ds)
print(ds)
