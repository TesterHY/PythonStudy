"""
피봇 테이블

- 데이터를 다른 관점으로 관찰할 수 있게 도움을 줌

"""


# 사용 데이터
# 타이타닉 데이터셋에서 몇몇 컬럼 삭제후 진행

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic = pd.read_csv('./titanic.csv')
titanic.drop(['PassengerId', 'Ticket', 'Name'], inplace=True, axis=1)
print(titanic.head())

# 피봇 테이블에서 인덱스를 사용하여 데이터를 그룹화하기
# pivot_table()
# data : 함수에 전달하는 데이터 프레임
# index : 데이터를 그룹화할 수 있는 열

# table = pd.pivot_table(data=titanic, index=['Sex'])
# print(table)
# table.plot(kind="bar")
# plt.show()

# 특징별로 집계 함수 적용
# - aggfunc는 pivot_table이 그룹화된 데이터에 적용하는 집계함수
# - 기본은 np.mean(), 하지만 다른 집계 함수 사용가능
# table = pd.pivot_table(data=titanic, index=["Sex", "Pclass"], aggfunc={"Age": np.mean, "Survived":np.sum})
# print(table)


# - value 매개 변수를 사용하여 특정한 데이터에 대한 집계
#  - Pclass가 낮을 수록, 남성이 여성보다 생존률이 낮음
#  - 관찰하기 힘듦
# table = pd.pivot_table(data=titanic, index=['Sex', 'Pclass'], values=['Survived'], aggfunc=np.mean)
# print(table)
# table.plot(kind='bar')
# plt.show()

# 데이터 간의 관계 찾기
table = pd.pivot_table(data=titanic, index=['Sex'], columns=['Pclass'], values=['Survived'], aggfunc=np.sum)
print(table)
table.plot(kind='bar')
plt.show()