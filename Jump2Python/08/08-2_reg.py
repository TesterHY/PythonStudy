# 08-2 정규 표현식 시작하기

"""
정규 표현식의 기초, 메타 문자

메타 문자 : 특별한 의미를 가진 문자.
정규표현식에 다음과 같은 메타 문자를 사용하면 특별한 의미를 갖게 된다.

. ^ $ * + ? { } [ ] \ | ( )

"""

# [] 문자 - 문자 클래스
#'[' 와 ']' 사이의 문자들과 매치 라는 의미를 갖는다.
"""
[abc]
 "a", "before", "dude" 
 
 "a" 는 정규식과 일치하는 문자인 "a" 가 있으므로 매치된다.
 "before" 는 정규식과 일치하는 문자인 "b"가 있으므로 매치된다.
 "dude" 는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않는다.

[] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미한다.
예를 들어 [a-c]라는 정규 표현식은 [abc]와 동일하고 [0-5]는 [012345]와 동일하다.

[a-zA-Z] : 모든 알파벳
[0-9] : 모든 숫자

^ : 문자 클래스 안에 ^ 메타 문자를 사용할 경우에는 반대(not)라는 의미를 갖는다.
[^0-9] : 숫자가 아닌 문자만 매치된다.

- 자주 사용하는 문자 클래스

\d : 숫자와 매치된다. [0-9]와 동일한 표현식
\D : 숫자가 아닌 것과 매치된다. [^0-9]와 동일한 표현식이다.
\s : 화이트스페이스(whitespace)문자와 매치된다. [ \t\n\r\f\v]와 동일한 표현식. 맨 앞의 빈칸은 공백문자(space)를 의미
\S : 화이트스페이스 문자가 아닌 것과 매치된다. [^ \t\n\r\f\v]와 동일한 표현식.
\w : 문자+숫자(alphanumeric)와 매치된다. [a-zA-Z0-9_]와 동일한 표현식
\W : 문자+숫자(alphanumeric)가 아닌 문자와 매치된다. [^a-zA-Z0-9_]와 동일한 표현식
"""

# .(dot) 문자 - \n을 제외한 모든 문자
# 줄바꿈 문자인 \n을 제외한 모든 문자와 매치된다는 것을 의미한다.
"""
a.b : "a + 모든 문자 + b"
 "aab", "a0b", "abc"

 "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 . 과 일치하므로 정규식과 매치된다.
 "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 . 과 일치하므로 정규식과 매치된다.
 "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는 있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.

a[.]b : "a + . + b" -> []안에 . 문자를 쓰면서 .은 문자 그대로를 의미
 "a.b" 문자열과 매치되고, "a0b" 문자열과는 매치되지 않는다.
"""

# * 문자 - 반복을 의미. 0번 이상 반복될 때 사용
"""
ca*t : "c + a가 0번이상 반복 + t"

    정규식  문자열  매치여부    설명
    ca*t    ct      Yes        "a"가 0번 반복되어 매치
    ca*t    cat     Yes        "a"가 0번 이상 반복되어 매치(1번 반복)
    ca*t    caaat   Yes        "a"가 0번 이상 반복되어 매치(3번 반복)
"""

# + 문자 - 반복을 의미. 최소 1번 이상 반복될 때 사용
"""
ca+t : "c + a가 1번이상 반복 + t"

    정규식  문자열  매치여부    설명
    ca+t    ct      No          "a"가 0번 반복되어 매치되지 않음
    ca+t    cat     Yes         "a"가 1번 이상 반복되어 매치(1번 반복)
    ca+t    caat    Yes         "a"가 1번 이상 반복되어 매치(2번 반복)

"""

# {}, ? - 반복 횟수를 고정
# {m, n} - 반복 횟수가 m부터 n까지인 문자와 매치
# {3, } - 반복 횟수가 3 이상인 경우
# {, 3} - 반복 횟수가 3 이하인 경우
# {1, } - + 와 동일
# {0, } - * 와 동일
"""
1. {m}
ca{2}t : "c + a를 반드시 2번 반복 + t"

    정규식  문자열  매치여부    설명
    ca{2}t  cat     No         "a"가 1번만 반복되어 매치되지 않음.
    ca{2}t  caat    Yes        "a"가 2번 반복되어 매치.

2. {m, n}
ca{2,5}t : "c + a를 2~5회 반복 + t"

    정규식      문자열      매치여부    설명
    ca{2,5}t    cat         No          "a"가 1번만 반복되어 매치되지 않음
    ca{2,5}t    caat        Yes         "a"가 2번 반복되어 매치
    ca{2,5}t    caaaaat     Yes         "a"가 5번 반복되어 매치

3. ? : 반복은 아니지만 비슷한 기능을 함. {0, 1}을 의미
ab?c : "a + b가 있어도 되고 없어도 됨 + c"

    정규식      문자열      매치여부    설명
    ab?c        abc         Yes        b가 1번 사용되어 매치
    ab?c        ac          Yes        b가 0번 사용되어 매치
"""

