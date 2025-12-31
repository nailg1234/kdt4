import cv2
from pytesseract import pytesseract as pyt

img = cv2.imread('1231/ocr_basic_text.png', cv2.IMREAD_GRAYSCALE)

pyt.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 이진화
ret, binary = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

text = pyt.image_to_string(img, lang='eng')
print(text)

# 1. 이미지 불러오기
img = cv2.imread("1231/ocr_stop_sign.png")

h, w = img.shape[:2]

# ROI 직접 지정 ()
# STOP 글자 영역 (예시)
# roi = gray[0:484, 0:484]
roi = img[int(h*0.55):int(h*0.95), int(w*0.10):int(w*0.90)]

gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

# 이진화
# THRESH_BINARY_INV - 흰 글씨를 검은색으로 반전 (OCR이 검은 글씨를 더 잘 인식)
_, roi_bin = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# OCR 실행
# config='--psm 7' - 단일 텍스트 라인 인식 모드
text = pyt.image_to_string(
    roi_bin,
    lang="eng",
    config='--psm 7'
)
print(text)

