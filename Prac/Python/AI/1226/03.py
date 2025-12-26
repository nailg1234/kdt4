import cv2
import numpy as np
# 이미지 읽기
# cv2. imread()

# 기본 읽기 (컬러)
# img = cv2.imread('./1226/image.jpg')
# rgba = cv2.imread('./1226/image1.png', cv2.IMREAD_UNCHANGED)

# if img is None:
#     print('이미지를 읽을 수 없습니다.')
# else:
#     print(f'이미지 크기: {img.shape}')

# if rgba is not None:
#     print(f'알파 포함: {rgba.shape}')


# 읽기 플래그
# cv2.IMREAD_COLOR (1): 컬러, 알파 채널 무시 (기본값)
# cv2.IMREAD_GRAYSCALE : 흑백
# cv2.IMREAD_UNCHANGED (-1) : 알파 채널 포함

'''
OpenCV 지원 이미지 형식:

읽기/쓰기 기능:
- BMP: Windows 비트맵
- JPEG: 손실, 압출, 사진에 적합
- PNG: 무손실, 투명도 지원
- TIFF: 고품질, 다중 페이지
- Webp: 웹 최적화
'''

# 이미지 쓰기
img = np.random.randint(0, 256, (500, 500, 3), dtype=np.uint8)

# 저장
success = cv2.imwrite('output.jpg', img)
print(f'저장 {"성공" if success else "실패"}')

# JPEG 품질 (0-100, 기본값 95)
cv2.imwrite('low_quality.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 30])
cv2.imwrite('high_quality.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])

# PNG 압축 레벨(0~9, 기본값 3)
# 높을수록 파일 작지만 시간 오래 걸림
cv2.imwrite('fast.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
cv2.imwrite('small.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

cv2.imshow('img', img)

# 키 입력 대기
key = cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()
