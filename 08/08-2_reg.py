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