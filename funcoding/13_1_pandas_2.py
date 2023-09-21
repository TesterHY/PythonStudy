"""
데이터 프레임

CSV파일을 읽어서 데이터 프레임 생성하기
 - 판다스에서 데이터를 읽는 메소드는 항상 read_xxx()와 같은 형태이고,
   반대로 데이터를 파일에 쓰는 메소드는 to_xxx()의 형태를 가짐

"""

import pandas as pd
import numpy as np

# 파일 읽기
# titanic = pd.read_csv('./titanic.csv')

# 항목 타입 확인
#print(titanic.dtypes)

# 인덱스 변경
# 파일에서 읽을 때 index 를 변경가능함
#titanic = pd.read_csv('./titanic.csv', index_col=0) # 0번째 열을 인덱스로
#print(titanic)

# 데이터 프레임의 몇 개 행을 보려면?
# print(titanic.head(8))

# 데이터 프레임을 엑셀 파일로 저장하려면?
# 필요한 모듈 : pip install openpyxl
# titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False)

# 엑셀파일을 읽기
# titanic2 = pd.read_excel('./titanic.xlsx', sheet_name='passengers')
# print(titanic2)


# 난수로 데이터 프레임 채우기
df = pd.DataFrame(np.random.randint(0, 100, size=(5,4)), columns=list('ABCD'))
print(df)

print(np.random.randint(0, 10, size=(3,3)))

