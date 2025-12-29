import cv2
import numpy as np

# 비트 연산과 마스킹


h, w = 300, 300
# 원 마스크 생성
circle_mask = np.zeros((h, w), dtype=np.uint8)
cv2.circle(circle_mask, (150, 150), 100, 255, -1)

# 사각형 마스크 생성
rect_mask = np.zeros((h, w), dtype=np.uint8)
cv2.rectangle(rect_mask, (100, 100), (200, 200), 255, -1)

# 비트 연산
and_mask = cv2.bitwise_and(circle_mask, rect_mask)  # 교집합
or_mask = cv2.bitwise_or(circle_mask, rect_mask)  # 합집합
xor_mask = cv2.bitwise_xor(circle_mask, rect_mask)  # 배타적 논리합
not_mask = cv2.bitwise_not(circle_mask)  # 반전

result = np.hstack([
    circle_mask, rect_mask,
    and_mask, or_mask,
    xor_mask, not_mask,])

cv2.imshow('rect', rect_mask)
cv2.imshow('circle', circle_mask)
cv2.imshow('bitwise operations', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 마스크 적용
# 원본 이미지 (임시 생성)
img = np.random.randint(100, 200, (300, 300, 3), dtype=np.uint8)
img[:, :, 0] = 200  # Blue 강조

# 원형 마스크 생성
mask = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(mask, (150, 150), 100, 255, -1)

# 마스크 적용
masked = cv2.bitwise_and(img, img, mask=mask)

# 배경 변경
background = np.zeros_like(img)
background[:] = [0, 0, 255]  # 빨간 배경

# 마스크 반전으로 배경 추출
inv_mask = cv2.bitwise_not(mask)
bg_part = cv2.bitwise_and(background, background, mask=inv_mask)

# 합성
result = cv2.add(masked, bg_part)

# 시각화
display = np.hstack([img, masked, result])
cv2.imshow('Masking', display)
cv2.waitKey(0)
cv2.destroyAllWindows()
