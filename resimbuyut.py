import tkinter as tk
from tkinter import HORIZONTAL, filedialog, Text, DISABLED, NORMAL, ttk, font, RIGHT, Y, messagebox
from PIL import ImageTk, Image
import random

dosyaadi = tk.filedialog.askopenfilename(initialdir = "/", title = "Yeniden boyutlandırılacak resmi seçin", filetypes = (("PNG","*.png"),("JPEG","*.jpg"),("Tüm Dosyalar","*.*")))

genişlik = int(input("Genişlik : "))
yukseklik = int(input("Yükseklik : "))

resim = Image.open(dosyaadi)
yeniresim = resim.resize((genişlik, yukseklik), Image.Resampling.LANCZOS)
yol = tk.filedialog.askdirectory(initialdir="/", title="Kaydetme yolu seçin")
yeniresim.save(yol + f"/yeniresim [{random.randint(0,10000)}].png")