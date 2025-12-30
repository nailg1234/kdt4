import cv2
##### 1. 이미지를 불러서 창으로 띄우는 작업

### 1-1 imread(이미지경로): 이미지 반환(numpy)
img = cv2.imread("OpenCV/1212/images/puppy.jpg")
img2 = cv2.imread("OpenCV/1212/images/puppy.jpg", cv2.IMREAD_GRAYSCALE)
# print("img:", img) # numpy 배열 출력


### 1-2 imshow(윈도우이름, 읽어온이미지): 이미지를 새창으로 열어주는 함수
cv2.imshow("puppy image", img)
cv2.imshow("puppy image grayscale", img2)

### 1-3 waitKey(밀리초): ASCII CODE 반환
# 윈도우가 시간초만큼 대기후에 종료된다.
# waitKey가 없다면 윈도우가 대기하지 않고 바로 꺼진다.
key = cv2.waitKey(0) # 0은 무한대기
print("key", key)

changeToChar = chr(key)
changToASCII = ord(changeToChar)
print(f"문자: {changeToChar}, ASCII CODE: {changToASCII}")



cv2.destroyAllWindows()

##### 2. 이미지 저장, shape 속성 확인
gray_cat = cv2.imread("OpenCV/1212/images/cat.jpg", cv2.IMREAD_GRAYSCALE)
color_cat = cv2.imread("OpenCV/1212/images/cat2.jpg", cv2.IMREAD_COLOR)

### 2-1 shape 속성: 세로, 가로, 채널값을 튜플형태로 반환
# 채널은 grayscale 사진일 경우는 값이 없다.
print('gray cat image shape', gray_cat.shape)
print('color cat image shape', color_cat.shape)

cv2.imshow("cute cat gray", gray_cat)
cv2.imshow("cute cat color", color_cat)

h1, w1 = gray_cat.shape
print("gray height", h1)
print("gray width", w1)

h2, w2, c2 = color_cat.shape
print("color height", h2)
print("color width", w2)
print("color channel", c2)

h3, w3 = color_cat.shape[:2]
print("color height3", h3)
print("color width3", w3)

cv2.waitKey(0)
cv2.destroyAllWindows()

## imwrite("저장할 경로명", 저장할이미지)
cv2.imwrite("OpenCV/1212/output/gray_cat.png", gray_cat)