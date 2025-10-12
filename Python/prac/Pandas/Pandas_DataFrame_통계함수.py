import pandas as pd

data = {
"상품명": ["무선 이어폰", "스마트 워치", "텀블러", "노트북", "블루투스 스피커", "무드등"],
"가격": [129000, 250000, 15000, 1200000, 85000, 22000],
"재고": [23, 12, 54, 5, 17, 31]
}
df = pd.DataFrame(data)

# 주요 통계 함수

# 사용 예시 1
print(f'평균(가격) : {df['가격'].mean():.2f}')
print(f'평균(재고) : {df['재고'].mean():.2f}')

print('중앙값(가격) : ', df['가격'].median())
print('중앙값(재고) : ', df['재고'].median())

print('가격 값 개수 : ', df['가격'].count())
print('재고 값 개수 : ', df['재고'].count())


# 사용 예시 2
print(f'표준편차(가격) : {df['가격'].std()}')
print(f'표준편차(재고) : {df['재고'].std()}')

print(f'분산(가격) : {df['가격'].var()}')
print(f'분산(재고) : {df['재고'].var()}')

print(f'최소값(가격) : {df['가격'].min()}')
print(f'최대값(가격) : {df['가격'].max()}')
print(f'합계(가격) : {df['가격'].sum()}')