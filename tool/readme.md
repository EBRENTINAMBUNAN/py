
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

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/youtube-mp3-downloader.git
   cd youtube-mp3-downloader
   ```

2. **Install Dependensi**:
   Instal `yt_dlp` dengan perintah berikut:
   ```bash
   pip install yt-dlp
   ```

3. **Download FFmpeg**:
   - **Kunjungi** [BtbN FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases).
   - Unduh **versi terbaru** (misalnya `ffmpeg-master-latest-win64-gpl.zip`).
   - **Ekstrak file ZIP** ke lokasi yang mudah diakses, seperti `C:\ffmpeg`.

4. **Tambahkan FFmpeg ke PATH**:
   - Buka **Environment Variables**:
     - Klik **Start** > cari **"Environment Variables"** > klik **Edit the system environment variables**.
   - Tambahkan path folder `bin` dari FFmpeg ke **System Path**:
     ```
     C:\ffmpeg\bin
     ```
   - Restart **CMD** atau komputer untuk menerapkan perubahan.

5. **Verifikasi Instalasi**:
   Buka terminal/command prompt dan ketik:
   ```bash
   ffmpeg -version
   ```
   Jika berhasil, informasi versi FFmpeg akan muncul.

---

### 💻 Menjalankan Program
1. Jalankan aplikasi menggunakan Python:
   ```bash
   python dl.py
   ```
2. Masukkan **URL YouTube** pada kolom input.
3. Klik tombol **Download MP3**.
4. Audio akan diunduh dan dikonversi ke format **MP3** secara otomatis.

---

### 📂 Struktur Proyek
```
youtube-mp3-downloader/
│
├── dl.py                # Skrip utama aplikasi
├── README.md            # Dokumentasi proyek
└── requirements.txt     # Daftar dependensi (opsional)
```

---

### ⚠️ Troubleshooting
1. **Error: `ffmpeg not found`**  
   - Solusi: Pastikan path `C:\ffmpeg\bin` sudah ditambahkan ke Environment Variables.

2. **Error: `yt_dlp not found`**  
   - Solusi: Install ulang `yt_dlp` dengan:
     ```bash
     pip install --upgrade yt-dlp
     ```

3. **FFmpeg versi lama atau tidak berfungsi**  
   - Solusi: Unduh versi terbaru dari [BtbN FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases).

---

### 🤝 Kontribusi
Kontribusi sangat diterima! Lakukan fork, buat cabang baru, dan ajukan **Pull Request**.

---

### 📜 Lisensi
Proyek ini dilisensikan di bawah **MIT License**.

---

### ✨ Kontak
Jika ada pertanyaan atau saran, silakan hubungi:  
- **Discord**: [https://discord.gg/BgiwgWX](https://discord.gg/BgiwgWX)

---

Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan proyek ini dengan lancar menggunakan FFmpeg dari **BtbN Builds**. 😊