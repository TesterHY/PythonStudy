"""
데이터로 차트 그리기

- matplot 라이브러리를 사용하여 여러가지 형태의 차트를 그릴 수 있음
- df.plot() : 인덱스에 대하여 모든 열을 그리기
- df.plot(x='col1') : 하나의 열만을 그리기
- df.plot(x='col1', y='col2') : 특정 열에 대하여 다른 열 그리기

"""

# 예제

import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    'name' : ['Kim', 'Lee', 'Park', 'Choi', 'Hong', 'Chung', 'Jang'],
    'age' : [22, 26, 78, 17, 46, 32, 21],
    'city' : ['Seoul', 'Daegu', 'Seoul', 'Busan', 'Seoul', 'Daegu', 'Daejun'],
    'children' : [2, 3, 0, 1, 3, 4, 3],
    'pets' : [0, 1, 0, 2, 2, 0, 3]
})

# 선 차트
#df.plot(kind='line', x='name', y='pets', color='red')
#plt.show()

# 중첩 차트
# ax = plt.gca() # 중첩차트 그리기 gca : get current axis
# df.plot(kind='line', x='name', y='children', ax=ax)
# df.plot(kind='line', x='name', y='pets', color='red', ax=ax)
# plt.show()

# 막대그래프
# df.plot(kind='bar', x='name', y='age')
# plt.show()

# 산포도 그리기
# df.plot(kind='scatter', x='children', y='pets', color='red')
# plt.show()

# 그루핑하여 그리기
# 도시별로 그루핑한 후, 유일한 이름의 개수를 계산
# df.groupby('city')['name'].nunique().plot(kind='bar')
# plt.show()

# 히스토그램 그리기
# 히스토그램 : 데이터를 다양한 "빈" 또는 "범위 그룹"으로 분류하고 해당 빈 각각에 속하는 데이터 포인트 수를 계산
df[['age']].plot(kind='hist', bins=[0, 20, 40, 60, 80, 100], rwidth=0.8)
plt.show()