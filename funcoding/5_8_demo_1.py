"""
문제. 다음 수식의 빈칸에 들어갈 수를 찾는 코드를 작성해 보자.
단, ◻︎는 63보다 작은 정수

- 3 * ◻︎ / 2 = 63 
- 정답인 42만 찾으면 맞는 것으로 인정
"""


x = 1
answer = 0

while x < 63:
    if 3 * x / 2 == 63:
        answer = x
        break
    x += 1

print('answer is : ', answer)