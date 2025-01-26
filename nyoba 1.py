import streamlit as st

st.title("Nadya Ratu Anjani's profile")


def tampilkan_biodata(nama, umur, alamat, hobi):
    print("===== BIODATA =====")
    print(f"Nama   : {nama}")
    print(f"Umur   : {umur} tahun")
    print(f"Alamat : {alamat}")
    print(f"Hobi   : {hobi}")
    print("===================")


nama = input("Masukkan nama: ")
umur = input("Masukkan umur: ")
alamat = input("Masukkan alamat: ")
hobi = input("Masukkan hobi: ")

# Tampilkan biodata
tampilkan_biodata(nama, umur, alamat, hobi)