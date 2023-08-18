# 08-3 강력한 정규 표현식의 세계로
import re

# 문자열 소비가 없는 메타 문자
"""
+, *, [], {} 등의 메타 문자는 매치가 성사되면 문자열을 탐색하는 시작 위치가 변경된다.
(보통 소비된다고 표현한다). 가령 aac 라는 문자열에서 a+라는 패턴을 찾아야 할 때,
aa 가 매치되고 나면 문자열 중 aa는 소비되고 남은 c 가 시작 위치가 된다
"""

# | : or 과 동일한 의미로 사용
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)


# ^ : 문자열의 맨 처음과 일치한다는 것을 의미
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))

# $ : 문자열의 끝과 매치한다는 것을 의미
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))

# \A : 문자열의 처음과 매치된다는 것을 의미
#   re.MULTILINE 옵션을 사용할 경우,
#   ^ 은 각 줄의 문자열의 처음과 매치되지만,
#   \A 는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.

# \Z : 문자열의 끝과 매치된다는 것을 의미
#   re.MULTILINE 옵션을 사용할 경우,
#   $ 메타 문자와는 달리 전체 문자열의 끝과 매치된다.

# \b : 단어 구분자(word boundary)이다. 보통 단어는 화이트스페이스에 의해 구분된다.
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))  # 매치 됨
print(p.search('the declassfied algorith')) # class 양쪽에 화이트스페이스가 없어 매치되지 않음

# \B : \b 메타 문자와 반대. 화이트스페이스로 구분된 단어가 아닌 경우에만 매치
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))  # class 양쪽에 화이트 스페이스가 있으므로 매치되지 않음
print(p.search('the declassfied algorith')) # class 양쪽에 화이트스페이스가 없어 매치됨

# grouping
# 그룹을 만들어 주는 메타 문자는 ()
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)

# 이름 + " " + 전화번호
p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m)

# 위에서 이름 부분만 뽑아내려면
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))

# group(index)
"""
    group(index)    설명
    group(0)        매치된 전체 문자열
    group(1)        첫 번째 그룹에 해당되는 문자열
    group(2)        두 번째그룹에 해당되는 문자열
    group(n)        n 번째 그룹에 해당되는 문자열
"""

# 전화번호만 뽑아내기
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))

# 전화번호 중에서 국번만 뽑아내기
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))

# 위 처럼 그룹을 중첩해 사용할 수 있다.
# 그룹이 중첩된 경우 바깥쪽부터 시작해 안쪽으로 들어갈수록 인덱스 값이 증가한다.

