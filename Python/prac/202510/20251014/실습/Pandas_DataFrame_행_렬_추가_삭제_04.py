import pandas as pd
import numpy as np

# 실습2. 행/열 추가·수정·삭제(4)
# 사용 데이터
df = pd.DataFrame({
'이름': ['A', 'B'],
'나이': [20, 22]
})
# 7. 이름이 'C', 나이가 25, 키가 NaN(결측값)인 새 행을 추가하세요.
# (단, '키'라는 새 열이 자동으로 추가되어야 함)

print('문제7.')
df2 = pd.DataFrame({'이름':['C'], '나이':[25]})
df3 = pd.concat([df, df2])
df3['키'] = [np.nan, np.nan, np.nan]
print('새 행 추가\n', df3)
