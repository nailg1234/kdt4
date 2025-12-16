import cv2 as cv

cap = cv.VideoCapture(0) # 경로명이 아닌 기기 id
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv.imshow('camera', img)
            if cv.waitKey(10) != -1:
                cv.imwrite("OpenCV/1212/output/camera_capture.jpg", img)
                break

cap.release()
cv.destroyAllWindows()