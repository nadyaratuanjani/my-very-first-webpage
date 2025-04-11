import streamlit as st 

def tampilkan_biodata(nama, umur, alamat, hobi):
    print("===== biodata =====")
    print(f"Nama   : Nadya")
    print(f"Umur   : 19 tahun")
    print(f"Alamat : somewhere in sukarame")
    print(f"Hobi   : mamam")
    print("===================")

with st.container():
    nama = st.text_input("Masukkan nama: ")
    umur = st.text_input("Masukkan umur: ")
    alamat = st.text_input("Masukkan alamat: ")
    hobi = st.text_input("Masukkan hobi: ")


# Panggil fungsi untuk menampilkan biodata
tampilkan_biodata(nama, umur, alamat, hobi)





