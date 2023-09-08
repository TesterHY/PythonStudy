import turtle as t

while True:
    direction = input("왼쪽(l), 오른쪽(r) : ")
    if direction == 'l':
        t.left(60)
        t.forward(100)
    if direction == 'r':
        t.right(60)
        t.forward(100)
