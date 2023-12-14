# Phase 1 - Milestone
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Explaration Data Analysis (EDA)')
    st.write('Analisis data lebih lanjut untuk mendapatkan wawasan mendalam terhadap dataset yang digunakan.')
    st.header('')
    
    # Melihat Contoh X-ray Paru-paru normal dan Paru-paru Pneumonia
    st.header('Melihat Contoh X-ray Paru-paru normal dan Paru-paru Pneumonia')
    image = Image.open('Melihat Contoh X-ray Paru-paru normal dan Paru-paru Pneumonia 1.png')
    image2 = Image.open('Melihat Contoh X-ray Paru-paru normal dan Paru-paru Pneumonia 2.png')
    st.image(image)
    st.image(image2, caption='Figure 1: X-ray paru-paru Pneumonia dan normal')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Pneumonia adalah suatu kondisi penyakit yang ditandai oleh peradangan pada jaringan paru-paru, khususnya pada kantong udara kecil yang disebut alveoli. Peradangan ini dapat disebabkan oleh infeksi bakteri, virus, atau jamur.

            Visualisasi diatas adalah beberapa sampel foto X-ray paru-paru normal dan paru-paru pengidap pneumonia. X-ray paru-paru digunakan untuk memeriksa kondisi kesehatan paru-paru seseorang.

            Pada kasus pneumonia, perubahan pada gambar X-ray dapat teramati. Area yang terkena pneumonia cenderung menunjukkan gambaran yang lebih gelap dan kabur akibat adanya cairan atau perubahan jaringan.

            Sebaliknya, pada X-ray paru-paru yang normal, gambar yang terlihat akan lebih terang dan jelas tanpa adanya area yang gelap atau kabur. Oleh karena itu, kita dapat membedakan antara paru-paru normal dan yang mengidap pneumonia melalui pemeriksaan hasil X-ray tersebut.
            ''')

    # Menghitung jumlah sampel untuk setiap kelas pada data testing, training, dan validation
    st.header('Menghitung jumlah sampel untuk setiap kelas pada data testing, training, dan validation')
    image3 = Image.open('Menghitung jumlah sampel untuk setiap kelas pada data testing, training, dan validation 1.png')
    image4 = Image.open('Menghitung jumlah sampel untuk setiap kelas pada data testing, training, dan validation 2.png')
    image5 = Image.open('Menghitung jumlah sampel untuk setiap kelas pada data testing, training, dan validation 2.png')
    st.image(image3)
    st.image(image4)
    st.image(image5, caption='Figure 2: Distribusi data paru-paru normal dan Pneumonia pada data Train, Test, dan Val')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Dari hasil pengecekan, terlihat bahwa pada keseluruhan dataset yang kita gunakan baik pada data training, testing, dan validation, data foto rontgen pasian yang mengidap penumonia menjadi foto terbanyak dibandingkan foto yang normal. Untuk menghasilkan model dengan performansi yang baik, kita akan melakukan handling terhadap data yang tidak seimbang ini.
            ''')
        
    # Melihat distribusi ukuran gambar pada data training, testing, dan validation
    st.header('Melihat distribusi ukuran gambar pada data training, testing, dan validation')
    image6 = Image.open('Melihat distribusi ukuran gambar pada data training, testing, dan validation 1.png')
    image7 = Image.open('Melihat distribusi ukuran gambar pada data training, testing, dan validation 2.png')
    image8 = Image.open('Melihat distribusi ukuran gambar pada data training, testing, dan validation 3.png')
    st.image(image6)
    st.image(image7)
    st.image(image8, caption='Figure 2: Distribusi ukuran gambar paru-paru normal dan Pneumonia pada data Train, Test, dan Val')
    with st.expander("**Penjelasan**"):
        st.write(
            '''
            Dari hasil pengecekan dengan visualisasi, terlihat bahwa distribusi ukuran gambar pada dataset yang kita gunakan baik data training, testing, maupun validation adalah serupa.
            ''')