import cv2
import numpy as np

# ========================================
# 이미지에 도형 및 텍스트 그리기
# ========================================
# OpenCV는 이미지에 직접 도형과 텍스트를 그릴 수 있는 함수 제공
# 원본 이미지를 수정하므로 복사본을 만들어 사용하는 것을 권장

# 검은색 캔버스 생성 (그리기용)
canvas = np.zeros((1000, 1200, 3), dtype=np.uint8)

# ========================================
# 1. 선 그리기 (cv2.line)
# ========================================
# cv2.line(img, pt1, pt2, color, thickness, lineType)
# - img: 그릴 이미지 (원본이 수정됨)
# - pt1: 시작점 좌표 (x, y)
# - pt2: 끝점 좌표 (x, y)
# - color: 색상 (B, G, R)
# - thickness: 선 두께 (픽셀 단위, 기본값 1)
# - lineType: 선 종류 (선택사항)
#   - cv2.LINE_4: 4-연결 선 (계단 현상)
#   - cv2.LINE_8: 8-연결 선 (기본값)
#   - cv2.LINE_AA: 안티앨리어싱 (부드러운 선)

# 일반 선 (계단 현상이 보임)
cv2.line(canvas, (50, 150), (550, 450), (0, 0, 255), 2)

# 안티앨리어싱 선 (부드러움)
# LINE_AA는 경계를 부드럽게 처리하여 계단 현상 감소
cv2.line(canvas, (50, 50), (550, 350), (0, 0, 255), 2, cv2.LINE_AA)


# ========================================
# 2. 사각형 그리기 (cv2.rectangle)
# ========================================
# cv2.rectangle(img, pt1, pt2, color, thickness)
# - img: 그릴 이미지
# - pt1: 좌상단 모서리 좌표 (x, y)
# - pt2: 우하단 모서리 좌표 (x, y)
# - color: 색상 (B, G, R)
# - thickness: 선 두께
#   - 양수: 테두리 두께
#   - -1: 내부를 색상으로 채움 (filled)

# 사각형 테두리만
cv2.rectangle(canvas, (50, 50), (200, 150), (0, 0, 255), 2)

# 채워진 사각형
cv2.rectangle(canvas, (250, 50), (400, 150), (0, 255, 0), -1)


# ========================================
# 3. 원 그리기 (cv2.circle)
# ========================================
# cv2.circle(img, center, radius, color, thickness)
# - img: 그릴 이미지
# - center: 원의 중심 좌표 (x, y)
# - radius: 반지름 (픽셀)
# - color: 색상 (B, G, R)
# - thickness: 선 두께 (-1이면 채움)

# 원 테두리만
cv2.circle(canvas, (150, 250), 50, (255, 0, 0), 2)

# 채워진 원
cv2.circle(canvas, (350, 250), 50, (255, 0, 0), -1)


# ========================================
# 4. 타원 그리기 (cv2.ellipse)
# ========================================
# cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
# - img: 그릴 이미지
# - center: 타원의 중심 좌표 (x, y)
# - axes: 축의 길이 (장축 절반, 단축 절반)
# - angle: 타원 회전 각도 (시계방향, 도 단위)
# - startAngle: 호의 시작 각도 (0도 = 오른쪽)
# - endAngle: 호의 끝 각도
# - color: 색상 (B, G, R)
# - thickness: 선 두께 (-1이면 채움)

# 채워진 타원 (45도부터 360도까지 그리기)
cv2.ellipse(canvas, (550, 350), (80, 40), 0, 45, 360, (255, 0, 0), -1)


# ========================================
# 5. 텍스트 추가 (cv2.putText)
# ========================================
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)
# - img: 그릴 이미지
# - text: 표시할 텍스트 (문자열)
# - org: 텍스트 시작 위치 (좌하단 기준점) (x, y)
# - fontFace: 글꼴 종류
# - fontScale: 글자 크기 배율 (1.0 = 기본 크기)
# - color: 색상 (B, G, R)
# - thickness: 글자 두께 (픽셀)
# - lineType: 선 종류 (cv2.LINE_AA 권장)

cv2.putText(
    canvas,
    'Hello OpenCV!',  # 텍스트
    (700, 100),       # 위치 (좌하단 기준)
    cv2.FONT_HERSHEY_SIMPLEX,  # 글꼴
    2,                # 크기
    (255, 255, 255),  # 흰색
    2,                # 두께
    cv2.LINE_AA       # 안티앨리어싱
)


# ========================================
# 결과 표시
# ========================================
cv2.imshow('Drawing Shapes', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
========================================
사용 가능한 글꼴 (fontFace)
========================================

cv2.FONT_HERSHEY_SIMPLEX        : 기본 산세리프체 (가장 많이 사용)
cv2.FONT_HERSHEY_PLAIN          : 작은 크기의 산세리프체
cv2.FONT_HERSHEY_DUPLEX         : 복잡한 산세리프체
cv2.FONT_HERSHEY_COMPLEX        : 더 복잡한 산세리프체
cv2.FONT_HERSHEY_TRIPLEX        : 더욱 복잡한 산세리프체
cv2.FONT_HERSHEY_COMPLEX_SMALL  : HERSHEY_COMPLEX의 작은 버전
cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일
cv2.FONT_HERSHEY_SCRIPT_COMPLEX : 복잡한 필기체
cv2.FONT_ITALIC                 : 이탤릭체 플래그 (다른 폰트와 OR 연산)

예: cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC (이탤릭 적용)
'''

'''
========================================
기타 그리기 함수
========================================

cv2.polylines()     : 다각형 그리기 (여러 점 연결)
cv2.fillPoly()      : 채워진 다각형
cv2.drawContours()  : 윤곽선 그리기
cv2.arrowedLine()   : 화살표 선

예제:
# 삼각형 그리기
points = np.array([[100,100], [200,50], [300,100]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(img, [points], True, (0,255,0), 2)

# 화살표
cv2.arrowedLine(img, (50,50), (200,200), (255,0,0), 3)
'''

'''
========================================
활용 팁
========================================

1. 원본 보존: 그리기 전에 이미지 복사
   img_copy = img.copy()

2. 반투명 그리기: addWeighted 사용
   overlay = img.copy()
   cv2.rectangle(overlay, (100,100), (200,200), (0,255,0), -1)
   cv2.addWeighted(overlay, 0.5, img, 0.5, 0, img)

3. 텍스트 크기 확인: getTextSize 사용
   (w, h), baseline = cv2.getTextSize('Text', cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

4. 중심에 텍스트 배치:
   text = 'Centered'
   (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
   x = (img.shape[1] - w) // 2
   y = (img.shape[0] + h) // 2
   cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
'''