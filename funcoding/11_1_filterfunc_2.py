"""
필터함수(filter function)

- 반복 가능한 요소들을 함수에 넣어 그 리턴값이 참인 것만 묶어서 반환

"""

# 음수 값 추출기능
def minus_func(n):
    if n < 0 :
        return True
    else:
        return False
    
n_list = [-30, 45, -5, -90, 20, 53, 77, -36]
minus_list1 = []
minus_list2 = []
minus_list3 = []

for n in filter(minus_func, n_list):
    minus_list1.append(n)

print('음수 리스트 : ', minus_list1)


for n in filter(lambda x : x < 0, n_list):
    minus_list2.append(n)

print('음수 리스트 : ', minus_list2)

minus_list3 = list(filter(lambda x : x < 0, n_list))
print('음수 리스트 : ', minus_list3)
