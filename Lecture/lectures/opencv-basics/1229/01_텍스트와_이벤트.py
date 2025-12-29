"""
OpenCV 기초 - 01. 텍스트 그리기와 이벤트 처리

이 파일에서 배울 내용:
1. 이미지 중앙에 텍스트를 예쁘게 배치하는 방법
2. 마우스 클릭, 드래그 등의 마우스 이벤트 처리하기
3. 키보드 입력 받아서 처리하기
"""

import cv2
import numpy as np

# ============================================================
# 1. 중앙 정렬 텍스트 그리기
# ============================================================
def draw_centered_text(img, text, font, scale, color, thicknes=1):
    '''
    이미지 중앙에 텍스트를 그려주는 함수

    왜 필요할까?
    - cv2.putText()는 시작점을 지정해야 해서 중앙에 배치하려면 계산이 필요함
    - 이 함수를 사용하면 자동으로 중앙에 배치됨
    '''
    h, w = img.shape[:2]  # 이미지의 높이와 너비

    # 텍스트 크기 미리 계산하기
    # getTextSize()는 텍스트가 얼마나 큰 공간을 차지하는지 알려줌
    # text_width: 텍스트가 차지하는 가로 길이 (픽셀)
    # text_height: 텍스트가 차지하는 세로 높이 (글자 위 ~ 기준선)
    # baseline: 'g', 'y', 'p' 같은 글자의 아래로 내려가는 부분을 위한 추가 공간
    (text_width, text_height), baseline = cv2.getTextSize(text, font, scale, thicknes)

    # 중앙에 배치할 시작 좌표 계산
    x = (w - text_width) // 2   # 가로 중앙: (전체 너비 - 텍스트 너비) / 2
    y = (h + text_height) // 2  # 세로 중앙: (전체 높이 + 텍스트 높이) / 2

    # 계산한 위치에 텍스트 그리기
    cv2.putText(img, text, (x, y), font, scale, color, thicknes, cv2.LINE_AA)

# 사용 예제 (주석 해제하면 실행됨)
canvas = np.zeros((300, 400, 3), dtype=np.uint8)
# draw_centered_text(canvas, "Centered Text", cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
# cv2.imshow("Centered", canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ============================================================
# 2. 마우스 이벤트 처리하기
# ============================================================
def mouse_callback(event, x, y, flags, param):
    '''
    마우스 이벤트를 처리하는 콜백 함수

    언제 사용할까?
    - 이미지에 그림을 그리는 프로그램 만들 때
    - 이미지에서 특정 영역을 선택할 때
    - 마우스로 물체의 위치를 표시할 때

    매개변수 설명:
    :param event: 어떤 마우스 동작이 일어났는지 (클릭, 드래그 등)
    :param x: 마우스의 가로 위치 (픽셀)
    :param y: 마우스의 세로 위치 (픽셀)
    :param flags: Ctrl, Shift 같은 특수 키가 눌렸는지
    :param param: 추가로 전달할 데이터 (사용자 정의)
    '''

    """
    📌 자주 사용하는 마우스 이벤트:
    - cv2.EVENT_MOUSEMOVE: 마우스를 움직일 때
    - cv2.EVENT_LBUTTONDOWN: 왼쪽 버튼을 누를 때
    - cv2.EVENT_LBUTTONUP: 왼쪽 버튼을 뗄 때
    - cv2.EVENT_LBUTTONDBLCLK: 왼쪽 버튼을 더블클릭할 때
    - cv2.EVENT_RBUTTONDOWN: 오른쪽 버튼을 누를 때
    - cv2.EVENT_RBUTTONUP: 오른쪽 버튼을 뗄 때
    - cv2.EVENT_MBUTTONDOWN: 가운데 버튼 (휠 클릭)을 누를 때
    - cv2.EVENT_MOUSEWHEEL: 마우스 휠을 굴릴 때

    📌 플래그로 특수 키 확인하기:
    - cv2.EVENT_FLAG_LBUTTON: 왼쪽 버튼이 눌린 상태인지
    - cv2.EVENT_FLAG_RBUTTON: 오른쪽 버튼이 눌린 상태인지
    - cv2.EVENT_FLAG_CTRLKEY: Ctrl 키가 눌렸는지
    - cv2.EVENT_FLAG_SHIFTKEY: Shift 키가 눌렸는지
    - cv2.EVENT_FLAG_ALTKEY: Alt 키가 눌렸는지
    """

    # 어떤 이벤트가 발생했는지 확인하고 처리
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'왼쪽 클릭: ({x}, {y})')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f'오른쪽 클릭: ({x}, {y})')
    elif event == cv2.EVENT_MOUSEMOVE:
        # 마우스를 움직일 때마다 출력하면 너무 많이 나와서 주석 처리
        # print(f'마우스 이동: ({x}, {y})')
        pass
    elif event == cv2.EVENT_LBUTTONUP:
        print(f'왼쪽 버튼 해제: ({x}, {y})')

# 마우스 이벤트 사용 예제 (주석 해제하면 실행됨)
# canvas = np.zeros((400, 600, 3), dtype=np.uint8)
# cv2.namedWindow("Mouse Event")
# cv2.setMouseCallback("Mouse Event", mouse_callback)  # 마우스 콜백 함수 등록
#
# while True:
#     cv2.imshow('Mouse Event', canvas)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 종료
#         break
#
# cv2.destroyAllWindows()

# ============================================================
# 3. 키보드 이벤트 처리하기
# ============================================================
"""
키보드 입력을 받는 방법

OpenCV에서는 cv2.waitKey()로 키보드 입력을 받을 수 있어요.
이 함수는 지정한 시간(ms) 동안 키 입력을 기다립니다.

사용 예시:
- cv2.waitKey(0): 키를 누를 때까지 무한 대기
- cv2.waitKey(1): 1ms만 대기 (동영상 재생 등에 사용)
- cv2.waitKey(100): 100ms 대기
"""

canvas = np.zeros((400, 600, 3), dtype=np.uint8)

print('키 입력 테스트 시작! (q 또는 ESC로 종료)')

while True:
    cv2.imshow('Keyboard', canvas)

    key = cv2.waitKey(100)  # 100ms 동안 키 입력 대기

    # 키가 입력되지 않았으면 -1이 반환됨
    if key == -1:
        continue

    # 키 코드 추출 (운영체제마다 다른 값이 나올 수 있어서 하위 8비트만 사용)
    key = key & 0xFF

    """
    📌 자주 사용하는 특수 키 코드:
    - 27: ESC (Escape 키)
    - 13: Enter
    - 32: Space (스페이스바)
    - 8: Backspace
    - 9: Tab

    ⚠️ 화살표 키는 운영체제마다 달라요:
    - Linux: 81(↑), 82(↓), 83(→), 84(←)
    - Windows: cv2.waitKeyEx() 사용 필요
    """

    # 입력된 키에 따라 다른 동작 수행
    if key == ord('q'):  # ord('q')는 'q' 문자의 ASCII 코드
        print('q 키로 종료')
        break
    elif key == 27:  # ESC 키
        print('ESC 키로 종료')
        break
    elif key == 13:  # Enter 키
        print('Enter 키를 눌렀습니다')
    elif key == 32:  # Space 키
        print('Space 키를 눌렀습니다')
    elif key == 8:  # Backspace 키
        print('Backspace 키를 눌렀습니다')
    else:
        # 일반 문자인 경우 출력 (ASCII 코드 32~126만 출력 가능)
        print(f'키 코드: {key}, 문자: {chr(key) if 32 <= key < 127 else "?"}')

cv2.destroyAllWindows()