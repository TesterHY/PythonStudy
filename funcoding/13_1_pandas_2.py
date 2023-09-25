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
#df = pd.DataFrame(np.random.randint(0, 100, size=(5,4)), columns=list('ABCD'))
#print(df)

#print(np.random.randint(0, 10, size=(3,3)))



# 타이타닉 데이터에서 승객의 나이만 추출하려면?
titanic = pd.read_csv('./titanic.csv')
ages = titanic["Age"]
#print(ages.head())

# 타이타닉 탑승객의 이름, 나이, 성별을 동시에 알고 싶으면?
nameAgeSex = titanic[["Name", "Age", "Sex"]]
#print(nameAgeSex)

# 20세 미만의 승객만 추리려면?
# 필터링 : 조건을 주어 특정 행을 골라 내는 것 - 괄호 안에 조건을 주어 필터링 가능

below_20 = titanic[titanic["Age"] < 20]
print(below_20.head())

# 1등석이나 2등석에 탑승한 승객들을 출력하려면?
# - 조건식과 유사하게 isin() 함수는 제공된 리스트에 있는 값들이 들어 있는 각 행에 대하여 True를 반환함
# - df["Pclass"].isin([1,2])은 Pclass열이 1 또는 2인 행을 확인함
pclass1_2 = titanic[titanic["Pclass"].isin([1, 2])]
print(pclass1_2)

# 20세 미만의 승객 이름에만 관심이 있다면?
# - 어떤 조건을 주어서 행을 선택한 후에 특정 열만 추출하기
# - loc연산자 : 레이블 기반 인덱싱]
# df.loc[조건, 열레이블] -> df : 데이터 프레임, 조건 : 추출 조건, 열레이블 : 추출할 열 레이블
below_20_Name = titanic.loc[titanic["Age"] < 20, "Name"]
print(below_20_Name)


# 20행에서 23행, 5열에서 7열에만 관심이 있다면?
rowcol = titanic.iloc[20:24, 5:7]
print(rowcol)

# 데이터를 정렬하는 방법
# sort_values()를 사용하면 테이블의 행이 지정된 열에 따라 정렬
sortAge = titanic.sort_values(by="Age").head()
print(sortAge)

sortPclassAge = titanic.sort_values(by=["Pclass", "Age"], ascending=False).head()
print(sortPclassAge)