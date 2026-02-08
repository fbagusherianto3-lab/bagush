import streamlit as st
from streamlit_option_menu import option_menu

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(page_title="Hitung Luas Bangun", page_icon="📐", layout="centered")

# =========================================================
# STYLE CSS LANGSUNG DI STREAMLIT
# =========================================================
st.markdown("""
    <style>
    /* Background utama */
    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
        color: #333333;
        font-family: "Poppins", sans-serif;
    }

    /* Header */
    h1, h2, h3 {
        color: #00695c;
        text-align: center;
        font-weight: 700;
    }

    /* Tombol */
    div.stButton > button:first-child {
        background-color: #00796b;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        height: 3em;
        width: 100%;
        border: none;
        transition: 0.3s;
        font-weight: bold;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    }
    div.stButton > button:hover {
        background-color: #004d40;
        color: #e0f2f1;
        transform: scale(1.05);
        box-shadow: 0px 6px 12px rgba(0,0,0,0.3);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #004d40;
        color: white;
        padding-top: 20px;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
        font-family: "Poppins", sans-serif;
    }

    /* Input number dan slider */
    .stNumberInput input {
        background-color: #ffffff;
        border-radius: 10px;
        border: 1px solid #00796b;
        padding: 5px;
        font-size: 15px;
    }
    .stSlider > div > div > div {
        background-color: #00796b !important;
    }
    .stSlider > div > div > div > div {
        background-color: #80cbc4 !important;
    }

    /* Kotak hasil sukses */
    .stSuccess {
        background-color: #b2dfdb !important;
        color: #004d40 !important;
        border-radius: 10px;
        padding: 12px;
        font-weight: 600;
        text-align: center;
        border: 1px solid #004d40;
    }

    /* Animasi ringan pada header */
    h1:hover, h2:hover {
        color: #004d40;
        transition: 0.3s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# NAVIGASI SIDEBAR
# =========================================================
with st.sidebar:
    selected = option_menu(
        '📏 Hitung Luas Bangun',
        ['Hitung Luas Persegi Panjang',
         'Hitung Luas Segitiga'],
        default_index=0
    )

# =========================================================
# HALAMAN: PERSEGI PANJANG
# =========================================================
if selected == 'Hitung Luas Persegi Panjang':
    st.title("📏 Hitung Luas Persegi Panjang")

    panjang = st.number_input("Masukkan nilai panjang", min_value=0)
    lebar = st.number_input("Masukkan nilai lebar", min_value=0)
    hitung = st.button("Hitung Luas Persegi Panjang")

    if hitung:
        luas = panjang * lebar
        st.write(f"Luas segitiga adalah = {luas}")
        st.success(f"Luas persegi panjang adalah = {luas}")

# =========================================================
# HALAMAN: SEGITIGA
# =========================================================
elif selected == 'Hitung Luas Segitiga':
    st.title("🔺 Hitung Luas Segitiga")

    alas = st.slider("Masukkan nilai alas", 0, 100, 0)
    tinggi = st.slider("Masukkan nilai tinggi", 0, 100, 0)
    hitung = st.button("Hitung Luas Segitiga")

    if hitung:
        luas = 0.5 * alas * tinggi
        st.write(f"Luas segitiga adalah = {luas}")
        st.success(f"Luas segitiga adalah = {luas}")
