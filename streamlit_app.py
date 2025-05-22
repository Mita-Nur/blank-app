import streamlit as st

st.title("Selamat datang di Website Informatika")
st.image("7673827846d1550beafb0fd0be08d930.jpg", width=200)
st.write("\n")
st.subheader("Mita Nur Ballza")
st.write( 
    "mari latihan membuat gambar karakter dari anime" 
)

st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
