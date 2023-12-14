# Phase 1 - Milestone
# Nama  : Michael Nathaniel
# Batch : HCK-009

import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox(label='Menu:', options=['Beranda', 'Exploration Data Analysis', 'Model Inference'])

if page == 'Beranda':
    st.title('Welcome to, Pneumonia Analyzer')
    st.write('GC7 - FTDS - Phase 2')
    st.header('')

    col1, col2 = st.columns(2)

    # ======================= Columns 1 =======================
    col1.write('**Nama             :**')
    col1.write('**Batch            :**')
    col1.write('**Tujuan           :**')

    # ======================= Columns 2 =======================
    col2.write('Michael Nathaniel')
    col2.write('HCK-009')
    col2.write("Proyek ini bertujuan mengembangkan model komputer yang dapat melakukan klasifikasi apakah seseorang menderita Pneumonia atau tidak, berdasarkan hasil X-ray paru-paru pasien.")
    col2.write("Pendekatan yang diterapkan dalam pembuatan model ini adalah konsep Computer Vision, dengan implementasi arsitektur Artificial Neural Network untuk memahami hubungan kompleks antara gambar X-ray dan keberadaan Pneumonia. Prinsip dasar proyek ini melibatkan pelatihan model untuk mengenali pola dan fitur pada gambar X-ray yang menunjukkan adanya Pneumonia.")
    col2.write("Dengan demikian, proyek ini bersifat esensial dalam pengaplikasian teknologi kecerdasan buatan dalam bidang diagnostik medis.")

    st.header('')
    st.write('**Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!**')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Kita diberikan dataset mengenai data-data foto xray paru-paru normal dan paru-paru pengidap pneumonia. Untuk membantu dokter dalam menganalisa pasien, kita akan membuat model yang dapat mengklasifikasikan apakah pasien memiliki pneumonia atau tidak dengan hanya memberikan inputan foto xray paru-paru pasien.')
    
    with st.expander("Problem Statement"):
        st.caption('Buatlah model komputer yang dapat melakukan klasifikasi apakah seseorang menderita Pneumonia atau tidak, berdasarkan hasil X-ray paru-paru pasien.')

    with st.expander("Outline"):
        st.caption("1. Memuat data dan memeriksa informasi mengenai kumpulan data.")
        st.caption("2. EDA pada kumpulan data yang melibatkan analisis data lebih lanjut untuk mendapatkan wawasan.")
        st.caption("3. Feature Engineering untuk mendapatkan fitur dan target pemodelan.")
        st.caption("4. Mendefinisikan Model Deep Learning.")
        st.caption("5. Melatih model.")
        st.caption("6. Evaluasi model yang terdiri dari Hyperparameter Tuning untuk mendapatkan model terbaik dengan hasil terbaik.")
        st.caption("7. Menyimpan model terbaik.")
        st.caption("8. Kesimpulan.")
        st.caption("9. Deployment.")
        st.caption("")

    with st.expander("Kesimpulan"):
        st.caption("Dataset yang digunakan menunjukkan ketidakseimbangan antara data foto X-ray paru-paru normal dan pneumonia. Melalui tahap Analisis Eksplorasi Data (EDA), ditemukan variasi tingkat keparahan pneumonia pada foto X-ray paru-paru pasien yang beragam. Keadaan ini menyebabkan model mempelajari data dari paru-paru yang tidak terlalu parah pneumonia. Namun, hal ini juga berpotensi membuat model bingung, terutama karena beberapa foto X-ray paru-paru pneumonia sangat mirip dengan kondisi paru-paru normal. Ketidakseimbangan data diatasi dengan menggunakan pembobotan kelas (class weight).")
        st.caption("Model terbaik menggunakan arsitektur dengan 3 lapisan tersembunyi, jumlah neuron yang merupakan kelipatan 8, lapisan flatten, dan penerapan dropout. Model ini dilatih dengan 30 epoch dan mencapai kinerja yang sangat baik. Kami juga mengimplementasikan callback yaitu checkpoint untuk menyimpan model dalam kondisi terbaik, dan dari total 30 epoch, model terbaik disimpan pada epoch ke-30.")
        st.caption("Model berhasil melakukan prediksi dengan baik, dapat membedakan paru-paru pneumonia dengan tingkat false pneumonia yang rendah (mampu memprediksi data paru-paru pneumonia dengan akurasi sebesar 95%). Namun, kelemahan model terletak pada prediksi klasifikasi paru-paru normal, di mana hanya 54% dari seluruh data uji yang berhasil diidentifikasi sebagai paru-paru normal.")


elif page == 'Exploration Data Analysis':
    eda.run()
else:
    prediction.run()