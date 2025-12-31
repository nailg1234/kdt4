import cv2
import numpy as np
import matplotlib.pyplot as plt


# 객체 탐지
# 이미지에서 객체의 위치(바운딩 박스)와 클래스를 예측
# - 분류: 이미지 전체가 무엇인가?
# - 탐지: 어디에 무엇이 있는가?
# - 분할: 픽셀 단위로 무엇인가?

# 모델 불러오기
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지 읽어오기
img = cv2.imread("Prac/Python/AI&OpenCV/1231/baby.jpg")

# 이미지 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 객체 탐지 알고리즘 실행
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20)
)

# 원본 이미지에 사각형 그리기
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("face recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
