import pandas as pd
import numpy as np

'''
    결측값 : 데이터에 값이 기록되지 않은 상태
    Pandas의 결측값 : NaN(Not a Number, float), None(object), NA 등
    
    결측값이 있는 데이터의 문제점
    - 통계, 분석, 모델링 시 오류, 왜곡 발생할 수 있음
    -> 따라서 탐색, 전처리 단계에서 결측값 처리 반드시 해야함!
'''

'''
    < 결측값 탐지 >
    df.isnull()
    df.notnull()
'''

data = {
    "이름": ["서준", np.nan, "민준", "서연", "하은", "지민"],
    "나이": [22, 28, np.nan, 31, np.nan, 24],
    "점수": [89, np.nan, 83, 90, 88, np.nan],
    "성별": ["남", "여", "남", np.nan, "여", "여"],
    "국적": ["한국","한국","한국","한국","한국","한국"]
}

df = pd.DataFrame(data)
print('==================================================')
print('===== < 결측값 탐지 > =====')
print(df)
print()
print('컬럼별 결측 값 개수 : \n', df.isnull().sum())
print()
print('전체 결측값 개수 : ', df.isnull().sum().sum())
print()
print('결측값 아닌 데이터 확인 : \n', df.notnull())
print()

'''
    < 결측값 제거 >
    df.dropna(axis = 0, how = 'any', inplace=False)
    axis
        axis = 0 : 결측값이 있는 행 삭제 (기본 값)
        axis = 1 : 결측값이 있는 열 삭제
    how
        how = 'any' : 하나라도 결측값이 있으면 삭제
        how = 'all' : 모두 결측값인 행/열 삭제
    inplace
        inplace = True : 원본 데이터 프레임에서 바로 삭제 (반환 값 X)
        inplace = False : 삭제된 새로운 데이터 프레임 반환
'''
print('==================================================')
print('===== < 결측값 제거 > =====')
print(df)
print()
print('결측값 있는 전체 행 삭제 : \n', df.dropna())
print()
print('결측값 있는 열 삭제 : \n', df.dropna(axis=1))
print()
print('모두 결측값인 행만 삭제 : \n', df.dropna(how='all'))
print()

'''
    < 결측값 대체 >
    df.fillna(value, method=None, inplace=False)
    value : 특정 값으로 채움
    method
        method = 'ffill' : 이전 값으로 채움
        method = 'bfill' : 다음 값으로 채움
    inplace
        inplace = True : 원본 데이터 프레임에서 바로 대체 (반환 값 X)
        inplace = False : 대체한 새로운 데이터 프레임 반환
'''
print('==================================================')
print('===== < 결측값 대체 > =====')
print(df)
print()
print('모든 결측값 0으로 채움 : \n', df.fillna(0))
print()
print('각 컬럼별 평균값으로 결측값 대체 : \n', df.fillna(df.mean(numeric_only=True)))
print()
print('이전 값으로 채움 : \n', df.fillna(method='ffill'))
print()
print('이전 값으로 채움 : \n', df.ffill()) # 파이썬에서 권장 하는듯?
print()
print('다음 값으로 채움 : \n', df.bfill()) # 파이썬에서 권장 하는듯?