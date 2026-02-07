import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Pythones Portfolio",
    page_icon="🐍",
    layout="wide"
)

# =========================================================
# FUNGSI UTILITAS
# =========================================================
def load_lottieurl(url: str):
    """Memuat animasi Lottie dari URL."""
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        st.warning(f"⚠️ Gagal memuat animasi Lottie: {e}")
        return None


def local_css(file_name: str):
    """Memuat file CSS lokal untuk styling tambahan."""
    try:
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ File CSS tidak ditemukan: {file_name}")


def safe_open_image(path):
    """Aman membuka gambar dari path, tampilkan error jika tidak ditemukan."""
    try:
        return Image.open(path)
    except FileNotFoundError:
        st.error(f"❌ Gambar tidak ditemukan: {path}")
        return None


# =========================================================
# MEMUAT CSS DAN ANIMASI
# =========================================================
local_css("style/style.css")

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_developer = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_yr6zz3wv.json")  # ✅ ditambahkan

# =========================================================
# MEMUAT GAMBAR
# =========================================================
img_ram = safe_open_image("images/b-123.jpg")
img_storage = safe_open_image("images/b-123.jpg")

# Gambar profil — cek berurutan, pakai cadangan kalau tidak ada
profile_image = safe_open_image("images/profile.jpg")
if profile_image is None:
    profile_image = safe_open_image("images/bagus.png")

# =========================================================
# BAGIAN 1: HEADER / INTRO
# =========================================================
with st.container():
    st.title("🐍 Pythones Portfolio")
    st.subheader("Selamat datang di portfolio interaktif saya!")
    st.write("Berikut ini contoh animasi interaktif yang dimuat dari LottieFiles:")

    col1, col2 = st.columns(2)

    with col1:
        st.header("💻 Coding Time")
        if lottie_coding:
            st_lottie(lottie_coding, speed=1, loop=True, height=300, key="coding")
        else:
            st.error("Gagal memuat animasi coding 😢")

    with col2:
        st.header("👨‍💻 Developer Spirit")
        if lottie_developer:
            st_lottie(lottie_developer, speed=1, loop=True, height=300, key="developer")
        else:
            st.error("Gagal memuat animasi developer 😢")

# =========================================================
# BAGIAN 2: PROFIL SINGKAT
# =========================================================
st.divider()
st.header("📸 Tentang Saya")

if profile_image:
    st.image(profile_image, caption="Python Developer", width=200)
else:
    st.info("Tambahkan file `profile.jpg` atau `bagus.png` di folder images untuk menampilkan foto profil.")

# =========================================================
# BAGIAN 3: PROFESI DAN PENGALAMAN
# =========================================================
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Hi, Saya **F Bagus Herianto** 👋")
        st.title("Data Operation - PT BRI Insurance")
        st.write(
            """
            Saya bekerja sebagai Software Engineer, Data Scientist, dan Data Operation Enthusiast.
            Berpengalaman dalam:
            - Optimalisasi integrasi data menggunakan **SSIS**  
            - Sistem monitoring database & data info (**SSRS**, **Grafana**, **Python**)  
            - Pengembangan **chatbot Telegram**  
            - Pengelolaan server (**Windows Server**, **MS SQL**, **Tableau Server**, **Python**)  
            - Prediksi kebutuhan server berdasarkan workload
            """
        )
        st.markdown("[🌐 LinkedIn](https://www.linkedin.com/in/bagus-herianto-a977783ab/)")
        st.markdown("[🎥 YouTube: FBagusherianto](https://www.youtube.com/@FBagusherianto)")
        st.markdown("[🎥 YouTube: HarianANTB.o](https://www.youtube.com/@HarianANTB)")
        st.markdown("[💰 Dukung di Saweria](https://saweria.co/Antbofficial)")

    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding_2")
        else:
            st.info("Animasi belum dimuat.")

# =========================================================
# BAGIAN 4: DAFTAR PROJEK
# =========================================================
st.write("---")
st.header("🧠 Daftar Projek")
st.write("Berikut beberapa proyek yang telah saya kerjakan:")

# --- Projek 1 ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if img_ram:
            st.image(img_ram, caption="Monitoring RAM Server")
    with text_column:
        st.subheader("Automation - Monitoring RAM")
        st.write("Sistem otomatis untuk memantau kondisi RAM server secara realtime.")
        st.markdown("[Tonton Video >](https://youtu.be/GXlckaGr0Eo?si=2Ttnn2TUTDOmsvR-)")

# --- Projek 2 ---
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if img_storage:
            st.image(img_storage, caption="HEBOH KERJA DI COFFEE SHOP")
    with text_column:
        st.subheader("HEBOH KERJA DI COFFEE SHOP")
        st.write("Sistem otomatis untuk memantau kondisi storage server secara realtime.")
        st.markdown("[Tonton Video >](https://youtu.be/4PnroGADX-I?si=snxjZlap3w_GUUd0)")

# =========================================================
# BAGIAN 5: KONTAK
# =========================================================
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("📞 Hubungi Saya")
        st.write(
            """
            Jika kamu tertarik dengan apa yang saya kerjakan, silakan hubungi saya:

            📧 **Email:** fbagusherianto@gmail.com  
            📱 **Whatsapp:** 0858-2013-1590  
            ▶️ **YouTube:** FBagusherianto
            """
        )
    with right_column:
        st.empty()  # Placeholder untuk form kontak di masa depan
