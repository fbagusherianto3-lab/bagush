import streamlit as st
from streamlit_option_menu import option_menu


# =========================================================
# Navigasi Sidebar
# =========================================================
with st.sidebar:
    selected = option_menu(
        'Hitung Luas Bangun',
        ['Hitung Luas Persegi Panjang', 
         'Hitung Luas Segitiga'],
        default_index=0
    )

# =========================================================
# Halaman: Hitung Luas Persegi Panjang
# =========================================================
if selected == 'Hitung Luas Persegi Panjang':
    st.title("Hitung Luas Persegi Panjang")

    panjang = st.number_input("Masukkan nilai panjang", min_value=0)
    lebar = st.number_input("Masukkan nilai lebar", min_value=0)
    hitung = st.button("Hitung Luas Persegi Panjang")

    if hitung:
        luas = panjang * lebar
        st.write(f"Luas persegi panjang adalah = {luas}")
        st.success(f"Luas persegi panjang adalah = {luas}")

# =========================================================
# Halaman: Hitung Luas Segitiga
# =========================================================
elif selected == 'Hitung Luas Segitiga':
    st.title("Hitung Luas Segitiga")

    alas = st.slider("Masukkan nilai alas", 0, 100, 0)
    tinggi = st.slider("Masukkan nilai tinggi", 0, 100, 0)
    hitung = st.button("Hitung Luas Segitiga")

    if hitung:
        luas = 0.5 * alas * tinggi
        st.write(f"Luas segitiga adalah = {luas}")
        st.success(f"Luas segitiga adalah = {luas}")
