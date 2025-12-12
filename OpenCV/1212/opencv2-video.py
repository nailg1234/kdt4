import cv2

##### 영상을 윈도우로 띄우기
cap = cv2.VideoCapture("OpenCV/1212/videos/dog.mp4")

### cap.get(int 속성의ID>cv2.[정해진상수])
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 1280.0
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 720.0
print(cap.get(cv2.CAP_PROP_FPS)) # 25.0
print(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # 411.0
print(cap.get(cv2.CAP_PROP_POS_FRAMES)) # 0.0

cap.set(cv2.CAP_PROP_POS_FRAMES, 300)

### cap.isOpened(): bool
# 정상적으로 파일이 열렸는지, 카메라 사용시 카메라가 연결됐는지 확인

### cap.read(): ret, frame 값을 반환
# ret: bool 프레임을 정상적으로 읽었는지 반환
# frame: numpy, 읽어온 영상의 프레임 하나, ret이 false라면 None
# frame은 image 데이터이기 때문에 cv2.imshow()를 통해 화면에 보여줄 수 있음

### cap.release(): 영상 재생이 끝나고 메모리, 카메라 점유 등 자원을 반납



if cap.isOpened():
    while True:
        ret, frame = cap.read()

        if not ret: # ret가 false라면 영상을 모두 재생시킨 것
            print("불러올 프레임이 없어요")
            break

        cv2.imshow("dog video", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
else:
    print("비디오 파일 열기 불가능")

cap.release()
cv2.destroyAllWindows()