
import pandas as pd
import numpy as np

titanic = pd.read_csv("./titanic.csv")

# 타이타닉 승객 연령의 평균 나이
print(titanic["Age"].mean())

# 타이타닉 승객 연령과 탑승권 요금의 중간값
print(titanic[["Age", "Fare"]].median())

# 카테고리별로 그룹화된 통계
print(titanic[["Sex", "Age"]].groupby("Sex").mean())

# 성별 및 승객 등급 조합의 평균 탑승권 요금은 얼마인가?
print(titanic.groupby(["Sex", "Pclass"])["Fare"].mean())

# 각 승객 등급의 수는 몇 명인가?
print(titanic["Pclass"].value_counts())
