"""
다음 리스트의 요소를 선택 정렬을 이용해 오름차순으로 정렬하는 코드를 작성하라

data = ["A", "L", "G", "O", "R", "I", "T", "H", "M"]

"""

def selection_sort(A):

    for i in range(len(A)-1):
        least = i
        for j in range(i+1, len(A)):
            if (A[j] < A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i+1)


def printStep(arr, val):
    print("  Step %2d = " % val, end = '')
    print(arr)

data = ["A", "L", "G", "O", "R", "I", "T", "H", "M"]
print("Original : ", data)
selection_sort(data)
print("Selection : ", data)



