"""
['a', 'b', 'c', 'd']와 같은 영문 소문자가 들어 있는 a_list라는 이름의 리스트를
['A', 'B', 'C', 'D']와 같은 영문 대문자가 들어 있는 upper_a_list라는 이름의 리스트로 변환시키는 map() 함수를 작성하여라.


"""

#1. 이 때 소문자를 매개변수로 받아 대문자를 반환하는 to_upper()라는 이름의 함수를 정의하여 변환시키시오.
def to_upper(s):
    return s.upper()

a_list = ['a', 'b', 'c', 'd']
upper_a_list1 = []

upper_a_list1 = list(map(to_upper, a_list))
print(upper_a_list1)


#2. 「1」에서 생성한 to_upper()함수를 lambda함수로 고쳐서 간결하게 변환시키시오 (힌트: str의 upper()메소드를 사용해 보세요)

upper_a_list2 = []
upper_a_list2 = list(map(lambda x : x.upper(), a_list))
print(upper_a_list2)

