import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


dataset = pd.read_csv("dataset.csv").sample(frac=1).reset_index(drop=True)

dataset['location'] = dataset['location'].map({'TUXTLA GUTIERREZ':0,'SAN CRISTOBAL DE LAS CASAS':1,'COMITAN':2})
dataset['propertyType'] = dataset['propertyType'].map({'Casa':0,'Departamento':1})

x_train = dataset.drop(['prices'],axis=1).to_numpy()[:len(dataset)-500]
yd_train = dataset['prices'].to_numpy()[:len(dataset['prices'])-500]

x_test = dataset.drop(['prices'],axis=1).to_numpy()[len(dataset)-500:len(dataset)]
yd_test = dataset['prices'].to_numpy()[len(dataset['prices'])-500:len(dataset['prices'])]

def cargar_modelado():
    model = models.Sequential([
        layers.Dense(100, activation='relu',input_dim=5),
        layers.Dense(100, activation='relu'),
        layers.Dense(100, activation='relu'),
        layers.Dense(1, activation='linear'),
    ])

    model.compile(optimizer=tf.keras.optimizers.Adadelta(learning_rate=0.4), loss='huber', metrics=['accuracy'])

    history = model.fit(x_train,yd_train, epochs=50, validation_data=(x_test,yd_test))
    return model, history

modelo, historial = cargar_modelado()
result = modelo.predict([[0,0,100,3,2]])
print(result)

plt.plot(historial.history['val_loss'], label='val_loss')
plt.plot(historial.history['loss'], label='loss')
plt.xlabel('Número de iteraciones')
plt.ylabel('Error')
plt.legend()
plt.show()