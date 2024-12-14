from __future__ import unicode_literals
import yt_dlp as youtube_dl  # Ganti youtube_dl dengan yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading

def download_audio():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return

    folder = filedialog.askdirectory()
    if not folder:
        return

    # Konfigurasi yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{folder}/%(title)s.%(ext)s",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'progress_hooks': [on_progress],
    }

    def download_task():
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            update_status("Download completed!")
            messagebox.showinfo("Success", "Audio has been downloaded successfully!")
        except Exception as e:
            update_status("Error")
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            download_button.config(state=tk.NORMAL)

    threading.Thread(target=download_task).start()
    update_status("Downloading...")
    download_button.config(state=tk.DISABLED)

def on_progress(d):
    if d['status'] == 'downloading':
        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes', 1)
        percentage = (downloaded_bytes / total_bytes) * 100
        progress_bar['value'] = percentage
        status_label.config(text=f"Downloading... {percentage:.2f}%")
    elif d['status'] == 'finished':
        progress_bar['value'] = 100
        status_label.config(text="Download finished!")

def update_status(message):
    status_label.config(text=message)

# GUI Setup
root = tk.Tk()
root.title("YouTube MP3 Downloader")
root.geometry("450x300")

# Label untuk URL Input
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=5)

# Input URL
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Tombol Download
download_button = tk.Button(root, text="Download MP3", command=download_audio)
download_button.pack(pady=10)

# Progress Bar
progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
progress_bar.pack(pady=10)

# Label Status
status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=5)

# Footer
footer_label = tk.Label(root, text="Contact me on Discord: https://discord.gg/BgjwgWx", fg="gray", font=("Arial", 8))
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the GUI
root.mainloop()