# 파이썬에서 정규 표현식을 지원하는 re 모듈
# 파이썬에서는 re (regular expression) 모듈을 제공.
"""
사용법

import re
p = re.compile('ab*') 

-> re.compile을 사용하여 정규표현식을 컴파일
-> 리턴값을 p에 할당해 그 이후 작업 수행

"""

"""
정규식을 이용한 문자열 검색

    Method      목적
    match()     문자열의 처음부터 정규식과 매치되는지 조사한다.
    search()    문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
    findall()   정규식과 매치된ㄴ 문자열(substring)을 리스트로 리턴한다.
    finditer()  정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 리턴한다.

"""
import re

p = re.compile('[a-z]+')

# match
m = p.match("python")
print(m) # 매치에 일치하므로 match 객체가 리턴

m = p.match("3 python")
print(m) # 매치에 일치하지 않으므로 None이 리턴

# 보통 다음과 같이 이용함
"""
p = re.compile(정규표현식)
m = p.match( '조사할 문자열' )

if m:
    print('Match found : ', m.group())
else:
    print('No match')

"""

# search : 문자열 전체를 검색 -> match()는 문자열의 처음부터 검색
m = p.search('3 python')
print(m) # 매치에 일치하므로 match 객체가 리턴

# findall : 패턴과 매치되는 모든 값을 찾아 리스트로 리턴
result = p.findall('life is too shoart')
print(result)

# finditer
result = p.finditer("life is too short")
print(result)

for r in result: print(r)

# match 객체의 메서드
"""
    method  목적
    group   매치된 문자열을 리턴한다.
    start   매치된 문자열의 시작 위치를 리턴한다.
    end     매치된 문자열의 끝 위치를 리턴한다.
    span    매치된 문자열의 (시작, 끝)에 해당하는 튜플을 리턴한다.
"""
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

# 모듈 단위로 수행하기
"""
p = re.compile('[a-z]+')
m = p.match("python")

위에 코드는 아래와 동일
re.match('[a-z]+', "python")
"""

# 컴파일 옵션
"""
정규식을 컴파일할 때 다음 옵션을 사용할 수 있다.

DOTALL(S)     - .(dot)이 줄바꿈 문자를 포함해 모든 문자와 매치될 수 있게 한다.
IGNORECASE(I) - 대소문자에 관계없이 매치될 수 있게 한다.
MULTILINE(M)  - 여러 줄과 매치될 수 있게 한다. ^, $ 메타 문자 사용과 관계 있는 옵션
VERBOSE(X)    - verbose 모드를 사용할 수 있게 한다. 정규식을 보기 편하게 만들 수 있고 주석 등을 사용할 수 있게 된다.

"""

# DOTALL, S : .(dot) 메타문자는 줄바꿈 문자(\n)를 제외한 모든 문자와 매치되는 규칙이 있다.
# 만약 \n 문자도 포함하여 매치하고 싶다면 re.DOTALL or re.S 옵션을 사용하면 된다.
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

# IGNORECASE, I : 대소문자 구별 없이 매치를 수행할 때 사용
p = re.compile('[a-z]+', re.I)
m1 = p.match('python')
m2 = p.match('Python')
m3 = p.match('PYTHON')
print(m1, m2, m3)

# MULTILINE, M
# ^ : 문자열의 처음
# $ : 문자열의 마지막
p = re.compile("^python\s\w+") # python이라는 문자열로 시작, 그 뒤에 화이트스페이스, 그 뒤에 단어
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))

p = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data))

# VERBOSE, X : 주석 또는 줄 단위로 구분할 수 있게 함
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

# 역슬래시 문제 : \를 사용한 표현이 계속 반복되는 정규식이라면 raw string 표현법을 사용
p = re.compile(r'\\section') # \\section 문자열 
