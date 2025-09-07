import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8, 10, 12, 14])
y = np.array([0, 0, 0, 1, 1, 1, 1])

model = Sequential()

model.add(Dense(1, input_dim = 1, activation="sigmoid"))

model.compile(optimizer = "sgd", loss = "binary_crossentropy")

model.fit(x, y, epochs=1000)

plt.scatter(x, y)
plt.plot(x, model.predict(x), 'r')
plt.show()

hour = 7
input_data = tf.constant([[hour]], dtype = tf.float32)
prediction = model.predict(input_data)[0][0]

print(hour, prediction)