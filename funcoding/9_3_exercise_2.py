"""
아래와 같은 리스트를 입력받아, 가장 작은 값과 가장 큰 값 모두 찾아
한꺼번에 반환하는 알고리즘을 생각한 후, 그 알고리즘을 find_min_max() 함수로 구현하시오

[2, 4, 56, 0, 8, 34, 7, 5]

1. 리스트를 입력받는다.
2. 루프 시작
2-1. 리스트의 첫번째 요소를 min, max 변수에 넣는다.
2-2. 리스트의 그 다음 요소(i)를 min과 비교하여, 작으면 min 에 i 값을 넣는다.
    if i < min:
        min = i
2-3. 리스트의 요소 (i)를 max와 비교하여, 크면 max 에 i 값을 넣는다.
    if max < i:
        max = i
3. 함수 반환은 min, max를 한다.
"""

def find_min_max(l) :

    min, max = 0, 0

    for i in range(0, len(l)):

        num = l[i]

        if i == 0:
            min = num
            max = num
            continue

        if num < min:
            min = num

        if max < num:
            max = num

    print("min : %d, max : %d" %(min, max))
    return min, max

li = [-2, 4, 56, 0, 8, 34, 7, 5]

result = find_min_max(li)
print(result[0], result[1])