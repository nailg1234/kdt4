# 실습4. 그라데이션 이미지(도전)
# 수평과 수직 그라데이션이 동시에 적용된 이미지를 만들어 보세요
# - 크기: 300x300
# - 왼쪽-> 오른쪽: 0->255(수평)
# - 위->아래: 0->255(수직)
# - 두 그라데이션을 합성

# 힌트: np.linspace(), np.tile(), 브로드캐스팅 활용

import cv2
import numpy as np

h, w = 300, 300

gradient_h = np.tile(np.linspace(0, 255, w), (h, 1)).astype(np.uint8)
gradient_w = np.tile(np.linspace(0, 255, h), (w, 1)).T.astype(np.uint8)

grad = cv2.add(gradient_h, gradient_w)

cv2.imshow('prac_04', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()
