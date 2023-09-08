def factorial(n):

    print("n : %d" %n)

    if n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))
