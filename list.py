# 리스트의 인덱싱
a = [1, 2, 3]
print(a[0])


b = [1, 2, 3, ['a', 'b', 'c']]
print(b[3][1])


c = [1, 2, ['a', 'b', ['Life', 'is']]]
print(c[2][2][0])

# 리스트의 슬라이싱
d = [1, 2, 3, 4, 5]
print(d[0:2])


# 리스트 연산하기
e = [1, 2, 3]
f = [4, 5, 6]
print(e + f)
print(e * 3)

# 리스트 길이 구하기
print(len(e))


# 리스트의 수정과 삭제
g = [1, 2, 3, 4, 5]
g[1] = 5
print(g)

del g[2]
print(g)

del g[2:]
print(g)

# 리스트에 요소 추가하기 - append
h = [1, 2, 3]
h.append(4)
print(h)

h.append(['Hello', 5])
print(h)

# 리스트 정렬 - sort
i = [1, 3, 2, 9, 5, 8]
i.sort()
print(i)

# 리스트 뒤집기 - reverse
i.reverse()
print(i)

# 인덱스 반환 - index
j = [1, 2, 3, 4, 5, 6]
j1 = j.index(5) # 숫자 5의 위치 반환
print(j1)

# 리스트에 요소 삽입 - insert
k = [2, 3, 4]
k.insert(0, 9)
print(k) # 0번째에 숫자9를 삽입


# 리스트 요소 제거 - remove
l = [1, 2, 3, 1, 2, 3]
l.remove(3) # 리스트에서 첫 번째로 나오는 숫자3을 삭제
print(l)


# 리스트 요소 끄집어 내기 - pop
m = [1, 2, 3]
m1 = m.pop() # 리스트의 맨 마지막 요소를 리턴하고 그 요소를 삭제
print(m1)
print(m)

n = [1, 2, 3]
n1 = n.pop(1) # 리스트의 1번째 요소를 리턴하고 그 요소는 삭제
print(n1)
print(n)

o = [1, 2, 3, 1, 4, 5, 1]
o1 = o.count(1)
print(o1)

# 리스트 확장 - expand
p = [1, 2, 3]
p1 = [4, 5]
p.extend(p1)
print(p)

