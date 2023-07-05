"""

- 딕셔너리는 key, value를 한 쌍으로 가지는 자료형
- 순차적으로 모두 검색하는 것이 아니라 key를 지정하여 검색

# 딕셔너리의 기본 모습
{Key1: Value1, Key2: Value2, Key3: Valu3 ...}

"""

# 딕셔너리 추가
a = {1: 'a'}
print(a)
a[2] = 'b'
a[3] = [1, 2, 3]
print(a)

# 딕셔너리 삭제
del a[2]
print(a)

# 딕셔너리에서 Key를 사용해 Value 얻기
grade = {'shiu': 99, 'akane': 88}
print('shiu : %s, akane : %s'  %(grade['shiu'], grade['akane']))

# 딕셔너리 만들 때 주의할 사항
# 딕셔너리에서 Key는 고유한 값이므로 중복도는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
a = {1: 'a', 1: 'b'}
print(a)


# Key에 리스트를 쓸 수 없다. 하지만 튜플은 Key로 쓸 수 있다.

# a = {[1, 2]: "Hello"}
# print(a)  # Key를 리스트로 사용하여 ,에러 발생

a = {(1, 2) : "Hello", (3, 4) : "World"}
print(a)
print(a[1, 2])

### 딕셔너리 관련 함수 ###

# keys - Key 리스트 만들기
a = {'name': 'shiu', 'phone': '012-3456-7890', 'birth': '0323'}
print(a.keys())

for k in a.keys():
    print('key : %s' % k)

# values - Value 리스트 만들기
for v in a.values():
    print('value : %s' % v)

# items - Key, Value 쌍 얻기
for i in a.items():
    print('item : %s ' % str(i))

# clear - Key, Value 쌍 모두 지우기
a.clear()
print(a)

# get - Key로 Value 얻기
a = {'name': 'shiu', 'phone': '012-3456-7890', 'birth': '0323'}
name = a.get('name')
print(f'name : {name}')

## 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우
## a['nokey'] 방식은 오류를 발생시킴
## a.get('nokey') 방식은 None을 리턴함

# get Default 값
nokey = a.get('nokey', 'aaa')
print(nokey)

# in - 해당 Key가 딕셔너리 안에 있는지 조사하기
isName = 'name' in a
isHobby = 'hobby' in a
print('isName : %s, isHobby : %s' %(isName, isHobby))
