"""
[10, 20, 30]과 같은 값을 가진 n_list라는 이름의 리스트를 map() 함수에 넣은 후의 결과는 각각 다음과 같다.

  입력 값의 두 배 : [20, 40, 60]
  입력 값의 세 배 : [30, 60, 90]

"""

# 1. twice()와 triple()라는 이름의 함수를 만들어서 각각 입력 값의 2배와 3배 큰 값을 반환하도록 하시오.
#    그리고 map() 함수를 이용하여 위의 결과와 같이 나오도록 하시오
def twice(x) :
    return x * 2

def triple(x) :
    return x * 3


n_list = [10, 20, 30]
print("입력 값의 두 배 : ", list(map(twice, n_list)))
print("입력 값의 세 배 : ", list(map(triple, n_list)))


# 2. twice()와 triple() 함수를 lambda 함수로 고쳐서 간결하게 변환시키시오.
print("입력 값의 두 배 : ", list(map(lambda x : x * 2, n_list)))
print("입력 값의 세 배 : ", list(map(lambda x : x * 3, n_list)))
