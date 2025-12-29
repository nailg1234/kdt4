"""
OpenCV 기초 - 03. 비트 연산과 마스킹

이 파일에서 배울 내용:
1. 비트 연산(AND, OR, XOR, NOT)이 무엇인지
2. 마스크를 만들고 사용하는 방법
3. 마스크를 이용해서 이미지의 특정 부분만 선택하거나 합성하기
"""

import cv2
import numpy as np

# ============================================================
# 1. 비트 연산 이해하기
# ============================================================
"""
비트 연산이란?
- 이미지의 각 픽셀값을 0과 1로 생각하고 논리 연산을 하는 것
- 마스크(선택 영역)를 만들 때 매우 유용해요!

주요 비트 연산:
- AND (교집합): 두 영역이 모두 겹치는 부분만
- OR (합집합): 두 영역 중 하나라도 포함되는 모든 부분
- XOR (배타적 논리합): 두 영역이 겹치지 않는 부분만
- NOT (반전): 검은색↔흰색 뒤집기
"""

h, w = 300, 300

# 원형 마스크 만들기
circle_mask = np.zeros((h, w), dtype=np.uint8)  # 검은색 바탕
cv2.circle(circle_mask, (150, 150), 100, 255, -1)  # 흰색 원 그리기
# -1은 원을 채우라는 의미

# 사각형 마스크 만들기
rect_mask = np.zeros((h, w), dtype=np.uint8)  # 검은색 바탕
cv2.rectangle(rect_mask, (100, 100), (200, 200), 255, -1)  # 흰색 사각형 그리기
# -1은 사각형을 채우라는 의미

# 다양한 비트 연산 수행하기
and_mask = cv2.bitwise_and(circle_mask, rect_mask)  # AND: 원과 사각형이 겹치는 부분
or_mask = cv2.bitwise_or(circle_mask, rect_mask)    # OR: 원과 사각형을 합친 전체
xor_mask = cv2.bitwise_xor(circle_mask, rect_mask)  # XOR: 겹치지 않는 부분만
not_mask = cv2.bitwise_not(circle_mask)             # NOT: 원 영역을 반전 (흰색↔검은색)

# 개별 마스크 확인
cv2.imshow('1. Circle Mask (원)', circle_mask)
cv2.imshow('2. Rectangle Mask (사각형)', rect_mask)

# 모든 비트 연산 결과를 한 줄로 나란히 배치
result = np.hstack([
    circle_mask, rect_mask,   # 원본 2개
    and_mask, or_mask,         # AND, OR
    xor_mask, not_mask         # XOR, NOT
])

cv2.imshow('Bitwise Operations (비트 연산 결과)', result)
print("비트 연산 결과를 확인하세요!")
print("왼쪽부터: 원, 사각형, AND, OR, XOR, NOT")
cv2.waitKey(0)
cv2.destroyAllWindows()


# ============================================================
# 2. 마스크를 이용한 이미지 합성
# ============================================================
"""
마스킹이란?
- 이미지의 특정 부분만 선택하거나 숨기는 기술
- 사진 배경 바꾸기, 워터마크, 로고 합성 등에 사용

실생활 예시:
- 증명사진 배경 바꾸기
- 유튜브 썸네일에 이미지 합성하기
- 게임에서 캐릭터와 배경 합성
"""

# 원본 이미지 생성 (파란색 계열 랜덤 이미지)
img = np.random.randint(100, 200, (300, 300, 3), dtype=np.uint8)
img[:, :, 0] = 200  # Blue 채널을 강조해서 파란색 느낌

# 원형 마스크 생성 (원 안쪽만 선택)
mask = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(mask, (150, 150), 100, 255, -1)

# 1단계: 마스크로 원본 이미지의 원 부분만 추출
masked = cv2.bitwise_and(img, img, mask=mask)
# mask=mask는 "mask가 흰색(255)인 부분만 보여줘"라는 의미

# 2단계: 새로운 배경 만들기
background = np.zeros_like(img)  # 원본과 같은 크기
background[:] = [0, 0, 255]  # 빨간색 배경 (BGR 순서)

# 3단계: 마스크를 반전시켜서 원 바깥 부분만 선택
inv_mask = cv2.bitwise_not(mask)  # 흰색↔검은색 뒤집기
bg_part = cv2.bitwise_and(background, background, mask=inv_mask)
# 빨간 배경의 원 바깥 부분만 추출

# 4단계: 원 안쪽(원본)과 원 바깥쪽(빨간 배경)을 합성
result = cv2.add(masked, bg_part)

# 결과를 나란히 배치해서 보여주기
display = np.hstack([img, masked, result])
cv2.imshow('Masking (마스킹 결과)', display)
print("\n마스킹 결과:")
print("왼쪽: 원본 이미지")
print("중간: 마스크 적용 (원 부분만)")
print("오른쪽: 배경 합성 (원 안은 원본, 밖은 빨간색)")
cv2.waitKey(0)
cv2.destroyAllWindows()