import tensorflow as tf
from tensorflow.keras import layers, models
import numpy  as np



def create_model(input_dim):
    model = models.Sequential()
    model.add(layers.Dense(128, activation = 'relu', input_dim = input_dim))
    model.add(layers.Dense(64, activation = 'relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer = 'adam', loss = 'mse')
