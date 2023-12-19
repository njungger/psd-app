# -*- coding: utf-8 -*-
"""psd_streamlit-app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kNjzen_cK3sJjOQTWa0tiBYJx10WaCWC
"""

! pip install streamlit

import streamlit as st
from PIL import Image
import numpy as np
import joblib

model = joblib.load('/content/drive/MyDrive/saved model/saved_model.pkl')

def klasifikasi(image):

    classes = ['_LeafBlast', '_BrownSpot', '_Hispa', '_Healthy']

    test_image_path = image
    test_image = Image.open(test_image_path)
    test_image = test_image.resize((128, 128))
    test_image = np.array(test_image) / 255.0
    test_image = np.expand_dims(test_image, axis=0)

    predictions = model.predict(test_image)
    class_index = np.argmax(predictions[0])
    class_name = classes[class_index]

    print(f'Predicted Class: {class_name}')

st.title("klasifikasi penyakit daun dengan metode cnn")

image = st.file_uploader("masukkan gambar daun")

if image:
    st.header("foto yang diupload")
    st.image(image)

submit = st.button("submit")

if submit:
    hasil = klasifikasi(image)
    st.succes(hasil)