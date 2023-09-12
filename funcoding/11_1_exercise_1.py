"""
정수 요소 값을 가진 n_list=[1,2,3,4,5,6,7,8,9,10]이라는 리스트가 있다.
n_list에서 짝수 값 항목만을 가진 even_list라는 리스트를 람다 함수를 이용하여
아래와 같이 생성해 보자.

even_list = [2, 4, 6, 8, 10]

1) 이때 even_list라는 빈 리스트를 만든 후 append() 메소드를 이용하여 짝수값 항목을 추가시켜 보시오
2) filter() 함수가 반환하는 객체를 list() 함수를 통하여 리스트 객체로 만들어서 even_list에 할당하시오

"""

n_list=[1,2,3,4,5,6,7,8,9,10]
even_list1 = []

for n in filter(lambda x : x % 2 == 0, n_list):
    even_list1.append(n)

print('even_list : ', even_list1)


even_list2 = []
even_list2 = list(filter(lambda x : x % 2 == 0, n_list))
print('even_list : ', even_list2)
