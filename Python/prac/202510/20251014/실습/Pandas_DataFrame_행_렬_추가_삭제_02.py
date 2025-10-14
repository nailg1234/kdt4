import pandas as pd
# 실습2. 행/열 추가·수정·삭제(2)
# 사용 데이터
df = pd.DataFrame({
'제품': ['A', 'B'],
'가격': [1000, 2000]
})
# 3. 제품 'C', 가격 1500인 새 행을 추가하세요.
print('문제3.')
df2 = pd.DataFrame({'제품':['C'], '가격':[1500]})
df3 = pd.concat([df, df2], ignore_index=True)
print('제품C, 가격1500추가\n', df3)
print()
# 4. 3번 문제의 DataFrame에서 첫 번째 행(제품 'A')을 삭제하세요.
print('문제4.')
print('첫번째 행 삭제\n', df3.drop(0))
