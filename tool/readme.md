
---

## 📥 YouTube MP3 Downloader

Proyek ini adalah aplikasi sederhana untuk mengunduh audio dari video YouTube dalam format **MP3**. Aplikasi ini menggunakan **yt_dlp** (pengganti youtube-dl) dan **FFmpeg** dari [BtbN FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases) untuk proses konversi.

---

### 🚀 Fitur Utama
- **Mengunduh audio** dari video YouTube.
- **Konversi otomatis** file audio dari `.webm` ke `.mp3` menggunakan FFmpeg.
- **Tampilan grafis sederhana** berbasis tkinter.

---

### 🛠️ Persyaratan
Pastikan Anda sudah menginstal:
1. **Python** (versi 3.8 atau lebih baru).
2. **yt_dlp** (library Python untuk mengunduh video/audio YouTube).
3. **FFmpeg** (dari BtbN FFmpeg Builds).

---

### 📝 Instalasi

1. **Install Dependensi**:
   Instal `yt_dlp` dengan perintah berikut:
   ```bash
   pip install yt-dlp
   ```

2. **Download FFmpeg**:
   - **Kunjungi** [BtbN FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases).
   - Unduh **versi terbaru** (misalnya `ffmpeg-master-latest-win64-gpl.zip`).
   - **Ekstrak file ZIP** ke lokasi yang mudah diakses, seperti `C:\ffmpeg`.

3. **Tambahkan FFmpeg ke PATH**:
   - Buka **Environment Variables**:
     - Klik **Start** > cari **"Environment Variables"** > klik **Edit the system environment variables**.
   - Tambahkan path folder `bin` dari FFmpeg ke **System Path**:
     ```
     C:\ffmpeg\bin
     ```
   - Restart **CMD** atau komputer untuk menerapkan perubahan.

4. **Verifikasi Instalasi**:
   Buka terminal/command prompt dan ketik:
   ```bash
   ffmpeg -version
   ```
   Jika berhasil, informasi versi FFmpeg akan muncul.

---

### 💻 Menjalankan Program
1. Jalankan aplikasi menggunakan Python:
   ```bash
   python tool/dl.py
   ```
2. Masukkan **URL YouTube** pada kolom input.
3. Klik tombol **Download MP3**.
4. Audio akan diunduh dan dikonversi ke format **MP3** secara otomatis.

---

### 🤝 Kontribusi
Kontribusi sangat diterima! Lakukan fork, buat cabang baru, dan ajukan **Pull Request**.

---

### 📜 Lisensi
Proyek ini dilisensikan di bawah **MIT License**.

---

### ✨ Kontak
Jika ada pertanyaan atau saran, silakan hubungi:  
- **Email**: bendev403@gmail.com

---