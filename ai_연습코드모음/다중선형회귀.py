import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([2, 4, 6, 8])
x2 = np.array([0, 4, 2, 3])
y = np.array([81, 93, 91, 97])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x1, x2, y)
plt.show()

a = 0
b = 0
c = 0

lr = 0.01

epochs = 2001

n = len(x1)

for i in range(epochs):
  y_pred = (a * x1) + (b * x2) + c
  error = y - y_pred

  a_diff = (2/n)*sum(-x1*(error))
  b_diff = (2/n)*sum(-x2*(error))
  c_diff = (2/n)*sum(-(error))

  a = a - (lr*a_diff)
  b = b - (lr*b_diff)
  c = c - (lr*c_diff)

  if i % 100 == 0:
    print(f"{i}번째 학습 - x1 기울기 : {a} x2 기울기 : {b} 절편 : {c}")

y_pred = a*x1 + b*x2 + c