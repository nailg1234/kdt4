"""
OpenCV 기초 - 05. 이미지/비디오 저장과 웹캠 활용

이 파일에서 배울 내용:
1. 이미지를 다양한 형식(JPEG, PNG)과 품질로 저장하기
2. 이미지 읽기 실패를 안전하게 처리하는 방법
3. 웹캠으로 사진 촬영하고 저장하기
4. 비디오 속도를 조절하는 방법 (배속, 슬로우모션)
"""

import cv2
import numpy as np
import os

# ============================================================
# 1. 이미지 저장 형식 및 품질 비교
# ============================================================
"""
이미지 저장 포맷의 차이:
- JPEG (.jpg): 손실 압축, 파일 크기 작음, 사진에 적합
- PNG (.png): 무손실 압축, 파일 크기 큼, 투명도 지원, 그래픽에 적합

JPEG 품질 설정:
- 0 ~ 100 (낮을수록 압축률 높고 화질 낮음, 높을수록 파일 크기 크고 화질 좋음)
"""

# 480x640 크기의 랜덤 컬러 이미지 생성
img = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)

# 다양한 형식과 품질로 이미지 저장하기
print("이미지를 다양한 형식으로 저장 중...")

# JPEG 품질 50 (낮은 화질, 작은 파일)
cv2.imwrite('test_jpg_q50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])

# JPEG 품질 95 (높은 화질, 큰 파일)
cv2.imwrite('test_jpg_q95.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])

# PNG 형식 (무손실)
cv2.imwrite('test.png', img)

# 저장된 파일들의 크기 비교
print("\n저장된 파일 크기 비교:")
print("-" * 40)
files = ['test_jpg_q50.jpg', 'test_jpg_q95.jpg', 'test.png']
for fname in files:
    size = os.path.getsize(fname)
    print(f'{fname}: {size/1024:.2f} KB')
print("-" * 40)
print("💡 JPEG 품질이 높을수록, PNG는 무손실이라 파일 크기가 큰 것을 확인할 수 있어요!\n")

# ============================================================
# 2. 이미지 읽기 실패를 안전하게 처리하기
# ============================================================
"""
왜 필요할까?
- 파일이 없거나 경로가 잘못되면 cv2.imread()는 None을 반환
- None을 처리하지 않으면 프로그램이 에러로 종료될 수 있어요
- 안전한 처리를 통해 프로그램의 안정성을 높일 수 있어요

실생활 활용:
- 사용자가 잘못된 파일을 선택했을 때
- 네트워크 문제로 이미지 다운로드 실패했을 때
- 파일이 삭제되었을 때
"""

def safe_imread(filepath):
    '''
    안전하게 이미지를 읽는 함수

    파일이 존재하지 않거나 읽을 수 없으면:
    - 에러 메시지 출력
    - 기본 검은 이미지 반환 (프로그램은 계속 실행)

    파일을 성공적으로 읽으면:
    - 이미지 크기 정보 출력
    - 읽은 이미지 반환
    '''
    img = cv2.imread(filepath)

    if img is None:
        print(f'❌ 이미지를 찾을 수 없습니다: {filepath}')
        print(f'   대신 검은색 기본 이미지를 반환합니다.')
        # 300x300 크기의 검은색 이미지를 기본값으로 반환
        img = np.zeros((300, 300, 3), dtype=np.uint8)
    else:
        print(f'✅ 이미지 읽기 성공! 크기: {img.shape}')

    return img

# 테스트: 존재하지 않는 파일 읽기 시도
print("\n존재하지 않는 파일 읽기 테스트:")
img1 = safe_imread('nonexistent.jpg')  # 이 파일은 없어서 검은 이미지가 반환됨
print()
# ============================================================
# 3. 웹캠으로 사진 촬영하고 저장하기
# ============================================================
"""
웹캠 활용 예시:
- 셀카 촬영 앱
- 화상 회의 프로그램
- 보안 카메라 시스템
- QR 코드/바코드 스캐너

주요 기능:
- 실시간 웹캠 영상 표시
- 's' 키로 현재 화면 저장
- 미러 모드 (좌우 반전)로 더 자연스러운 화면
"""

# 웹캠 열기 (0은 기본 카메라, 여러 개면 1, 2, ... 사용)
cap = cv2.VideoCapture(0)

# 웹캠이 제대로 열렸는지 확인
if not cap.isOpened():
    print('❌ 웹캠을 열 수 없습니다.')
    print('   웹캠이 연결되어 있는지 확인하세요.')
    exit()

photo_count = 1  # 저장할 사진 번호

print("\n" + "="*50)
print("📷 웹캠 촬영 모드")
print("="*50)
print('💡 사용법:')
print('   - "s" 키: 현재 화면을 사진으로 저장')
print('   - "q" 키: 프로그램 종료')
print("="*50 + "\n")

while True:
    # 웹캠에서 프레임(화면) 읽기
    ret, frame = cap.read()

    # 프레임 읽기 실패 시 종료
    if not ret:
        print('❌ 프레임을 읽을 수 없습니다.')
        break

    # 미러 모드 (좌우 반전) - 셀카처럼 자연스럽게
    # 1: 좌우 반전, 0: 상하 반전, -1: 상하좌우 반전
    frame = cv2.flip(frame, 1)

    # 화면에 안내 텍스트 표시
    cv2.putText(frame, "Press 's' to save, 'q' to quit",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # 웹캠 화면 표시
    cv2.imshow('WebCam', frame)

    # 1ms 동안 키 입력 대기
    key = cv2.waitKey(1) & 0xFF

    # 's' 키를 누르면 사진 저장
    if key == ord('s'):
        filename = f'Photo_{photo_count:03d}.jpg'  # 예: Photo_001.jpg
        cv2.imwrite(filename, frame)
        print(f'📸 사진 저장됨: {filename}')
        photo_count += 1  # 다음 사진 번호 증가
    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        print('👋 웹캠 촬영을 종료합니다.')
        break

# 웹캠 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
print()

# ============================================================
# 4. 비디오 속도 조절하기 (배속, 슬로우모션)
# ============================================================
"""
비디오 속도 조절 원리:
- 2배속: 프레임을 건너뛰면서 저장 (2개 중 1개만 사용)
- 0.5배속(슬로우모션): 같은 프레임을 여러 번 저장

실생활 활용:
- 유튜브 배속 재생 기능
- 슬로우모션 영상 제작
- 타임랩스 영상 만들기
- 동영상 용량 줄이기
"""

# 비디오 설정
width, height = 640, 480  # 비디오 해상도
fps = 30                   # 초당 프레임 수 (30fps)
duration = 5               # 비디오 길이 (5초)
total_frames = fps * duration  # 총 프레임 수: 30 * 5 = 150

# fourcc: 비디오 코덱 설정 (mp4v = MPEG-4 코덱)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

print("\n" + "="*50)
print("🎬 비디오 생성 중...")
print("="*50)

# 1단계: 원본 비디오 생성 및 프레임 저장
out_original = cv2.VideoWriter('original.mp4', fourcc, fps, (width, height))

frames = []  # 모든 프레임을 저장할 리스트
for i in range(total_frames):
    # 검은 배경에 Blue 채널이 점점 밝아지는 프레임 생성
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:, :, 0] = int(255 * i / total_frames)  # Blue 채널 증가 (0 → 255)

    # 프레임 번호 표시
    cv2.putText(frame, f'Frame: {i}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # 원본 비디오에 프레임 쓰기
    out_original.write(frame)
    # 나중에 사용하기 위해 프레임 저장
    frames.append(frame)

out_original.release()
print("✅ original.mp4 생성 완료! (5초, 30fps, 150 프레임)")

# 2단계: 2배속 비디오 생성
# 프레임을 2개씩 건너뛰면서 저장 → 재생 시간이 절반으로 줄어듦
out_2x = cv2.VideoWriter('speed_2x.mp4', fourcc, fps, (width, height))
for i in range(0, len(frames), 2):  # 0, 2, 4, 6, ... (2칸씩 건너뛰기)
    out_2x.write(frames[i])

out_2x.release()
print("✅ speed_2x.mp4 생성 완료! (2.5초, 2배속, 75 프레임)")

# 3단계: 0.5배속(슬로우모션) 비디오 생성
# 각 프레임을 2번씩 저장 → 재생 시간이 2배로 늘어남
out_half = cv2.VideoWriter('speed_0.5x.mp4', fourcc, fps, (width, height))
for frame in frames:
    out_half.write(frame)  # 1번
    out_half.write(frame)  # 2번 (같은 프레임을 두 번 저장)

out_half.release()
print("✅ speed_0.5x.mp4 생성 완료! (10초, 0.5배속, 300 프레임)")

print("="*50)
print("🎉 모든 비디오 생성 완료!")
print("="*50)
print("\n생성된 파일:")
print("  - original.mp4: 원본 (5초)")
print("  - speed_2x.mp4: 2배속 (2.5초)")
print("  - speed_0.5x.mp4: 0.5배속/슬로우모션 (10초)")
print("\n💡 각 비디오를 재생해서 속도 차이를 확인해보세요!")
