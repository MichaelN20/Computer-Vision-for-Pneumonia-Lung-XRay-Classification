# Phase 1 - Milestone
# Nama  : Michael Nathaniel
# Batch : HCK-009

import requests
import numpy as np
import pandas as pd
from PIL import Image
from io import BytesIO
import streamlit as st
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img

def run():
    # Load the model
    st.title('Model Inference')
    st.write('Silahkan berikan imputasi data untuk dilakukan prediksi')
    st.header('')

    model = load_model("model_final.h5")

    st.write('Pilih cara input gambar:')
    input_option = st.radio("Pilih cara input gambar:", ("Unggah Gambar", "Link Gambar"))

    if input_option == "Unggah Gambar":
        uploaded_file = st.file_uploader("Unggah gambar x-ray paru-paru", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = load_img(uploaded_file, target_size=(150, 150))
            st.image(image, caption='Gambar yang diunggahan', use_column_width=True)
            image = image.resize((150, 150)) # Resize foto menjadi sesuai dengan target size
            img_array = img_to_array(image) # Convert foto menjadi numpy array
            img_array = np.expand_dims(img_array, axis=0) / 255.0 # Mengekspnasi dimensi and normalisasi pixel values
            
    elif input_option == "Link Gambar":
        image_url = st.text_input("Masukkan URL gambar x-ray paru-paru")
        
        if image_url:
            try:
                response = requests.get(image_url)
                image = Image.open(BytesIO(response.content))
                st.image(image, caption=f'URL: {image_url}', use_column_width=True)
                image = image.resize((150, 150)) # Resize foto menjadi sesuai dengan target size
                img_array = img_to_array(image) # Convert foto menjadi numpy array
                img_array = np.expand_dims(img_array, axis=0) / 255.0 # Mengekspnasi dimensi and normalisasi pixel values
            except Exception as e:
                st.write("Error:", str(e))

    st.write('Berikut hasil data yang anda input :')

    if st.button(label='Predict'):
        try:
            # Melakukan prediksi data gambar
            prediction = model.predict(img_array)
            if prediction[0][0] > 0.7: # mengkonversi hasil prediksi menjadi dapat dibaca manusia
                st.write("Paru-paru ini adalah paru-paru Pneumonia")
            else:
                st.write("Paru-paru ini adalah paru-paru normal")
        except Exception as e:
            st.write("Input belum diberikan.")