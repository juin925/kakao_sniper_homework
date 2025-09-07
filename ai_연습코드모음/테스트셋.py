import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('./data/sonar3.csv', header = None)

X = df.iloc[:, 0:60]
y = df.iloc[:, 60]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, shuffle = True)

model = Sequential()
model.add(Dense(24, input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

model.compile(loss="binary_crossentropy", optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=200, batch_size=10)

score = model.evaluate(X_test, y_test)
print(score[1])