import numpy as np
import matplotlib.pyplot as plt


# 한글 폰트 설정 추가
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False


def sigmod(z):
    return 1 / (1 + np.exp(-z))


# 시각화
z = np.linspace(-10, 10, 100)
y = sigmod(z)

plt.figure(figsize=(10, 6))
plt.plot(z, y, 'b-', linewidth=2)
plt.axhline(y=0.5, color='r', linestyle='--', label='경계 (0.5)')
plt.axvline(x=0, color='gray', linestyle='-', alpha=0.3)
plt.xlabel('z (wx + b)')
plt.ylabel('σ(z)')
plt.title('시그모이드 함수')
plt.legend()
plt.grid(True)
plt.show()
