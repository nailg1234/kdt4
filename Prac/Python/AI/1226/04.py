# 비디오 읽기
import cv2
import numpy as np

# 비디오 파일 읽기
cap = cv2.VideoCapture("Prac/Python/AI/1226/videos/dog.mp4")

# 열기 확인
if not cap.isOpened():
    print('비디오를 열 수 없습니다!.')
    exit()
else:
    # 비디오 속성 읽기
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fps (Frames Per Second)
    # 1초에 몇 프레임을 보여주는지
    # 120fps = 1초에 120장의 사진을 재생 한다
    # 60fps = 1초에 60장의 사진을 재생 한다
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # 총 프레임 수
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # 코덱 식별자
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

    print(f'해상도: {width}x{height}')
    print(f'fps: {fps}')
    print(f'frame_count: {frame_count}')
    print(f'재생 시간: {frame_count/fps}')
    print(f'코덱: {fourcc}')

# 특정 프레임으로 이동
frame_number = 300
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# 시간으로 이동(밀리초)
time_ms = 5000
cap.set(cv2.CAP_PROP_POS_MSEC, time_ms)


# 프레임 읽기
ret, frame = cap.read()

if ret:
    print(f'현재 프레임: {int(cap.get(cv2.CAP_PROP_POS_FRAMES))}')
    cv2.imshow('frame', frame)
    cv2.waitKey(0)


# 프레임 읽기
# while True:
#     ret, frame = cap.read()

#     if not ret:
#         print('프레임 읽기 끝')
#         break

#     cv2.imshow("Video", frame)

#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# # 비디오 속성 설정
# width, height = 640, 480
# fps = 30

# # FourCC 코드(코덱 지정)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4

# # VideoWriter 생성
# out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# for i in range(fps * 5):  # 5초 비디오
#     # 그라데이션 프레임 생성
#     frame = np.zeros((height, width, 3), dtype=np.uint8)
#     frame[:, :, 0] = int(255 * i / (fps * 5))  # Blue 증가

#     out.write(frame)

# out.release()
# print('비디오 저장 완료')


# 웹캠으로 녹화
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('recording.mp4', fourcc, fps, (width, height))

recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 녹화 상태 표시
    if recording:
        cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
        cv2.putText(frame, 'REC', (50, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        out.write(frame)

    cv2.imshow('Recording', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        recording = not recording
        print(f'녹화: {"시작" if recording else "중지"}')
    elif key == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
