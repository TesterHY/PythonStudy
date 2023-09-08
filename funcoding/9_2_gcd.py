"""
유클리드 알고리즘 실행
"""

def gcd(a, b):
    print("gcd", (a,b))
    while True:
        r = a % b
        
        if r == 0: 
            a = b
            break

        a = b
        b = r
        print("gcd", (a,b))
    return a

print(gcd(60, 28))

