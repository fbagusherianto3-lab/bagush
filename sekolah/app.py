import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Penyajian Data KK",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Penyajian Data Kartu Keluarga")
st.write("Aplikasi sederhana menggunakan **Python + Streamlit**")

st.divider()

# =========================
# FORM INPUT DATA
# =========================
with st.form("form_kk"):
    st.subheader("👨‍👩‍👧 Data Anggota Keluarga")

    hubungan = st.selectbox(
        "Hubungan Keluarga",
        [
            "Kepala Keluarga",
            "Ibu RT",
            "Tante / Om",
            "Kakak",
            "Adik",
            "Kakek / Nenek"
        ]
    )

    nama = st.text_input("Nama Lengkap")
    alamat = st.text_area("Alamat")
    ttl = st.text_input("Tempat, Tanggal Lahir")
    umur = st.number_input("Umur (Tahun)", min_value=0, max_value=120)
    pekerjaan = st.text_input("Pekerjaan")

    st.subheader("🎓 Jenjang Pendidikan")
    sd = st.text_input("SD")
    smp = st.text_input("SMP")
    sma = st.text_input("SMA / SMK")
    s1 = st.text_input("S1")

    submit = st.form_submit_button("Simpan Data")

# =========================
# TAMPILKAN DATA
# =========================
if submit:
    data = {
        "Hubungan": hubungan,
        "Nama": nama,
        "Alamat": alamat,
        "TTL": ttl,
        "Umur": f"{umur} Tahun",
        "Pekerjaan": pekerjaan,
        "SD": sd,
        "SMP": smp,
        "SMA/SMK": sma,
        "S1": s1
    }

    st.success("✅ Data berhasil disimpan")

    st.subheader("📄 Hasil Penyajian Data")
    df = pd.DataFrame([data])
    st.dataframe(df, use_container_width=True)

    st.subheader("📌 Detail Data")
    for key, value in data.items():
        st.write(f"**{key}** : {value}")