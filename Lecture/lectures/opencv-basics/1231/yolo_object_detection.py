
import cv2

# 눈 모델 로드 (OpenCV 기본 제공 경로 사용)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

img = cv2.imread("1231/eye_detection_boy.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(60, 60)
)

for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow("eye detection", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from ultralytics import YOLO

model = YOLO('yolo11n.pt')

img = cv2.imread('1231/yolo_street_scene.jpg')

results = model.predict(img, conf=0.5)

annotated_frame = results[0].plot()


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("카메라를 열 수 없습니다.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO 추론
    results = model.predict(frame, conf=0.5)

    # 바운딩 박스 + 라벨 그린 프레임
    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Webcam", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# cv2.imshow('img', annotated_frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

