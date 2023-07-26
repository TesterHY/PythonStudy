"""
# 파일 읽고 쓰기
"""

# 파일 생성하기
f = open('새파일.txt', 'w')
f.close()

"""
파일 객체 = open(파일이름, 파일열기모드)

- 파일열기모드
  r : 읽기 모드
  w : 쓰기 모드
  a : 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용

- 파일 경로와 슬래시(/)
  파이썬 코드에서 파일경로를 표시할 때 "C:/doit/새파일.txt" 처럼 슬래시(/)를 사용할 수 있다.
  만약 역슬래시(\)를 사용한다면 "C:\\doit\\새파일.txt" 처럼 역슬래시를 2개 사용하거나
  r"C:\doit\새파일.txt" 와 같이 문자열 앞에 r 문자(raw string)를 덧붙여 사용해야 한다.
  왜냐하면 \n과 같은 이스케이프 문자가 있을 경우, 줄바꿈 문자로 해석되어 의도했던 파일 경로와 달라지기 때문이다.
"""

# 파일을 쓰기 모드고 열어 내용 쓰기
f = open('새파일2.txt', 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i 
    f.write(data)
f.close()

# 파일을 읽는 여러 가지 방법
# readline 함수 이용하기
f = open('새파일2.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines 함수 사용하기
f = open("새파일2.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip() # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()

# read 함수 사용하기 - 파일의 내용 전체를 문자열로 리턴한다.
f = open("새파일2.txt", "r")
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
f = open('새파일2.txt', 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with 문과 함께 사용하기 - 파일을 열고 닫는 것을 자동으로 처리
with open('foo.txt', 'w') as f:
    f.write('Life is too short, you need python')
