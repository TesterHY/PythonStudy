"""
A와B 리스트를 입력받아 A리스트 항목들이 B리스트에 모두 존재하면 True, 없으면 False를 반환하는 알고리즘을 생각한 후,
그 알고리즘을 same_elements()함수로 구현하라

1. A 리스트로 루프시작
 - A 의 요소가 B의 리스트에 존재 하지 않을 경우 return False 
2. A 루프가 종료되면 True를 반환

"""

l1 = [1, 2, 3]
l2 = [1, 3, 5, 4]

def same_elements(l1, l2):
    for s in l1:
        if s not in l2:
            return False
    
    return True

result2 = same_elements(l1, l2)
print(result2)
