"""
reduce function

"""

from functools import reduce

# 1. reduce() 함수를 사용하여 1에서 100까지 정수의 합을 구하여라.
#    이 때, range(1, 101)을 입력으로 사용하여라

n = reduce(lambda x, y: x + y, range(1, 101))
print(n)

# 2. reduce() 함수를 사용하여 10! 을 구하여라. 이 때 range(1, 11)을 입력으로 사용하여라
n = reduce(lambda x, y : x * y, range(1, 11))
print(n)
