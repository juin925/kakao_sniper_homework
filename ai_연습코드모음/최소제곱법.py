import tensorflow as tf
import numpy as np

x = np.array([2, 4, 6, 8]) # x 값 모음
y = np.array([81, 93, 91, 97]) # y 값 모음
 
def top(x, mx, y, my): # 분자 (x-x평균)(y-y평균)의 합 구하기
  d = 0
  for i in range(len(x)):
    d += (x[i]-mx)*(y[i]-my)
  return d

x_mean = x.mean() # x 값들의 평균
y_mean = y.mean() # y 값들의 평균

divisor = sum([(i-x_mean)**2 for i in x]) # 분모 (x-x평균)^2의 합 구하기

dividend = top(x, x_mean, y, y_mean) / divisor # 기울기

a = y_mean - (x_mean * dividend)  # y 절편

print(a)

print(f'1차방정식 : y = {dividend}x + {a}')