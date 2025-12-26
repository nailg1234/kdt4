import cv2
import numpy as np

# ========================================
# 좌표계와 인덱싱
# ========================================

# OpenCV 좌표계
# 이미지의 원점(0,0)은 왼쪽 위 모서리

#    (0,0) ─────────────► x (width, 가로)
#     │
#     │
#     │    이미지 영역
#     │
#     │
#     ▼
#     y (height, 세로)

# NumPy 인덱싱 방식:
# img[y, x] 또는 img[row, col]
# img[y1:y2, x1:x2]  # 영역 지정

# ⚠️ 중요한 차이점:
# - OpenCV 좌표: (x, y) 순서 - 가로, 세로
# - NumPy 인덱싱: [y, x] 순서 - 행, 열
# 예: 점(100, 50)의 픽셀값 = img[50, 100]




# ========================================
# 픽셀 접근 (읽기/쓰기)
# ========================================

# 테스트용 이미지 생성
img = np.zeros((200, 200, 3), dtype=np.uint8)

# 단일 픽셀 접근 (읽기)
# img[y좌표, x좌표] = img[행, 열]
pixel = img[50, 100]  # y=50, x=100 위치의 픽셀
print(f'픽셀 값 (BGR): {pixel}')  # [0, 0, 0] (검은색)

# 단일 픽셀 설정 (쓰기)
# BGR 순서로 값 지정
img[50, 100] = [200, 0, 0]  # 파란색으로 변경
print(f'변경된 픽셀 값 (BGR): {img[50, 100]}')  # [200, 0, 0]

# 영역 접근 (슬라이싱)
# img[y1:y2, x1:x2] 형식
roi = img[20:80, 50:150]  # 높이 60, 너비 100 영역
print(f'ROI 크기: {roi.shape}')  # (60, 100, 3)

# 영역 전체를 특정 색상으로 설정
img[20:80, 50:150] = [0, 255, 0]  # 초록색으로 채우기


# ========================================
# ROI(Region of Interest) - 관심 영역
# ========================================
# ROI: 이미지에서 특정 작업을 수행할 관심 영역
# 얼굴 검출, 물체 추적 등에서 자주 사용

# 랜덤 이미지 생성
img = np.random.randint(0, 256, (300,400, 3), dtype=np.uint8)
cv2.imshow('Original Image', img)

# ROI 추출 - 좌표와 크기로 지정
x, y, w, h = 100, 50, 200, 150  # x, y: 시작점, w, h: 너비, 높이
roi = img[y:y+h, x:x+w]  # NumPy 인덱싱: [y:y+h, x:x+w]

# ROI 복사 (독립적인 복사본 생성)
# copy() 없이 사용하면 원본 이미지를 참조함
roi_copy = roi.copy()

# ROI 수정 - 원본 이미지에도 영향을 미침
# roi는 img의 일부를 참조하고 있기 때문
roi[:] = [255, 0, 0]  # 파란색으로 채우기
cv2.imshow('Modified Original', img)  # 원본도 변경됨
cv2.imshow('ROI', roi)

# ROI 붙여넣기 - 다른 이미지에 복사
target = np.zeros((300,400,3), dtype=np.uint8)
target[y:y+h, x:x+w] = roi_copy  # 저장해둔 복사본 사용
cv2.imshow('Target with ROI', target)


# ========================================
# 윈도우 플래그 및 조작
# ========================================

# 윈도우 플래그 종류:
# cv2.WINDOW_NORMAL      : 크기 조절 가능 (마우스로 드래그)
# cv2.WINDOW_AUTOSIZE    : 이미지 크기에 맞춤 (기본값, 크기 조절 불가)
# cv2.WINDOW_FULLSCREEN  : 전체 화면 모드
# cv2.WINDOW_FREERATIO   : 비율 자유롭게 조절
# cv2.WINDOW_KEEPRATIO   : 원본 비율 유지

# 윈도우 생성 (크기 조절 가능하게)
cv2.namedWindow('Window', cv2.WINDOW_NORMAL)

# 윈도우 크기 설정
# resizeWindow(윈도우_이름, 너비, 높이)
cv2.resizeWindow('Window', 800, 600)

# 윈도우 위치 이동
# moveWindow(윈도우_이름, x좌표, y좌표)
cv2.moveWindow('Window', 100, 100)  # 화면의 (100, 100) 위치로 이동


# ========================================
# 키 이벤트 처리
# ========================================

# 키보드 입력을 받아 이미지 색상 변경하기
img = np.zeros((300, 400, 3), dtype=np.uint8)

while True:
    cv2.imshow('img', img)

    # waitKey(): 키 입력 대기
    # - 인자: 대기 시간(밀리초). 0이면 무한 대기
    # - 반환값: 눌린 키의 코드 (32비트 정수)
    # - & 0xFF: 하위 8비트만 추출 (64비트 시스템 호환성)
    #   waitKey()는 시스템에 따라 상위 비트에 추가 정보를 포함할 수 있음
    key = cv2.waitKey(30) & 0xFF

    if key == ord('q'):  # 'q' 키: 종료
        print('종료')
        break
    elif key == ord('r'):  # 'r' 키: 빨간색
        img[:] = [0, 0, 255]
        print('빨간색으로 변경')
    elif key == ord('g'):  # 'g' 키: 초록색
        img[:] = [0, 255, 0]
        print('초록색으로 변경')
    elif key == ord('b'):  # 'b' 키: 파란색
        img[:] = [255, 0, 0]
        print('파란색으로 변경')
    elif key == 27:  # ESC 키 (ASCII 코드 27)
        print('ESC로 종료')
        break

# 모든 윈도우 닫기
cv2.destroyAllWindows()

print()
print()
print()
print()
print()
print()