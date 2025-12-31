from ultralytics import YOLO
import cv2

# YOLO모델을 불러옴
model = YOLO("Prac/Python/AI&OpenCV/1231/yolov5s.pt")
img = cv2.imread("Prac/Python/AI&OpenCV/1231/baby.jpg")

# 신뢰도 0.5로 객체 탐지
results = model.predict(img, conf=0.5)

# 탐지 결과를 이미지 위에 그림
annotated_frame = results[0].plot()

cv2.imshow("img", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
