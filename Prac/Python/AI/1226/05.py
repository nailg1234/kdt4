# 이미지 표시와 그리기
import cv2
import numpy as np

# 캔버스 생성
canvas = np.zeros((1000, 1200, 3), dtype=np.uint8)

# 선 그리기
# cv2.line(
#   img = '도화지',
#   pt1 = '시작점',
#   pt2 = '끝점',
#   color = '색상',
#   thickness = '두께',
#   lineType = '선 종류'
#   )

# LINE_AA는 경계를 부드럽게 만들어주는 기능
cv2.line(canvas, (50, 50), (550, 450), (0, 0, 255), 2)
cv2.line(canvas, (50, 50), (550, 350), (0, 0, 255), 2, cv2.LINE_AA)

# cv2.rectangle(
#   img = '도화지',
#   pt1 = '시작점',
#   pt2 = '끝점',
#   color = '색상',
#   thickness = '두께' -1: 색상 채워진다!
#  )

# 사각형(테두리)
cv2.rectangle(canvas, (50, 50), (200, 150), (0, 0, 255), 2)

# 채워진 사각형
cv2.rectangle(canvas, (250, 50), (400, 150), (0, 255, 0), -1)


# 원과 타원 그리기
# cv2.circle(
#   img = '도화지',
#   center = '원의 중심',
#   radius = '반지름',
#   color = '색상',
#   thickness = '두께' -1: 색상 채워진다!
#  )
cv2.circle(canvas, (350, 250), 50, (255, 0, 0), -1)

# cv2.ellipse(
#   img = '도화지',
#   center = '원의 중심',
#   axes = '축',
#   angle = '각도',
#   startAngle = '각도',
#   endAngle = '각도',
#   color = '색상',
#   thickness = '두께' -1: 색상 채워진다!
#  )
cv2.ellipse(canvas, (550, 350), (80, 40), 0, 0, 360, (255, 0, 0), -1)

# 텍스트 추가
# cv2.putText(
#   img = '도화지',
#   text = '글자',
#   org = '위치',
#   fontFace = '글꼴',
#   fontScale = '글자 크기'
#   color = '색상',
#   thickness = '두께' -1: 색상 채워진다!
#  )

cv2.putText(
    canvas,
    'Hello OpenCV!',
    (700, 100),
    cv2.FONT_HERSHEY_DUPLEX,
    2,
    (255, 255, 255),
    2,
    cv2.LINE_AA
)

cv2.imshow('Lines', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
