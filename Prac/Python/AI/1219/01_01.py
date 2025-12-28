from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'age': [25, 30, np.nan, 45, np.nan, 35],
    'income': [50000, np.nan, 60000, 80000, 55000, np.nan],
    'city': ['서울', '부산', np.nan, '대구', '서울', '인천']
})

print('=== 결측치 확인 ===')
print(df.isnull().sum())
# === 결측치 확인 ===
# age       2
# income    2
# city      1
# dtype: int64

# 1. 결측치 처리
# 방법 1: 삭제
df_drop = df.dropna()
print(f'원본: {len(df)}행 => 삭제 후: {len(df_drop)}행')
# 원본: 6행 => 삭제 후: 2행

# 방법 2: 채우기
df['age'].fillna(df['age'].median(), inplace=True)    # 중앙값
df['income'].fillna(df['income'].mean(), inplace=True)  # 평균
df['city'].fillna(df['city'].mode()[0], inplace=True)  # 최빈값
print(df.isnull().sum())
# age       0
# income    0
# city      0
# dtype: int64


# 2. 범주형 데이터 인코딩 (Encoding)
# 방법 1: map()으로 수동 매핑
df = pd.DataFrame({
    'sex': ['male', 'female', 'male', 'female']
})

df['sex_encoded'] = df['sex'].map({'male': 0, 'female': 1})
print(df)
#       sex  sex_encoded
# 0    male            0
# 1  female            1
# 2    male            0
# 3  female            1

# 방법 2: LabelEncoder
df = pd.DataFrame({
    'city': ['서울', '부산', '대전', '대구', '서울', '인천']
})

le = LabelEncoder()
df['city_encoded'] = le.fit_transform(df['city'])
print(df)
#   city  city_encoded
# 0   서울             3
# 1   부산             2
# 2   대전             1
# 3   대구             0
# 4   서울             3
# 5   인천             4

# 방법 3: One-Hot Encoding
df = pd.DataFrame({
    'city': ['서울', '부산', '대전']
})

df_encoded = pd.get_dummies(df, columns=['city'], prefix='city')
print(df_encoded)
#    city_대전  city_부산  city_서울
# 0    False    False     True
# 1    False     True    False
# 2     True    False    False
