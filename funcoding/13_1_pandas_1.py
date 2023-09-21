"""
판다스

- 강력한 데이터 구조를 사용하여 고성능 데이터 조작 및 데이터 분석에 사용되는 
  오픈 소스 파이썬 라이브러리
- 통계 분석용 언어로 활용 가능
- 재무, 경제, 통계, 관고, 웹 분석 등 다양한 영역에서 활용
- 2차원 형태의 데이털르 자유롭게 활용 가능


자료 구조

1. 시리즈(Series) : 동일한 유형의 데이터를 저장하는 1차원 배열

2. 데이터 프레임(Data Frame) : 각 열마다 동일한 유형의 데이터를 저장하는 2차원 배열

"""

"""
타이타닉 데이터셋
https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/02_read_write.html

"""

import pandas as pd
import numpy as np

#titanic = pd.read_csv('titanic.csv')
#print('titanic : ' , titanic)
#print('titanic Age : ', titanic['Age'])
#print('titanic Age Max : ', titanic['Age'].max())
#print('describe() : ', titanic.describe())

# 데이터 시리즈 생성하기
# - 시리즈는 이름이 붙여진 1차원적인 배열이나 마찬가지임
# - 가장 기본적인 방법은 파이썬의 리스트에서 생성하는 것
data = ['Kim', 'Park', 'Lee', 'Choi']
ser = pd.Series(data)

print(ser)
print(ser[0])

data2 = {'Name':['Kim', 'Park', 'Lee', 'Choi']
         , 'Age':[20, 23, 21, 26]}

df = pd.DataFrame(data2, index=['학번1', '학번2', '학번3', '학번4'])

print(df)
