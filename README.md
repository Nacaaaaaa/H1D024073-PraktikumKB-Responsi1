# Responsi Kecerdasan Buatan - Implementasi Logika Fuzzy & Sistem Pakar

Proyek ini adalah *web-based application* yang mengimplementasikan dua cabang utama Kecerdasan Buatan: Logika Fuzzy untuk menilai kelayakan spesifikasi *smartphone* dalam *gaming*, dan Sistem Pakar untuk mendiagnosis akar masalah *lag* atau *stuttering* pada perangkat *mobile*.

---

## Identitas
- **Nama:** Nalendra Wicaksana
- **NIM:**   H1D024073
- **Shift Lama:** E
- **Shift Baru:** F


---

## Garis Besar Sistem
Aplikasi ini dibuat menggunakan arsitektur **MVC (Model-View-Controller)** sederhana:
- **Backend:** Dibuat `Flask` (Python) untuk memproses komputasi Fuzzy dan mesin inferensi Sistem Pakar.
- **Frontend (Antarmuka):** Menggunakan `HTML5` dan `Bootstrap 5` sebagai UI.

Sistem ini terbagi menjadi dua fungsi utama:

### 1. Gaming Phone Grader (Logika Fuzzy)
Sistem ini bertugas memberikan skor kelayakan (0-100) pada sebuah *smartphone* untuk menjalankan *game* berat berdasarkan spesifikasi teknisnya.
- **Metode:** Logika Fuzzy dengan defuzzifikasi *Centroid* (Titik Berat).
- **Variabel Input:** Intensitas Clock Processor, Kapasitas VRAM Total, dan Thermal Cooling Score.
- **Cara Kerja:** Mengubah nilai spesifikasi menjadi derajat keanggotaan (Fuzzifikasi), mengevaluasi kombinasi *Rule Base*, dan menghasilkan **Gaming Score Performance** secara dinamis.

### 2. Mobile Lag Tracker (Sistem Pakar)
Sistem ini bertugas untuk mencari akar permasalahan *lag, frame drop*, atau *force close*.
- **Metode:** *Forward Chaining* dengan arsitektur **Multiple-Fault Diagnosis**.
- **Basis Pengetahuan:** 8 gejala spesifik mencakup anomali visual, fluktuasi suhu, latensi jaringan, dan keterbatasan memori.
- **Cara Kerja:** Mampu mendeteksi **Komplikasi Masalah** (mengeliminasi bias *Single-Fault Assumption*) dan memberikan *actionable solution* untuk setiap diagnosis yang terpicu secara bersamaan.

---

## Quick Start (Instalasi & Deployment)

Pastikan Anda telah menginstal **Python 3.8+** dan **Git**. Anda bisa menyalin dan menjalankan seluruh blok kode di bawah ini di Terminal / Command Prompt Anda sekaligus.

```bash
# 1. Kloning dan masuk ke folder repositori
git clone <url-repositori-github-anda>
cd responsi_kb

# 2. Buat dan aktifkan Virtual Environment
python -m venv env
.\env\Scripts\activate

# 3. Instal semua dependencies yang dibutuhkan
pip install Flask numpy scikit-fuzzy networkx packaging

# 4. Jalankan AI Server
python app.py
