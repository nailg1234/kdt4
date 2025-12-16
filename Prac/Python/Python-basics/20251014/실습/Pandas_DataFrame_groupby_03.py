import pandas as pd
# 실습4. groupby 연습문제(3)
# 3. 아래 DataFrame에서 지역(region)별 판매자(seller)별로 판매액(sales)의 합계와 최대값
# 을 구하세요.
df = pd.DataFrame({
'region': ['Seoul', 'Seoul', 'Busan', 'Busan', 'Daegu', 'Daegu'],
'seller': ['A', 'B', 'A', 'B', 'A', 'A'],
'sales': [100, 200, 150, 120, 130, 200]
})


print('지역별, 판매자별 판매액 합계, 최대값\n',
      df.groupby(['region','seller'])['sales'].agg(['sum', 'max']))
