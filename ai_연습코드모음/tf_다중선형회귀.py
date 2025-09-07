import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

x = np.array([[2, 0], [4, 4], [6, 2], [8, 3]])
y = np.array([81, 93, 91, 97])

model = Sequential()

model.add(Dense(1, input_dim=2, activation="linear"))

model.compile(optimizer="sgd", loss="mse")

model.fit(x, y, epochs=500)

hour = 6
private_class = 3
input_data = tf.constant([[hour, private_class]])
prediction = model.predict(input_data)[0][0]
print(hour, private_class, prediction)