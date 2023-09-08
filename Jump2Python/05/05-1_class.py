"""
클래스 = 과자틀
객체 = 과자 틀로 찍어 낸 과자
"""

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(1))
print(cal1.add(2))
print(cal2.add(3))
print(cal2.add(4))



class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result


a = FourCal(4, 2)

print(a.first)
print(a.second)

resultAdd = a.add()
print(resultAdd)

resultSub = a.sub()
print(resultSub)

resultMul = a.mul()
print(resultMul)

resultDiv = a.div()
print(resultDiv)





# 상속하기
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(10, 5)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())


# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())


# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)