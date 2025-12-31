from pytesseract import pytesseract as pyt
import cv2

img = cv2.imread('Prac/Python/AI&OpenCV/1231/ocr1.png', cv2.IMREAD_GRAYSCALE)
pyt.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pyt.image_to_string(img, lang='eng')

print(text)
