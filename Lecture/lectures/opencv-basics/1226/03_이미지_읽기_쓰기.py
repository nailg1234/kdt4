import cv2
import numpy as np

# ========================================
# 이미지 읽기 (cv2.imread)
# ========================================

# 기본 읽기 (컬러 모드, 기본값)
# imread(파일경로, 플래그)
# 반환값: NumPy 배열 (성공) 또는 None (실패)
img = cv2.imread('./1226/image.jpg')

# 알파 채널 포함하여 읽기 (PNG 등에서 투명도 정보)
rgba = cv2.imread('./1226/image1.png', cv2.IMREAD_UNCHANGED)

# 이미지 로드 실패 확인 (중요!)
# 파일이 없거나, 손상되었거나, 지원하지 않는 형식일 경우 None 반환
if img is None:
    print('이미지를 읽을 수 없습니다.')
    print('경로, 파일 존재 여부, 형식을 확인하세요.')
else:
    print(f'이미지 크기 (높이, 너비, 채널): {img.shape}')

if rgba is not None:
    print(f'알파 포함 이미지 shape: {rgba.shape}')  # (높이, 너비, 4)


# ========================================
# imread 플래그 옵션
# ========================================
# cv2.IMREAD_COLOR (1)        : 컬러로 읽기, 알파 채널 무시 (기본값)
# cv2.IMREAD_GRAYSCALE (0)    : 흑백(그레이스케일)으로 읽기
# cv2.IMREAD_UNCHANGED (-1)   : 원본 그대로 읽기 (알파 채널 포함)

# 예제: 흑백으로 읽기
gray = cv2.imread('./1226/image.jpg', cv2.IMREAD_GRAYSCALE)
if gray is not None:
    print(f'흑백 이미지 shape: {gray.shape}')  # (높이, 너비) - 2차원

'''
========================================
OpenCV 지원 이미지 형식
========================================

읽기/쓰기 모두 지원:
- BMP: Windows 비트맵 (무압축, 용량 큼)
- JPEG/JPG: 손실 압축, 사진에 적합 (투명도 미지원)
- PNG: 무손실 압축, 투명도 지원 (웹/그래픽에 적합)
- TIFF: 고품질, 다중 페이지 지원 (전문 분야)
- WebP: 웹 최적화 (Google 개발, 압축률 우수)

기타 지원 형식:
- PBM, PGM, PPM: Portable 이미지 형식
- SR, RAS: Sun Raster 형식
- EXR: HDR 이미지 (OpenEXR)
'''

# ========================================
# 이미지 쓰기 (cv2.imwrite)
# ========================================

# 테스트용 랜덤 이미지 생성
img = np.random.randint(0, 256, (2000, 2000, 3), dtype=np.uint8)

# 기본 저장
# imwrite(파일경로, 이미지배열, [옵션])
# 반환값: 성공 시 True, 실패 시 False
success = cv2.imwrite('output.jpg', img)
print(f'저장 {'성공' if success else '실패'}')

# ========================================
# JPEG 저장 옵션
# ========================================
# JPEG 품질: 0~100 (기본값 95)
# - 높을수록: 화질 좋음, 파일 크기 큼
# - 낮을수록: 화질 나쁨, 파일 크기 작음

cv2.imwrite('low_quality.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 30])   # 저품질
cv2.imwrite('high_quality.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])  # 최고품질

# ========================================
# PNG 저장 옵션
# ========================================
# PNG 압축 레벨: 0~9 (기본값 3)
# - 0: 압축 없음 (빠르지만 파일 큼)
# - 9: 최대 압축 (느리지만 파일 작음)
# ⚠️ 무손실 압축이므로 화질은 동일

cv2.imwrite('fast_png.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # 빠른 저장
cv2.imwrite('small_png.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])  # 작은 파일


# ========================================
# 이미지 표시 및 종료
# ========================================

# 이미지를 윈도우에 표시
cv2.imshow('Random Image', img)

# 키 입력 대기 (아무 키나 누르면 종료)
key = cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()

'''
========================================
imwrite 추가 옵션들
========================================

WebP:
- cv2.IMWRITE_WEBP_QUALITY: 1~100 (기본값 100)

PNG:
- cv2.IMWRITE_PNG_STRATEGY: 압축 전략
  - cv2.IMWRITE_PNG_STRATEGY_DEFAULT
  - cv2.IMWRITE_PNG_STRATEGY_FILTERED
  - cv2.IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY

TIFF:
- cv2.IMWRITE_TIFF_COMPRESSION: 압축 방식

사용 예:
cv2.imwrite('image.webp', img, [cv2.IMWRITE_WEBP_QUALITY, 80])
cv2.imwrite('image.png', img,
            [cv2.IMWRITE_PNG_COMPRESSION, 5,
             cv2.IMWRITE_PNG_STRATEGY, cv2.IMWRITE_PNG_STRATEGY_DEFAULT])
'''
