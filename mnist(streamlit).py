# -*- coding: utf-8 -*-
"""MNIST(Streamlit).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/137xLUOGIh8Cb1E1GZBbE-xi75K-2fTrq
"""

!pip install streamlit

import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random as rn
import tensorflow as tf
from keras.utils import to_categorical
from tqdm.keras import TqdmCallback
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D,BatchNormalization
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix

st.title("Mnist Image Classification App")
st.write("")

file_up = st.file_uploader("Upload an image", type="jpg")

if file_up is not None:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Just a second...")
    labels = predict(file_up)

    # print out the top 5 prediction labels with scores
    for i in labels:
        st.write("Prediction (index, name)", i[0], ",   Score: ", i[1])

def predict(image_path):
  img = image.load_img(file, target_size=(28,28), color_mode="grayscale")
  img = img_to_array(img)
  img = np.expand_dims(img, axis=0)
  ans = load_model('mnist.h5').predict_classes(img)
  return ans

!pip install -r requirements.txt

