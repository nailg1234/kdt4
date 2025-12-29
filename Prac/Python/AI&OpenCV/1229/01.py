import cv2
import numpy as np

# 중앙 정렬 텍스트


def draw_centered_text(img, text, font, scale, color, thicknes=1):
    '''
        이미지 중앙에 텍스트 그리기
    '''
    h, w = img.shape[:2]

    # 텍스트 크기 계산
    # text_width: 텍스트가 차지하는 가로 픽셀
    # text_height: 텍스트가 차지하는 세로(글자 위 ~ 베이스 라인) 픽셀

    # baseline: 글자의 아래쪽(g, y, p 같은 내려오는 꼬리)을 위해 필요한 추가 여백 픽셀
    (text_width, text_height), baseline = cv2.getTextSize(
        text, font, scale, thicknes)

    # 중앙 좌표
    x = (w - text_width) // 2
    y = (h + text_height) // 2

    cv2.putText(img, text, (x, y), font, scale, color, thicknes, cv2.LINE_AA)


# 사용
# canvas = np.zeros((300, 400, 3), dtype=np.uint8)
# draw_centered_text(canvas, "Centerd Text",
#                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
# cv2.imshow("Centered", canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 마우스 이벤트
# def mouse_callback(event, x, y, flags, param):
#     '''
#     mouse_callback의 Docstring

#     :param event: 이벤트 종류
#     :param x: 마우스 좌표
#     :param y: 마우스 좌표
#     :param flags: 특수 키 상태
#     :param param: 사용자 데이터
#     '''

#     """
#     마우스 이벤트:
#     - cv2.EVENT_MOUSEMOVE: 마우스 이동
#     - cv2.EVENT_LBUTTONDOWN: 왼쪽 버튼 누름
#     - cv2.EVENT_LBUTTONUP: 왼쪽 버튼 해제
#     - cv2.EVENT_LBUTTONDBLCLK: 왼쪽 더블클릭
#     - cv2.EVENT_RBUTTONDOWN: 오른쪽 버튼 누름
#     - cv2.EVENT_RBUTTONUP: 오른쪽 버튼 해제
#     - cv2.EVENT_MBUTTONDOWN: 가운데 버튼 누름
#     - cv2.EVENT_MOUSEWHEEL: 마우스 휠

#     플래그:
#     - cv2.EVENT_FLAG_LBUTTON: 왼쪽 버튼 누른 상태
#     - cv2.EVENT_FLAG_RBUTTON: 오른쪽 버튼 누른 상태
#     - cv2.EVENT_FLAG_CTRLKEY: Ctrl 키 누른 상태
#     - cv2.EVENT_FLAG_SHIFTKEY: Shift 키 누른 상태
#     - cv2.EVENT_FLAG_ALTKEY: Alt 키 누른 상태
#     """

#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(f'왼쪽 클릭: ({x}, {y})')
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         print(f'오른쪽 클릭: ({x}, {y})')
#     elif event == cv2.EVENT_MOUSEMOVE:
#         print(f'마우스 이동: ({x}, {y})')
#     elif event == cv2.EVENT_LBUTTONUP:
#         print(f'왼쪽 버튼 해제: ({x}, {y})')


# canvas = np.zeros((400, 600, 3), dtype=np.uint8)
# cv2.namedWindow("Mouse Event")
# cv2.setMouseCallback("Mouse Event", mouse_callback)
# while True:
#     cv2.imshow('Mouse Event', canvas)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()


# 키보드 이벤트
canvas = np.zeros((400, 600, 3), dtype=np.uint8)

print(f'키 입력 테스트 (q: 종료)')

while True:
    cv2.imshow('Keyboard', canvas)

    key = cv2.waitKey(100)  # 100ms 대기

    if key == -1:
        continue

    # 키 코드 추출 (플랫폼 독립적)
    key = key & 0xFF

    if key == ord('q'):
        print('종료')
        break
    elif key == 27:  # ESC
        print('ESC 종료')
        break
    elif key == 13:  # Enter
        print('Enter 키')
    elif key == 32:  # Space
        print('Space 키')
    elif key == 8:  # BackSpace
        print('BackSpace 키')
    else:
        print(f"키 코드: {key}, 문자: {chr(key) if 32 <= key < 127 else '?' }")

cv2.destroyAllWindows()
