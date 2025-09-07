# x = [2, 4, 6, 8] y = [81, 93, 91, 97] 일 때 y = 3x + 76 의 import tensorflow as tf
import numpy as np

# x = [2, 4, 6, 8] y = [81, 93, 91, 97] 일 때 y = 3x + 76 의 평균 제곱 오차
x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

fake_a = 3
fake_b = 76

def predict(x):
  return fake_a * x + fake_b

predict_result = []

for i in range(len(x)):
  predict_result.append(predict(x[i]))

print(predict_result)

n = len(x)

def mse(y, y_pred):
  return (1/n) * sum((y - y_pred)**2)

print(mse(y, predict_result))