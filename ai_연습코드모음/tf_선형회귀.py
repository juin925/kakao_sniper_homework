import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])

model = Sequential()

model.add(Dense(1, input_dim=1, activation="linear"))

model.compile(optimizer="sgd", loss="mse")

model.fit(x, y, epochs=2001)

plt.scatter(x, y)
plt.plot(x, model.predict(x), 'r')
plt.show()

hour = 7
input_data = tf.constant([[hour]])
prediction = model.predict(input_data)[0][0]
print(hour, prediction)