"""
6과 45의 최소공배수(largest common multiple)
"""
lcm = 0
n = 45

while True:
    if n % 6 == 0 and n % 45 == 0:
        lcm = n
        break
    n += 1

print('lcm : ', lcm)


"""
42와 120의 최대공약수(greatest common divisor)
"""
gcm = 0
n = 42

while True:
    if 42 % n == 0 and 120 % n == 0:
        gcm = n
        break
    n -= 1

print('gcd : %d' %gcm)

