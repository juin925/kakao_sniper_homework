import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd

df = pd.read_csv('./data/pima-indians-diabetes3.csv')

x = df.iloc[:, 0:8]
y = df.iloc[:, 8]

model = Sequential()

model.add(Dense(12, input_dim=8, activation='relu', name='Dense1'))
model.add(Dense(8, activation='relu', name='Dense2'))
model.add(Dense(1, activation='sigmoid', name='Dense3'))
model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x, y, epochs=100, batch_size=5)