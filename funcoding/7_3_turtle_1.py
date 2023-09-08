"""
turtle 라이브러리 사용하기

- 이동 관련 함수
  forward(n)    : 앞으로 n만큼 이동
  backward(n)   : 뒤로 n만큼 이동
  home()        : 중심위치로 이동
  penup()       : 펜을 올림
  pendown()     : 펜을 내림
  goto(x,y)     : 지정한 x, y좌표로 이동
  Shape(모양)    : 화살표 변경

- 회전/색상 관련 함수
  right(n)      : 오른쪽으로 n도만큼 회전
  left(n)       : 왼쪽으로 n도만큼 회전
  color(c)      : 거북이 색상 변경
  pencolor(c)   : 선 색상 변경
  bgcolor(c)    : 배경 색상 변경

- 그리기 관련 함수
  circle(n)     : 반지름이 n인 원 그림
  dot(n)        : 크기가 n인 점을 그림
  width(n)      : 선의 두께 설정
  clear()       : 화면을 지움

- 기타 함수
  shape()       : 화살표의 모양 변경
  shapesize(n)  : 화솔표의 크기 변경
  xcor()        : 터틀의 현재 x위치
  ycor()        : 터틀의 현재 y위치
  distance(x,y) : 터틀의 위치와 지정 좌표 거리
"""

# 사각형 그리기
import turtle as t

#t = turtle.Pen()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
