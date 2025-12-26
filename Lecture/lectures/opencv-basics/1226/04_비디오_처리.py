import cv2
import numpy as np

# ========================================
# 비디오 처리
# ========================================
# OpenCV는 비디오 파일 읽기/쓰기와 웹캠 제어를 지원
# VideoCapture: 비디오 읽기 (파일 또는 카메라)
# VideoWriter: 비디오 쓰기 (저장)

'''
========================================
1. 비디오 파일 읽기
========================================
'''

# 비디오 파일 열기 예제 (주석 처리됨 - 비디오 파일이 필요)
# cap = cv2.VideoCapture('./1226/video.mp4')
#
# # 비디오가 제대로 열렸는지 확인
# if not cap.isOpened():
#     print('비디오를 열 수 없습니다!')
#     exit()
# else:
#     # ========================================
#     # 비디오 속성 읽기
#     # ========================================
#
#     # 프레임 해상도
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
#     # FPS (Frames Per Second) - 초당 프레임 수
#     # 120fps = 1초에 120장의 이미지를 재생
#     # 60fps = 1초에 60장의 이미지를 재생
#     # 높을수록 부드러운 영상
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#
#     # 총 프레임 수
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#
#     # 코덱 식별자 (FourCC)
#     # FourCC: 4개의 문자로 비디오 코덱을 식별하는 코드
#     fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
#
#     print(f'해상도: {width}x{height}')
#     print(f'FPS: {fps}')
#     print(f'총 프레임 수: {frame_count}')
#     print(f'재생 시간: {frame_count / fps:.2f}초')
#     print(f'코덱: {fourcc}')

'''
========================================
비디오 탐색 (특정 위치로 이동)
========================================
'''

# # 특정 프레임 번호로 이동
# frame_number = 200
# cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
#
# # 특정 시간(밀리초)으로 이동
# time_ms = 5000  # 5초 위치로 이동
# cap.set(cv2.CAP_PROP_POS_MSEC, time_ms)
#
# # 해당 위치의 프레임 읽기
# ret, frame = cap.read()
# # ret: 읽기 성공 여부 (True/False)
# # frame: 읽은 프레임 이미지 (NumPy 배열)
#
# if ret:
#     current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
#     print(f'현재 프레임: {current_frame}')
#     cv2.imshow('Frame', frame)
#     cv2.waitKey(0)

'''
========================================
비디오 전체 재생 (프레임 단위 반복)
========================================
'''

# # 비디오의 모든 프레임을 순차적으로 읽기
# while True:
#     ret, frame = cap.read()  # 다음 프레임 읽기
#
#     if not ret:  # 더 이상 읽을 프레임이 없으면
#         print('비디오 재생 완료')
#         break
#
#     # 프레임 처리 및 표시
#     cv2.imshow("Video", frame)
#
#     # 'q' 키를 누르면 종료
#     # waitKey(30): 약 33fps로 재생 (30ms 대기)
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
#
# # 자원 해제 (중요!)
# cap.release()
# cv2.destroyAllWindows()

'''
========================================
2. 웹캠(카메라) 사용
========================================
'''

# # 웹캠 열기
# # 0: 기본 카메라, 1,2,3...: 추가 카메라
# cap = cv2.VideoCapture(0)
#
# # 카메라 해상도 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
# if not cap.isOpened():
#     print('웹캠을 열 수 없습니다.')
#     exit()
#
# # 실시간 웹캠 영상 표시
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         break
#
#     cv2.imshow('WebCam', frame)
#
#     # 'q' 키로 종료
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

'''
========================================
3. 비디오 저장 (VideoWriter)
========================================
'''

# # 비디오 저장 설정
# width, height = 640, 480
# fps = 30  # 초당 30프레임
#
# # FourCC 코드 (코덱 지정)
# # 'mp4v': MPEG-4 코덱
# # 'XVID': Xvid 코덱
# # 'MJPG': Motion-JPEG 코덱
# # 'H264': H.264 코덱 (효율적, 널리 사용)
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4
#
# # VideoWriter 객체 생성
# # VideoWriter(파일명, 코덱, fps, (너비, 높이))
# out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))
#
# # 5초 분량의 그라데이션 비디오 생성
# for i in range(fps * 5):  # 30fps * 5초 = 150프레임
#     # 프레임 생성 (Blue 채널이 점점 밝아짐)
#     frame = np.zeros((height, width, 3), dtype=np.uint8)
#     frame[:, :, 0] = int(255 * i / (fps * 5))  # Blue 증가
#
#     # 프레임을 비디오에 쓰기
#     out.write(frame)
#
# # 자원 해제
# out.release()
# print('비디오 저장 완료: output.mp4')

'''
========================================
4. 웹캠 녹화 (실시간 녹화 제어)
========================================
'''

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 웹캠 설정 읽기
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 20  # 녹화 fps

# 비디오 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('recording.mp4', fourcc, fps, (width, height))

recording = False  # 녹화 상태 플래그

print('=== 웹캠 녹화 프로그램 ===')
print('r 키: 녹화 시작/중지')
print('q 키: 종료')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 녹화 중일 때 표시 추가
    if recording:
        # 빨간 원 (녹화 표시)
        cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
        # REC 텍스트
        cv2.putText(frame, 'REC', (50, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # 프레임을 비디오 파일에 저장
        out.write(frame)

    cv2.imshow('Recording', frame)

    # 키 입력 처리
    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):  # 'r' 키: 녹화 토글
        recording = not recording
        print(f"녹화: {'시작' if recording else '중지'}")
    elif key == ord('q'):  # 'q' 키: 종료
        break

# 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()

print('프로그램 종료')

'''
========================================
주요 VideoCapture 속성
========================================

cv2.CAP_PROP_FRAME_WIDTH    : 프레임 너비
cv2.CAP_PROP_FRAME_HEIGHT   : 프레임 높이
cv2.CAP_PROP_FPS            : 초당 프레임 수
cv2.CAP_PROP_FRAME_COUNT    : 총 프레임 수
cv2.CAP_PROP_POS_FRAMES     : 현재 프레임 위치 (0부터 시작)
cv2.CAP_PROP_POS_MSEC       : 현재 시간 위치 (밀리초)
cv2.CAP_PROP_FOURCC         : 코덱 식별자
cv2.CAP_PROP_BRIGHTNESS     : 밝기 (카메라)
cv2.CAP_PROP_CONTRAST       : 대비 (카메라)
cv2.CAP_PROP_SATURATION     : 채도 (카메라)

사용법:
- 읽기: value = cap.get(속성)
- 쓰기: cap.set(속성, value)
'''
