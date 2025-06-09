from genericpath import isdir
import win32.lib.win32con as win32con, win32gui, win32process
#pip install pywin32pip 
import pencerebul

import os
import json

#Yükleme Ekranını Yürüt
print("Yükleme Ekranı Yürütülüyor")

import threading
import actsupdater

if not os.path.isfile(r"./data.json"):
    jsonfile= open("data.json","w")
    jsonfile.write("{}")
    jsonfile.close()
    print("Yeni Json Yaratıldı.")

with open('data.json', 'r') as f:
    try:
        yzd = json.load(f)
    except:
        jsonfile= open("data.json","w")
        jsonfile.write("{}")
        jsonfile.close()
        yzd = json.load(f)
yzd[str(f"yuzde")] = 0
with open('data.json', 'w') as f:
    json.dump(yzd, f, indent=4)

with open('data.json', 'r') as f:
    clc = json.load(f)
    if not "tema_yolu" in clc:
        clc[str("tema_yolu")] = "./temalar/M O O D Y.actema"
with open('data.json', 'w') as f:
        json.dump(clc, f, indent=4)

try:
    os.startfile("acts.exe")
except:
    print("Development Modu Açık.")

server = "ws://acem8887-ghajinibot.glitch.me"

print("importlar yapılıyor")
# Importlar

import tkinter as tk
from tkinter import END, HORIZONTAL, CENTER, TOP, filedialog, Text, DISABLED, NORMAL, ttk, font, RIGHT, Y, messagebox
from PIL import ImageTk, Image
import yt_dlp as youtube_dl
import ytmusicapi
import random
import sty
import resim_aletleri
import time
import subprocess
import webbrowser
import pygame
import requests
import shutil
from pynput import keyboard
import pyglet
from pypresence import Presence
import datetime
from win10toast import ToastNotifier
import platform
import asyncio
import websockets
import websockets.legacy.client
import websockets.legacy.server
import base64
import pprint
import eyed3
from eyed3.id3.frames import ImageFrame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from io import BytesIO
from cryptography.fernet import Fernet

actsupdater.acts_guncelle(7.142857142857143)

scoop_chck = subprocess.run("scoop", capture_output=True, shell=True)

ffmpeg_chck = subprocess.run("ffmpeg", capture_output=True, shell=True)

actsupdater.acts_guncelle(7.142857142857143)


if "'ffmpeg' is not recognized as an internal or external command" in str(ffmpeg_chck):
    print("FFMPEG KURULU DEĞİL!")
    with open('data.json', 'r') as f:
        clc = json.load(f)
    clc[str(f"krlm_chk")] = 1
    with open('data.json', 'w') as f:
        json.dump(clc, f, indent=4)
    subprocess.call("scoop uninstall ffmpeg", shell=True)
    subprocess.call("scoop cache rm ffmpeg", shell=True)
else:
    with open('data.json', 'r') as f:
        clc = json.load(f)
    clc[str(f"krlm_chk")] = 2
    with open('data.json', 'w') as f:
        json.dump(clc, f, indent=4)

actsupdater.acts_guncelle(7.142857142857143)

if "'scoop' is not recognized as an internal or external command" in str(scoop_chck):
    print("SCOOP KURULU DEĞİL!")
    with open('data.json', 'r') as f:
        clc = json.load(f)
    clc[str(f"krlm_chk")] = 0
    with open('data.json', 'w') as f:
        json.dump(clc, f, indent=4)
    subprocess.call("scoop uninstall ffmpeg", shell=True)
    subprocess.call("scoop cache rm ffmpeg", shell=True)
    subprocess.call(f"rmdir /Q /S {os.path.expanduser('~')}\scoop\\", shell=True)
elif "'ffmpeg' is not recognized as an internal or external command" in str(ffmpeg_chck) and not "'scoop' is not recognized as an internal or external command" in str(scoop_chck):
    with open('data.json', 'r') as f:
        clc = json.load(f)
    clc[str(f"krlm_chk")] = 1
    with open('data.json', 'w') as f:
        json.dump(clc, f, indent=4)
    subprocess.call("scoop uninstall ffmpeg", shell=True)
    subprocess.call("scoop cache rm ffmpeg", shell=True)

actsupdater.acts_guncelle(7.142857142857143)
print("Fontlar Yükleniyor")
pyglet.font.add_file('font.ttf')

pyglet.font.add_file('font1.ttf')
#fontload = pyglet.font.load('Montserrat ExtraBold')
#fontload2 = pyglet.font.load('Montserrat Medium')

pygame.init()
actsupdater.acts_guncelle(7.142857142857143)
print("bildirimler başlatılıyor")

#Bilirimleri Başlat
try:
    tost = ToastNotifier()
except:
    print("win10 değil")
actsupdater.acts_guncelle(7.142857142857143)
print("zaman alınıyor")

#Programın Yürütüldüğü Zamanı Al
zmn = int(datetime.datetime.now().timestamp())
print(zmn)
prfx = str(zmn) + "."

#Variableler
version = "3.1.2"
tarih = "5/6/2023"
deneme = []
offline_modu = False
muzikres = {
    "muzikres": 0
}

jsonlink = "https://actupdates.glitch.me/guncbilgi.json"
dclink = "https://discord.gg/SCY67QJ5HY"
client_id = 0

#Renkler
def get_tema():
    print("Tema Alınıyor.")
    with open('data.json', 'r') as f:
        yol = json.load(f)
    if "tema_yolu" in yol:
        return yol["tema_yolu"]
    else:
        return 0

arkaplan = "#000000"
koyugri = "#1c1c1c"
acikgri = "#313542"
acikgri2 = "#23272a"
acikmavi = "#2082b2"
acikyesil = "#008000"
koyugri2 = "#1d1f21"
acarka = "#191414"
yazirengi = "#ffffff"
baslikyazirengi = "#ffffff"
altyazi = "B L Λ C K O U T"
kirmizi = "#FF0000"
turuncu = "#FFA500"
kenargenisligi = 0
cubukrengi = acikmavi
cubukrengi2 = acikyesil
kirmiziyazi = kirmizi
aramarengi = koyugri
thumbnailrengi = "#1f1f1f"
thumbnailikonrengi = "#d4d4d4"
thumbnaildolgu = koyugri
seffaflik = 1
stil = tk.RAISED

if get_tema() == 0:
    print("Geçerli Tema Yok.")
elif get_tema() != 0:
    print("Tema Yükleniyor.")
    try:
        with open(get_tema(), 'r') as f:
            renk = json.load(f)
        if "arkaplan" in renk:
            arkaplan = renk["arkaplan"]
            print("arkaplan: " + arkaplan)
        if "tusrengi" in renk:
            koyugri = renk["tusrengi"]
        if "thumbnailrengi" in renk:
            thumbnailrengi = renk["thumbnailrengi"]
            print("thumbnailrengi: " + thumbnailrengi)
        if "thumbnailikonrengi" in renk:
            thumbnailikonrengi = renk["thumbnailikonrengi"]
            print("thumbnailikonrengi: " + thumbnailikonrengi)
        if "thumbnaildolgu" in renk:
            thumbnaildolgu = renk["thumbnaildolgu"]
            print("thumbnaildolgu: " + thumbnaildolgu)
        if "basmarengi" in renk:
            acikgri = renk["basmarengi"]
            print("basmarengi: " + acikgri)
        if "acikgri" in renk:
            acikgri2 = renk["acikgri"]
            print("acikgri: " + acikgri2)
        if "acikmavi" in renk:
            acikmavi = renk["acikmavi"]
            print("acikmavi: " + acikmavi)
        if "acikyesil" in renk:
            acikyesil = renk["acikyesil"]
            print("acikyesil: " + acikyesil)
        if "cubukrengi" in renk:
            cubukrengi = renk["cubukrengi"]
            print("cubukrengi: " + cubukrengi)
        if "cubukrengi2" in renk:
            cubukrengi2 = renk["cubukrengi2"]
            print("cubukrengi2: " + cubukrengi2)
        if "acikarka" in renk:
            acarka = renk["acikarka"]
            print("acikarka: " + acarka)
        if "yazirengi" in renk:
            yazirengi = renk["yazirengi"]
            print("yazirengi: " + yazirengi)
        if "temaadi" in renk:
            altyazi = renk["temaadi"]
            print("temaadi: " + altyazi)
        if "baslikyazirengi" in renk:
            baslikyazirengi = renk["baslikyazirengi"]
            print("baslikyazirengi: " + baslikyazirengi)
        if "kirmizi" in renk:
            kirmizi = renk["kirmizi"]
            print("kirmizi: " + kirmizi)
        if "kirmiziyazi" in renk:
            kirmiziyazi = renk["kirmiziyazi"]
            print("kirmiziyazi: " + kirmiziyazi)
        if "aramarengi" in renk:
            aramarengi = renk["aramarengi"]
            print("aramarengi: " + aramarengi)
        if "turuncu" in renk:
            turuncu = renk["turuncu"]
            print("turuncu: " + turuncu)
        if "kenargenisligi" in renk:
            kenargenisligi = renk["kenargenisligi"]
            print("kenargenisligi: " + str(kenargenisligi))
        if "seffaflik" in renk:
            seffaflik = renk["seffaflik"]
            print("seffaflik: " + str(seffaflik))
        if "stil" in renk:
            stilraw = renk["stil"]
            if stilraw == 0:
                stil = tk.RAISED
            elif stilraw == 1:
                stil = tk.FLAT
            elif stilraw == 2:
                stil = tk.SUNKEN
            elif stilraw == 3:
                stil = tk.GROOVE
            elif stilraw == 4:
                stil = tk.RIDGE
            else:
                print("stil hatalı")
                stil = tk.RAISED
            print("stil " + str(stilraw))
    except Exception as e:
        print("Tema Hatalı: " + str(e))

actsupdater.acts_guncelle(7.142857142857143)
#191414
#331c28
#23272a

#Lisans Sözleşmesi
soz = f"""
AcemTube {version} Lisans Sözleşmesi.

- Hesaplar kişiye özeldir, paylaşılmamalıdır.

- Bir hesap sadece belirtilen sayıda bilgisayarda çalışır. Örn: 4PC 2PC

- Kötü amaçlı kullanım, şüpheli eylem durumunda hesabınız feshedilebilir.

- Epostanız, isim soyisminiz dışında başka hiçbir veri toplamayız.

- AcemTube sadece Discord üzerinden satın alınabilir, 
  başka yerden satılamaz, pazarlanamaz 

- Herhangi bir dolandırıcılığı veya 3. parti satıcıları lütfen tarafımıza bildirin.

- Programın 64 bit mimari üzerinde, minimum 6 GB ram barındıran bir
  makine üzerinde yürütülmesi tavsiye edilir.

- Eğer 14 günlük ücretsiz deneme hesabı açar ve programda herhangi bir bilinmeyen hata 
  bulursanız sınırsız 1PC lisans hediye edilecektir.

- 14 günlük deneme sürümü alanlar, programı satın aldıklarında 
  iade haklarından vazgeçmiş olurlar.

- Bu sözleşmede herhangi bir kurala uyulmaması durumunda 
  uyarmaksızın hesabınız feshedilecektir.

- Feshedilen hesaplar birdaha açılmayacaktır, program yeniden satın alınmalıdır.

- Lisans sözleşmesi bizim tarafımızdan her an bildirim vermeksizin değiştirilebilir.

- Kullanıcının programı kullanabilmesi için lisans sözleşmesini kabul etmesi zorunludur.

"""
#Json Bilgilerini Al
print("jsonlar alınıyor")
while True:
    try:
        verapi = requests.get(jsonlink)
        ver_get = json.loads(verapi.content)
        verakt = ver_get[version]
        updlink = ver_get["updatelink"]
        guncelsurumadi = ".".join(updlink.split("/")[-1].strip("AcemTube").strip("setup.exe"))
        print("Güncel Sürüm: " + guncelsurumadi)
        temalink = ver_get["temamarket"]
        dclink = ver_get["dclink"]
        chunkboyut = ver_get["chunk"]
        client_id = ver_get["clid"]
        deneme.clear()
        break
    except Exception as e:
        print("Jsonlar Alınamadı. : " + str(e))
        print(e)
        print(f"Deneme: {len(deneme)}, {deneme}")
        if len(deneme) > 2:
            rut = tk.Tk()
            rut.attributes("-alpha", 0)
            rut.title(f"AcemTube")
            rut.iconbitmap("acemtubered.ico")
            deneme.append(str(e))
            rut.geometry(f"{rut.winfo_screenwidth()}x{rut.winfo_screenheight()}+0+0")
            rut.bell()
            messagebox.showerror("Hata!", f"AcemTube Sunucularına Şu An Erişemiyoruz. Lütfen İnternet Bağlantınızı Kontrol Edin Veya Programı Güncelleyin. \n\nHata Kodu: {e} \n\nDiscord Sunucumuzdan Yardım Alabilirsiniz: {dclink}")
            try:
                with open('data.json', 'r') as f:
                    blgg = json.load(f)
                if "ofd" in blgg:
                    hwid = blgg["kullanici_adi"] + str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                    print(hwid)
                    if len(hwid) == 32:
                        antstr = hwid
                    elif len(hwid) < 32:
                        antstr = hwid + ("a"*(32 - len(hwid)))
                        print("int: " + str(antstr))
                    else:
                        antstr = hwid[:32]
                        print("ints: " + str(antstr))

                    anahtar = base64.urlsafe_b64encode(antstr.encode("ascii"))
                    acilcak = blgg["ofd"]
                    anlanahtar = Fernet(anahtar)
                    desif = anlanahtar.decrypt(acilcak.encode("ascii"))
                    #desif = "2022-06-15 15:41:42.213669"
                    print(desif)

                    print(str(desif).replace("b'", "").strip("'"))
                    fark = datetime.datetime.utcnow() - datetime.datetime.fromisoformat(str(desif).replace("b'", "").strip("'"))
                    if fark < datetime.timedelta(7):
                        offline_modu = messagebox.askyesno("AcemTube Offline Mod Kullanılabilir.", f"AcemTube'u Offline Modta Çalıştırmak İster Misiniz?")
                        print(offline_modu)
                        if offline_modu:
                            verakt = "1"
                            rut.destroy()
                    else:
                        messagebox.showerror(f"AcemTube Offline Modu Kullanılamaz.", f"AcemTube'u Offline Modta Çalıştırmak İçin Hesabınıza En Az 7 Gün İçinde Giriş Yapmış Olmanız Gerekiyor. ({str(fark).split('days')[0].strip()} Gün Oldu.)")
                        actsupdater.acts_guncelle(bitir=True)
                        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
            except Exception as e:
                print("Zaman Hesaplama Hatası: " + str(e))
                pass
            break
        else:
            deneme.append(str(e))


actsupdater.acts_guncelle(7.142857142857143)

print("discord rpc başlatılıyor")

#Discord RPC Başlat

if client_id != "0":
    try:
        RPC = Presence(client_id=client_id)
        RPC.connect()
        print("bob")
    except:
        print("discord yürütülmemişşşşş.")
else:
    print("Discord RPC Devre Dışı Bırakılmış.")

actsupdater.acts_guncelle(7.142857142857143)

def get_secim(s="sfx"):
    with open('data.json', 'r') as f:
        yol = json.load(f)
    if s in yol:
        return yol[s]
    else:
        return 1
print("sesler yükleniyor")
#Sesleri Yükle


if get_secim() != 0:
    if get_secim("tfx") == 1:
        click = pygame.mixer.Sound("click2.mp3")
    else:
        click = pygame.mixer.Sound("click1.mp3")

    if get_secim("ufx") == 1:
        tik = pygame.mixer.Sound('tik.mp3')
        hata = pygame.mixer.Sound('hata.mp3')
        hata1 = pygame.mixer.Sound('hata1.mp3')
        dikkat = pygame.mixer.Sound('dikkat.mp3')
    else:
        tik = pygame.mixer.Sound("click1.mp3")
        hata = pygame.mixer.Sound('click1.mp3')
        hata1 = pygame.mixer.Sound('click1.mp3')
        dikkat = pygame.mixer.Sound('click1.mp3')
    if get_secim("afx") == 1:
        rast = random.randint(0,100)
        if rast == 1:
            pygame.mixer.music.load("rr.mp3")
        elif rast == 100:
            pygame.mixer.music.load("AcemTubeog.mp3")
        elif rast == 50:
            pygame.mixer.music.load("bb.mp3")
        elif rast == 25:
            pygame.mixer.music.load("esp.mp3")
        elif rast == 75:
            pygame.mixer.music.load("wow.mp3")
        elif rast == 10:
            yumusakg = ["miss.mp3", "hit.mp3"]
            pygame.mixer.music.load(random.choice(yumusakg))
        elif rast == 0:
            pygame.mixer.music.load("arb.mp3")
        else:
            pygame.mixer.music.load("AcemTube.mp3")
            print(rast)
    else:
        pygame.mixer.music.load("click1.mp3")
else:
    click = pygame.mixer.Sound("click1.mp3")
    tik = pygame.mixer.Sound('click1.mp3')
    dikkat = pygame.mixer.Sound('click1.mp3')
    hata = pygame.mixer.Sound('click1.mp3')
    pygame.mixer.music.load("click1.mp3")
    hata1 = pygame.mixer.Sound('click1.mp3')

actsupdater.acts_guncelle(7.142857142857143)
pygame.mixer.music.set_volume(0.5)

print("ilk hazırlık tamamlandı.")

def dirtemizle(temizlenecek, au=True):
    karakterler = ["\\", '"']
    if au:
        return temizlenecek.replace(' (audio)', '').replace('/', ' ').replace(':', ' ').replace('?', '!').replace('*', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace(karakterler[0],'_').replace(karakterler[1], '_')
    else:
        return temizlenecek.replace('/', ' ').replace(':', ' ').replace('?', '!').replace('*', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace(karakterler[0],'_').replace(karakterler[1], '_')
#İlk Başlangıç
def ilkbaslangic(anamenu=0):
    if anamenu == 0 or anamenu == 2 or anamenu == 3:
        muzikres["muzikres"] = 0
        if anamenu == 0:
            pygame.mixer.music.play(loops=0)
        print("normal")
        global root
        root = tk.Tk()
        root.title(f"AcemTubewindow")
        root.iconbitmap("acemtube.ico")
        root.resizable(False, False)
        anapencere = win32gui.FindWindowEx(None, None, None, "AcemTubewindow")
        print(anapencere)
        try:
            win32gui.SetForegroundWindow(anapencere)
            print("Pencere Öne Getirildi!: " + str(win32gui.GetWindowText(anapencere)))
        except Exception as e:
            print("Pencere Öne Getirilemedi! :" + str(e))
        root.title(f"AcemTube ")
        yer = str(root.winfo_screenwidth()/2 - 740/2).split(".")[0]
        yer1 = str(root.winfo_screenheight()/2 - 510/2).split(".")[0]
        root.geometry(f"740x510+{yer}+{yer1}")
        root.attributes("-alpha", seffaflik)

        
    elif anamenu == 1:
        print("anamenü basıldı")
        
    try:
        RPC.update(details="Ana Menüde", start=zmn, large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
    except:
        print("discord yürümüyor.")

    actsupdater.acts_guncelle(bitir=True)
    
    def ses():
        try:
            RPC.update(details="Ses İndirmede", start=zmn, state="Link Giriyor", large_image="acemtubedc", small_image="ses", small_text="320 Kbps'e Kadar Ses İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")      
        except:
            print("hata")    
        try:
            verkutu.destroy()
        except:
            print("sürüm ok.")
        pygame.mixer.Sound.play(click)
        print("ses basıldı")
        engils.destroy()
        disc.destroy()
        discb.destroy()
        engil.destroy()
        
        ses.config(state=DISABLED)
        hkd.config(state=DISABLED)
        video.config(state=DISABLED)
        ayarlar.config(state=DISABLED)
        spotify.config(state=DISABLED)
        cıkıs.config(state=DISABLED)
        ses.destroy()
        hkd.destroy()
        
        video.destroy()
        ayarlar.destroy()
        
        spotify.destroy()
        cıkıs.destroy()
        baslik.destroy()

        global sescik
        sescik = tk.Label(baslikutu, text=f"Ses", bg=acikmavi, fg=baslikyazirengi)
        sescik.config(font=("Montserrat ExtraBold", "30", "italic"))
        sescik.place(relwidth=1, relheight=0.9)

        global sescik1
        sescik1 = tk.Label(baslikutu1, text=f"Lütfen İndirmek İstediğiniz Şarkının Linkini/İsmini Giriniz.", bg=arkaplan, fg=yazirengi)
        sescik1.config(font=("Montserrat Medium", "11"))
        sescik1.place(relwidth=1, relheight=0.1, rely=0.01)
        
        giris = tk.Entry(baslikutu1, width=105, bg=aramarengi, borderwidth=kenargenisligi, relief=stil, fg=yazirengi)
        giris.place(rely=0.1, relx=0.07)
        
        def cikis():
            pygame.mixer.Sound.play(click)
            pygame.mixer.Sound.play(hata)
            root.attributes('-disabled', True)
            
            def anan():
                print("anan")
            print("kapatıldım aq")
            kpw = tk.Tk()
            kpw.title("Emin Misiniz?")
            kpw.resizable(False, False)
            kpw.iconbitmap("acemtubered.ico")
            kpw.protocol("WM_DELETE_WINDOW", anan)
            yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
            yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
            kpw.geometry(f"400x150+{yer2}+{yer3}")
            kpw.attributes("-alpha", seffaflik)
            canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
            canvas.pack()
            emnk = tk.Frame(kpw, bg=arkaplan)
            emnk1 = tk.Frame(kpw, bg=arkaplan)
            emnk.place(relwidth=1, relheight=0.7, rely=0.3)
            emnk1.place(relwidth=1, relheight=0.3)
            emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
            emnb.config(font=("Montserrat ExtraBold", "30", "italic"))
    
            emnb.place(relwidth=1, relheight=0.9)
            
            ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=arkaplan, fg=yazirengi)
            ckyazi.config(font=("Montserrat Medium", "9"))
            ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
            def cikiss():
                pygame.mixer.Sound.play(click)
                try:
                   RPC.close()
                except:
                    print("discord yürütülmeimş")
                try:
                    root.destroy()
                except:
                    pass
                try:
                    kpw.destroy()
                except:
                    pass
                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                exit(0)
            def gri():
                pygame.mixer.Sound.play(click)
                root.attributes('-disabled', False)
                kpw.destroy()
    
            cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
            cikıss.place(rely=0.5, relx= 0.25)
            anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
            anamenuu.place(rely=0.5, relx= 0.57)
            kpw.mainloop()

        def anamenu():
            pygame.mixer.Sound.play(click)
            print("anamenu basıldı")
            baslikutu.destroy()
            baslikutu1.destroy()
            ilkbaslangic(anamenu=1)

        cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
        cikıs.place(rely=0.87, relx= 0.89)
        anamenu = tk.Button(baslikutu1, text=" Ana Menü ", padx=0, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=anamenu)
        anamenu.place(rely=0.8, relx= 0.89)

        def basla():
            try:
                RPC.update(details="Ses İndirmede", start=zmn, state="Kalite Seçiyor", large_image="acemtubedc", small_image="ses", small_text="320 Kbps'e Kadar Ses İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")      
            except:
                print("discord yürümüyor.")
            global kalitebaslik
            kalitebaslik = tk.Label(baslikutu, text=f"Kalite Seçimi", bg=acikmavi, fg=baslikyazirengi)
            kalitebaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            kalitebaslik.place(relwidth=1, relheight=0.9)
            global kaliteyazi
            kaliteyazi = tk.Label(baslikutu1, text=f"Lütfen Aşağıdan Bir Kalite Seçin.", bg=arkaplan, fg=yazirengi)
            kaliteyazi.config(font=("Montserrat Medium", "12"))
            kaliteyazi.place(relwidth=1, relheight=0.1, rely=0.06)
            giris.forget()
            devamke.destroy()


            menu = tk.StringVar()
            menu.set("Kalite Seçiniz")

            pygame.mixer.Sound.play(click)
            sescik1.destroy()
            sescik.destroy()
            def indbasla():
                pygame.mixer.Sound.play(click)
                menub.destroy()
                devamkeeu.destroy()
                kaliteyazi.destroy()
                kalitebaslik.destroy()
                anamenu.config(state=DISABLED)
                cikıs.config(state=DISABLED)

                yenibaslik = tk.Label(baslikutu, text=f"İndiriliyor...", bg=acikmavi, fg=baslikyazirengi)
                yenibaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                yenibaslik.place(relwidth=1, relheight=1)
                def get_yol():
                    with open('data.json', 'r') as f:
                        yol = json.load(f)
                    if "kayit_yolu" in yol:
                        if not yol["kayit_yolu"] == "":
                            return yol["kayit_yolu"]
                        else:
                            return "yok"
                    else:
                        return "yok"
                print(get_yol())
                yaziyeni = tk.Label(baslikutu1, text=f"Lütfen Bekleyin. Ses dosyanız .mp3 halinde kaydedilecek.", bg=arkaplan, fg=yazirengi)
                yaziyeni.config(font=("Montserrat Medium", "12"))
                yaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)
                yuzdeyazi = tk.Label(baslikutu1, text=f"İndirme Başlatılıyor...", bg=arkaplan, fg=yazirengi)
                yuzdeyazi.config(font=("Montserrat Medium", "10"))
                yuzdeyazi.place(relwidth=1, relheight=0.1, rely=0.23)
                kuryazi1 = tk.Label(baslikutu1, text=f"Kaydedilecek Yol: {get_yol()}/Sesler", bg=arkaplan, fg=yazirengi)
                kuryazi1.config(font=("Montserrat Medium", "10"))
                kuryazi1.place(relwidth=1, relheight=0.1, rely=0.3)
                muzikres["muzikres"] = 1
                s = ttk.Style()
                s.theme_use("clam")
                s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
                prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="indeterminate")
                prgs.place(relx=0.265, rely=0.2)
                prgs.start(25)
                linkproc = giris.get()
                if "/shorts/" in linkproc:
                    linkyy = "https://youtu.be/" + str(linkproc.split("/shorts/")[-1])
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Shorts Linki Normal Linke Dönüştürüldü: " + linkproc + " ==> " + linkyy)
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                else:
                    linkyy = linkproc
                link = linkyy
                giris.forget()
                devamke.destroy()
                
                try:
                    if get_yol() != "yok":
                        def get_klt():
                            if menuu == "320kbps        ":
                                return 320
                            elif menuu == "192kbps        ":
                                return 192
                            elif menuu == "160kbps        ":
                                return 160
                            elif menuu == "128kbps        ":
                                return 128
                            elif menuu == "64kbps          ":
                                return 64
                            elif menuu == "32kbps          ":
                                return 2
                        def get_klt1():
                            if menuu == "320kbps        ":
                                return "320kbps"
                            elif menuu == "192kbps        ":
                                return "192kbps"
                            elif menuu == "160kbps        ":
                                return "160kbps"
                            elif menuu == "128kbps        ":
                                return "128kbps"
                            elif menuu == "64kbps          ":
                                return "64kbps"
                            elif menuu == "32kbps          ":
                                return "32kbps"
                        try:
                            RPC.update(details="Ses İndirmede", start=zmn, state=f"İndiriliyor ({get_klt1()})", large_image="acemtubedc", small_image="ses", small_text="320 Kbps'e Kadar Ses İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")      
                        except:
                            print("discord yürümüyor.")
                        rndm = random.randint(0, 10000)
                        ses_yolu = os.path.abspath(get_yol() + f"\Sesler\%(title)s [{rndm}].%(ext)s")
                        liste_orda1 = os.path.isdir(f"{get_yol()}/Sesler")
                        if liste_orda1:
                            print("klasör zaten var")
                        else:
                            os.mkdir(f"{get_yol()}/Sesler")
                            print("klasör yaratıldı")

                        ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'outtmpl': '%(id)s.%(ext)s', 'default_search': 'auto', 'allowplaylist' : False, 'noplaylist' : True,})
                        with ydl:
                            result = ydl.extract_info(
                                link.replace(":", " "),
                                download=False,

                            )
                        if 'entries' in result:
                            video = result['entries'][0]
                        else:
                            # Just a video
                            video = result
                        pp = pprint.PrettyPrinter(indent=1)
                        pp.pprint(video["formats"])

                        vidthumbnail = f"https://img.youtube.com/vi/{video['id']}/maxresdefault.jpg"
                        print("Thumbnail Linki: " + vidthumbnail)
                        ses_kalite_secimi = {}
                        seskaliteler = []
                        boyutliste = []
                        for kalite in video["formats"]:
                            if not "audio only" in kalite["format"] or not kalite["format_id"] == "140":
                                #try:
                                #    vid_blg = kalite["filesize"]
                                #except:
                                #    vid_blg = 50000000
                                #print(kalite["format_id"] + " " + kalite["format"] + kalite["ext"] + " " + str(vid_blg))
                                #kaliteler.append(kalite["format_id"])
                                #boyutjson[str(kalite["format_id"])] = vid_blg
                                pass
                            else:
                                try:
                                    ses_blg = str(kalite["filesize"]) + " byte"
                                except:
                                    ses_blg = "Bilinmiyor."
                                print("Ses Kalitesi: " + kalite["format_id"] + " " + kalite["format"] + " " + kalite["ext"] + " " + ses_blg)
                                seskaliteler.append(kalite["format_id"])
                                ses_kalite_secimi[str(kalite["filesize"])] = str(kalite["format_id"])
                                try:
                                    boyutliste.append(kalite["filesize"])
                                except:
                                    pass
                        
                        sesklt = str(ses_kalite_secimi[str(max(boyutliste))])

                        def prgsbaslat():
                            
                            print(seskaliteler)
                            print(boyutliste)
                            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                            boyut = max(boyutliste)
                            print(boyut)

                            yt_boyut = boyut
                            tamamlanmadı = True
                            prgs.stop()
                            prgs.config(mode="determinate")
                            while tamamlanmadı:
                                onb_klasör = os.listdir(f"{get_yol()}/Sesler")
                                
                                gecerliboyut = 0
                                for onb in onb_klasör:
                                    if "[" + str(rndm) + "]" in onb:
                                        try:
                                            onb_dosya = f"{get_yol()}/Sesler/{onb}"
                                            boyut = os.path.getsize(onb_dosya)
                                            gecerliboyut += boyut
                                        except:
                                            pass
                                    else:
                                        pass
                                
                                yüzdee = 100 * float(gecerliboyut)/float(yt_boyut)

                                if yüzdee > 100:
                                    print("\nYükleme Barı Doldu.")
                                    prgs['value'] = 100
                                    yuzdeyazi.config(text=f".mp3'e Çeviriliyor...")
                                      
                                    break
                                else:
                                    prgs['value'] = yüzdee

                                    yuzdeyazi.config(text=f"%{round(yüzdee, 2)} ({round(float(yt_boyut)/1048576, 2)} MB içinden {round(float(gecerliboyut)/1048576, 2)} MB)")   
                                time.sleep(0.01)

                        prgsthread = threading.Thread(target=prgsbaslat)
                        prgsthread.start()


                        ydl_opts1 = {
                                'format': f'{sesklt}',
                                'default_search': 'auto',
                                'allowplaylist' : False,
                                'noplaylist' : True,
                                'cachedir': False,
                                'outtmpl': ses_yolu,
                                'postprocessors': [{
                                    'key': 'FFmpegExtractAudio',
                                    'preferredcodec': 'mp3',
                                    'preferredquality': f'{get_klt()}',
                                }],
                            }
                        with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
                            print("Ses indiriliyor, Lütfen bekleyin...")
                            ydl.download([link.replace(":", " ")])
                        #sese metadata koy
                        def isimbre():
                            for file in os.listdir(f"{get_yol()}/Sesler/"):
                                if f"[{rndm}].mp3" in file:
                                    return file.split(f"[{rndm}].mp3") 
                        ses_yolu1 = os.path.abspath(get_yol() + f"\Sesler\{isimbre()[0]}[{rndm}].mp3")

                        thumbnail = vidthumbnail
                        updget = requests.get(thumbnail)

                        
                        for chunk in updget.iter_content(chunk_size=chunkboyut):
                            if chunk:
                                    updgetb = chunk
                                    
                        
                        print("Liste/Parça Metadata Yazılıyor.....")

                        thumbsarkipath = ses_yolu1
                        
                        print(thumbsarkipath)

                        audiofile = eyed3.load(thumbsarkipath)
                        
                        if (audiofile.tag == None):
                            audiofile.initTag()
                        
                        audiofile.tag.title = isimbre()[0]
                        audiofile.tag.publisher = "AcemTube"
                        #audiofile.tag.images.set(3, open(thumbdi, 'rb').read(), 'image/jpeg')
                        audiofile.tag.images.set(3, updgetb, 'image/jpeg')
                        audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
                        yenibaslik.destroy()
                        giris.destroy()
                        prgs.destroy()
                        print("Ses Başarıyla İndirildi!")
                        pygame.mixer.Sound.play(tik)
                        dahayenibaslik = tk.Label(baslikutu, text=f"Tamamlandı!", bg=acikyesil, fg=baslikyazirengi)
                        dahayenibaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                        dahayenibaslik.place(relwidth=1, relheight=1)
                        yaziyeni.destroy()
                        yazidahayeni = tk.Label(baslikutu1, text=f"Ses dosyanız .mp3 halinde başarıyla kaydedildi.", bg=arkaplan, fg=yazirengi)
                        yazidahayeni.config(font=("Montserrat Medium", "12"))
                        yazidahayeni.place(relwidth=1, relheight=0.1, rely=0.1)
                        #ad = ses_yolu.split(".")[0]
                        #ade = ad.split("\\")
                        print(get_yol())
                        print(rndm)
                        
                        kuryazi = tk.Label(baslikutu1, text=f"Ses İsmi: {isimbre()[0]}", bg=arkaplan, fg=yazirengi)
                        kuryazi.config(font=("Montserrat Medium", "10"))
                        kuryazi.place(relwidth=1, relheight=0.1, rely=0.2)
                        kuryazi1.config(text=f"Kaydedilen Yol: {get_yol()}/Sesler")
                        anamenu.config(state=NORMAL)
                        cikıs.config(state=NORMAL)
                        
                        try:
                            RPC.update(details="Ses İndirmede", start=zmn, state=f"{isimbre()[0]} İndirildi.", large_image="acemtubedc", small_image="ses", small_text="320 Kbps'e Kadar Ses İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")      
                        except:
                            print("discord yürümüyor.")
                        print(root.state())
                        if root.state() != NORMAL:
                            try:
                                tost.show_toast("Ses Başarıyla İndirildi!",f"{isimbre()[0]} ({get_klt1()})", threaded=True, icon_path=r"./acemtube.ico")
                            except:
                                print("windows 10 değil")
                        def dk():
                            pygame.mixer.Sound.play(click)
                            subprocess.Popen(fr'explorer /select,"{ses_yolu1}"')
                        def oy():
                            pygame.mixer.Sound.play(click)
                            os.startfile(ses_yolu1)
                        oyn = tk.Button(baslikutu1, text=" Oynat ", padx=30, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=oy)
                        oyn.place(rely=0.5, relx= 0.55)
                        dosk = tk.Button(baslikutu1, text=" Klasörde Göster ", padx=5, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dk)
                        dosk.place(rely=0.5, relx= 0.3)
                        time.sleep(1)
                        def get_oto():
                            with open('data.json', 'r') as f:
                                yol = json.load(f)
                            if "oto_play" in yol:
                                return yol["oto_play"]
                            else:
                                return 0
                        if get_oto() == 1:
                            os.startfile(ses_yolu1)
                    else:
                        yenibaslik.destroy()
                        yaziyeni.destroy()
                        prgs.destroy()
                        pygame.mixer.Sound.play(hata1)
                        hatabaslik = tk.Label(baslikutu, text=f"Hata!", bg=kirmizi, fg=baslikyazirengi)
                        hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                        hatabaslik.place(relwidth=1, relheight=1)
                        hatayaziyeni = tk.Label(baslikutu1, text=f"Ses/Video Kayıt Etme Yolu Belirtilmedi. Lütfen Ayarlar Menüsünden Ayarlayınız.", bg=arkaplan, fg=yazirengi)
                        hatayaziyeni.config(font=("Montserrat Medium", "11"))
                        hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)
                        kuryazi1.destroy()
                        anamenu.config(state=NORMAL)
                        cikıs.config(state=NORMAL)
                        if root.state() != NORMAL:
                            try:
                                tost.show_toast("Hata!",f"Ses/Video Kayıt Etme Yolu Belirtilmedi. Lütfen Ayarlar Menüsünden Ayarlayınız.", threaded=True, icon_path=r"./acemtubered.ico")
                            except:
                                print("windows 10 değil")
                except Exception as e:
                    print(e)
                    hatakodu = e
                    pygame.mixer.Sound.play(hata1)
                    giris.destroy()
                    devamke.destroy()
                    sescik.destroy()
                    yaziyeni.destroy()
                    prgs.destroy()
                    yuzdeyazi.destroy()
                    kuryazi1.destroy()
                    hatabaslik = tk.Label(baslikutu, text=f"Hata!", bg=kirmizi, fg=baslikyazirengi)
                    hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    hatabaslik.place(relwidth=1, relheight=1)
                    hatayaziyeni = tk.Label(baslikutu1, text=f"Bir hata oluştu. Lütfen kurulum yaptığınızdan emin olun veya yeni sürüm varsa güncelleyin.", bg=arkaplan, fg=yazirengi)
                    hatayaziyeni.config(font=("Montserrat Medium", "11"))
                    hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)
                    anamenu.config(state=NORMAL)
                    cikıs.config(state=NORMAL)
                    if root.state() != NORMAL:
                        try:
                            tost.show_toast("Hata!",f"Bir hata oluştu. Lütfen kurulum yaptığınızdan emin olun veya yeni sürüm varsa güncelleyin.", threaded=True, icon_path=r"./acemtubered.ico")
                        except:
                            print("windows 10 değil")
                    def bildir():
                        pygame.mixer.Sound.play(click)
                        hatanumara = random.randint(0, 1000000000000)
                        def kld_get():
                            with open('data.json', 'r') as f:
                                klad = json.load(f)
                            if "kullanici_adi" in klad:
                                return klad["kullanici_adi"]
                            else:
                                try:
                                   RPC.close()
                                except:
                                    print("discord yürütülmeimş")
                                    
                                root.destroy()
                                exit(0)

                        print(f"Hata {hatakodu} Bildiriliyor...")
                        bildir.config(state=DISABLED)
                        try:
                            async def hello():
                                uri = server
                                async with websockets.connect(uri) as websocket:
                                    hwidstr = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                                    istek = f"hatabildir-'{kld_get()}' '{datetime.datetime.utcnow() + datetime.timedelta(hours=3)}' 'act{hatanumara}' '{platform.platform()}' '{version}' '{hatakodu}' 'Ses' '{hwidstr}'"
                                    print(f"{istek} İsteği Gönderiliyor")
                                    await websocket.send(istek)
                            asyncio.get_event_loop().run_until_complete(hello())
                        except:
                            pass
                        pygame.mixer.Sound.play(tik)
                        bas1yazi = tk.Label(baslikutu1, text=f"Hata Başarı İle Bildirildi. act{hatanumara} Destek Numaranız İle İletişime Geçebilirsiniz. ", bg=acikyesil, fg=yazirengi)
                        bas1yazi.config(font=("Montserrat Medium", "10"))
                        bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    bildir = tk.Button(baslikutu1, text=" Hata Bildir ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=bildir)
                    bildir.place(rely=0.35, relx= 0.44)
                    if link == "":
                        hatayaziyeni.config(text=f"Link Girilmedi.")
                        bildir.config(state=DISABLED)
                    elif str(e) == "list index out of range":
                        hatayaziyeni.config(text=f"İstenilen Video Bulunamadı!")
                        bildir.config(state=DISABLED)
                    if "[WinError 3] The system cannot find the path specified:" in str(hatakodu):
                        with open('data.json', 'r') as f:
                            ky = json.load(f)
                            ky.pop("kayit_yolu")
                        with open('data.json', 'w') as f:
                            json.dump(ky, f, indent=4)
                        ilkbaslangic(anamenu=1)


            def deney(menu):
                pygame.mixer.Sound.play(click)
                print("brug")
                print(menu)
                global menuu
                menuu = menu
                devamkeeu.config(state=NORMAL)
            
            global menub
            menub = tk.OptionMenu(baslikutu1, menu, "320kbps        ", "192kbps        ","160kbps        ", "128kbps        ", "64kbps          ", "32kbps          ", command=deney)
            menub.config(bg=koyugri, fg=yazirengi, borderwidth=kenargenisligi)
            menub.place(rely=0.19, relx=0.42)
            global devamkeeu
            devamkeeu = tk.Button(baslikutu1, text=" Devam ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, state=DISABLED, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=indbasla).start)
            devamkeeu.place(rely=0.35, relx= 0.45)
            def devambas(bob=None):
                try:
                    devamkeeu.invoke()
                except:
                    giris.unbind('<Return>')
 
            giris.bind('<Return>', devambas)

        time.sleep(0.1)
        devamke = tk.Button(baslikutu1, text=" Devam ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=basla).start)
        devamke.place(rely=0.2, relx= 0.452)
        def girisiac():
            try:
                if not giris.get().strip(" ") == "":
                    devamke.config(state=NORMAL)
                else:
                    devamke.config(state=DISABLED)
            except Exception as e:
                print(e)
            devamke.after(10, girisiac)
        girisiac()
        def devambas(bob=None):
            try:
                devamke.invoke()
            except:
                giris.unbind('<Return>')
 
        giris.bind('<Return>', devambas)

    def video():
        try:
            RPC.update(details="Video İndirmede", start=zmn,  state="Link Giriyor", large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887", small_image="videores", small_text="4K 60FPS Kadar Video İndirebilirsiniz.")
        except:
            print("dc yürümüyor.")
        try:
            verkutu.destroy()
        except:
            print("sürüm ok.")
        pygame.mixer.Sound.play(click)
        print("video basıldı")

        engils.destroy()
        disc.destroy()
        discb.destroy()
        engil.destroy()
        
        ses.config(state=DISABLED)
        hkd.config(state=DISABLED)
        video.config(state=DISABLED)
        ayarlar.config(state=DISABLED)
        spotify.config(state=DISABLED)
        cıkıs.config(state=DISABLED)
        ses.destroy()
        hkd.destroy()

        video.destroy()
        ayarlar.destroy()

        spotify.destroy()
        cıkıs.destroy()
        baslik.destroy()
        global sescik
        sescik = tk.Label(baslikutu, text=f"Video", bg=acikmavi, fg=baslikyazirengi)
        sescik.config(font=("Montserrat ExtraBold", "30", "italic"))
        sescik.place(relwidth=1, relheight=0.9)

        global sescik1
        sescik1 = tk.Label(baslikutu1, text=f"Lütfen İndirmek İstediğiniz Videonun Linkini/İsmini Giriniz.", bg=arkaplan, fg=yazirengi)
        sescik1.config(font=("Montserrat Medium", "11"))
        sescik1.place(relwidth=1, relheight=0.1, rely=0.01)

        global vgiris
        vgiris = tk.Entry(baslikutu1, width=105, bg=aramarengi, borderwidth=kenargenisligi, relief=stil, fg=yazirengi)
        vgiris.place(rely=0.1, relx=0.07)
        def cikis():
            pygame.mixer.Sound.play(click)
            pygame.mixer.Sound.play(hata)
            root.attributes('-disabled', True)
            
            def anan():
                print("anan")
            print("kapatıldım aq")
            kpw = tk.Tk()
            kpw.title("Emin Misiniz?")
            kpw.resizable(False, False)
            kpw.iconbitmap("acemtubered.ico")
            kpw.protocol("WM_DELETE_WINDOW", anan)
            yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
            yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
            kpw.geometry(f"400x150+{yer2}+{yer3}")
            kpw.attributes("-alpha", seffaflik)
            canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
            canvas.pack()
            emnk = tk.Frame(kpw, bg=arkaplan)
            emnk1 = tk.Frame(kpw, bg=arkaplan)
            emnk.place(relwidth=1, relheight=0.7, rely=0.3)
            emnk1.place(relwidth=1, relheight=0.3)
            emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
            emnb.config(font=("Montserrat ExtraBold", "30", "italic"))
    
            emnb.place(relwidth=1, relheight=0.9)
            
            ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=arkaplan, fg=yazirengi)
            ckyazi.config(font=("Montserrat Medium", "9"))
            ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
            def cikiss():
                pygame.mixer.Sound.play(click)
                try:
                   RPC.close()
                except:
                    print("discord yürütülmeimş")
                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                root.destroy()
                kpw.destroy()
                exit(0)
            def gri():
                pygame.mixer.Sound.play(click)
                root.attributes('-disabled', False)
                kpw.destroy()
    
            cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
            cikıss.place(rely=0.5, relx= 0.25)
            anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
            anamenuu.place(rely=0.5, relx= 0.57)
            kpw.mainloop()

        def anamenu():
            pygame.mixer.Sound.play(click)
            print("anamenu basıldı")
            baslikutu.destroy()
            baslikutu1.destroy()
            ilkbaslangic(anamenu=1)

        cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
        cikıs.place(rely=0.87, relx= 0.89)
        anamenu = tk.Button(baslikutu1, text=" Ana Menü ", padx=0, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=anamenu)
        anamenu.place(rely=0.8, relx= 0.89)

        def basla():
            pygame.mixer.Sound.play(click)
            try:
                RPC.update(details="Video İndirmede", start=zmn, state="Kalite Seçiyor", large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887", small_image="videores", small_text="4K 60FPS Kadar Video İndirebilirsiniz.")
            except:
                print("dc yürümüyor.")
            def indbasla():
                pygame.mixer.Sound.play(click)
                
                anamenu.config(state=DISABLED)
                cikıs.config(state=DISABLED)
                
                def klt(pr = True):
                    if pr:
                        print(f"kltmenu {menuu}")
                    if menuu == "2160p 60FPS":
                        if pr:
                            print("315")
                        return 315
                    elif menuu == "4320p":
                        if pr:
                            print("571")
                        return 571
                    elif menuu == "4320p HDR":
                        if pr:
                            print("702")
                        return 702
                    elif menuu == "2160p HDR":
                        if pr:
                            print("701")
                        return 701
                    elif menuu == "1440p HDR":
                        if pr:
                            print("700")
                        return 700
                    elif menuu == "1080p HDR":
                        if pr:
                            print("699")
                        return 699
                    elif menuu == "720p HDR":
                        if pr:
                            print("698")
                        return 698
                    elif menuu == "2160p":
                        if pr:
                            print("313")
                        return 313
                    elif menuu == "1440p 60FPS":
                        if pr:
                            print("308")
                        return 308
                    elif menuu == "1440p":
                        if pr:
                            print("271")
                        return 271
                    elif menuu == "1080p 60FPS":
                        if pr:
                            print("303")
                        return 303
                    elif menuu == "1080p":
                        if pr:
                            print("248")
                        return 248
                    elif menuu == "720p 60FPS":
                        if pr:
                            print("302")
                        return 302
                    elif menuu == "720p":
                        if pr:
                            print("247")
                        return 247
                    elif menuu == "480p":
                        if pr:
                            print("244")
                        return 244
                    elif menuu == "360p":
                        if pr:
                            print("243")
                        return 243
                    elif menuu == "240p":
                        if pr:
                            print("242")
                        return 242
                    elif menuu == "144p":
                        if pr:
                            print("278")
                        return 278
                    elif menuu == "Otomatik":
                        if pr:
                            print("bestvideo")
                        return "bestvideo"


                def klt1():
                    print(f"kltmenu {menuu}")
                    return str(menuu)

                try:
                    RPC.update(details="Video İndirmede", start=zmn, state=f"İndiriliyor ({menuu.strip(' ')})", large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887", small_image="videores", small_text="4K 60FPS Kadar Video İndirebilirsiniz.")
                except:
                    print("dc yürümüyor.")

                kalitebaslik.destroy()
                kaliteyazi.destroy()
                videobaslik = tk.Label(baslikutu, text=f"İndiriliyor...", bg=acikmavi, fg=baslikyazirengi)
                videobaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                videobaslik.place(relwidth=1, relheight=1)
                menub.destroy()
                kanalyazi.destroy()
                adyazi.place(relwidth=1, relheight=0.1, rely=0.3)
                devamkeeu.destroy()
                def get_yol():
                    with open('data.json', 'r') as f:
                        yol = json.load(f)
                    if "kayit_yolu" in yol:
                        if not yol["kayit_yolu"] == "":
                            return yol["kayit_yolu"]
                        else:
                            return "yok"
                    else:
                        return "yok"

                print(get_yol())

                if get_yol() != "yok":        
                    videoyazi = tk.Label(baslikutu1, text=f"Lütfen Bekleyin, Videonuz İndiriliyor.", bg=arkaplan, fg=yazirengi)
                    videoyazi.config(font=("Montserrat Medium", "12"))
                    
                    yüzdesayi = tk.Label(baslikutu1, text=f"%0", bg=arkaplan, fg=yazirengi)
                    yüzdesayi.config(font=("Montserrat Medium", "10"))
                    
                    kuryazi1 = tk.Label(baslikutu1, text=f"Kaydedilecek Yol: {get_yol()}/Videolar", bg=arkaplan, fg=yazirengi)
                    kuryazi1.config(font=("Montserrat Medium", "10"))
                    
                    rndm = random.randint(0, 10000)
                    video_yolu = os.path.abspath(os.path.realpath("Videolar") + f"\{rndm}" f"\%(title)s [{rndm}].%(ext)s")
                    
                    #song_there = os.path.isfile(video_yolu2)
                    muzikres["muzikres"] = 1
                    s = ttk.Style()
                    s.theme_use("clam")
                    s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
                    prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
                    

                    if vidthumbnail != None:
                        
                        videoyazi.place(relwidth=1, relheight=0.1, rely=0.03)
                        adyazi.place(relwidth=1, relheight=0.07, rely=0.54)
                        yüzdesayi.place(relwidth=1, relheight=0.06, rely=0.6)
                        kuryazi1.place(relwidth=1, relheight=0.08, rely=0.65)
                        prgs.place(relx=0.265, rely=0.5)
                    else:
                        videoyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                        yüzdesayi.place(relwidth=1, relheight=0.1, rely=0.23)
                        kuryazi1.place(relwidth=1, relheight=0.1, rely=0.37)
                        prgs.place(relx=0.265, rely=0.2)

                    #prgs.start(25)
                    #if song_there:
                    #    os.remove(video_yolu2)
                    try:
                        liste_orda1 = os.path.isdir(f"{get_yol()}/Videolar")
                        if liste_orda1:
                            print("klasör zaten var")
                        else:
                            os.mkdir(f"{get_yol()}/Videolar")
                            print("klasör yaratıldı")
                        os.mkdir(fr"./Videolar/{rndm}")
                        print(rndm)
                        tamamlanmadı = True
                        print(str(boyutjson[str(klt(pr=False))]) + "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

                        print(boyutjson)
                        
                        print("cuuuuuu /n /n" + str(boyutjson[str(140)]) + "/n /n")
                        
                        
                        

                        def prgsbar():
                            if not klt(pr=False) == "bestvideo":
                                vid_boyut = boyutjson[str(klt(pr=False))]
                                ses_boyut = boyutjson[str(140)]
                                yt_boyut = vid_boyut + ses_boyut

                                while tamamlanmadı:
                                    onb_klasör = os.listdir(fr"./Videolar/{rndm}")
                                    
                                    gecerliboyut = 0
                                    for onb in onb_klasör:
                                        try:
                                            onb_dosya = fr"./Videolar/{rndm}/{onb}"
                                            boyut = os.path.getsize(onb_dosya)
                                            gecerliboyut += boyut
                                        except:
                                            pass
                                        
                                    yüzde = 100 * float(gecerliboyut)/float(yt_boyut)
                                    prgs['value'] = yüzde
                                    
                                    if yüzde > 100:
                                        print("\nYükleme Barı Doldu.")
                                        yüzdesayi.config(text=f"%100")
                                        break
                                    else: 
                                        yüzdesayi.config(text=f"%{round(yüzde, 2)} ({round(float(yt_boyut)/1048576, 2)} MB içinden {round(float(gecerliboyut)/1048576, 2)} MB)")
                                    time.sleep(0.01)

                            else:
                                print("yükleme barı yok")

                        if klt(pr=False) == "bestvideo":
                            prgs.config(mode="indeterminate")
                            prgs.start(25)
                        prgsthread = threading.Thread(target=prgsbar)
                        prgsthread.start()
                        def sesklt():
                            if klt() == "bestvideo":
                                return "bestaudio"
                            else:
                                return 140
                        print(f'{klt()}+{sesklt()}' + " AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                        ydl_opts1 = {
                                'format': f'{klt()}+{sesklt()}',
                                'cachedir': False,
                                'default_search': 'auto',
                                'allowplaylist' : False,
                                'noplaylist' : True,
                                'outtmpl': video_yolu,
                            }
                        with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
                            print("Video indiriliyor, Lütfen bekleyin...")
                            ydl.download([link.replace(":", " ")])
                        def isimbre():
                            for file in os.listdir(f"./Videolar/{rndm}"):
                                if f"[{rndm}]" in file:
                                    return file
                        brug = isimbre().split(".")[-2]
                        print(isimbre())
                        karakterler = ["\\", '"']
                        video_yolu2 = os.path.abspath(os.path.realpath("Videolar") + f"\{rndm}" + f"\{isimbre()}")
                        video_yolu3 = os.path.abspath(get_yol() + f"\Videolar\{dirtemizle(vidbaslik, au=False)} [{rndm}].mp4")
                        video_yolu4 = os.path.abspath(get_yol() + f"\Videolar\{dirtemizle(vidbaslik, au=False)} [{rndm}].mkv")
                        pygame.mixer.Sound.play(dikkat)
                        tamamlanmadı = False
                        print("Video indirildi! Lütfen Format Seçin.")
                        try:
                            RPC.update(details="Video İndirmede", start=zmn, state="Format Seçiyor", large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887", small_image="videores", small_text="4K 60FPS Kadar Video İndirebilirsiniz.")
                        except:
                            print("dc yürümüyor.")
                        vgiris.destroy()
                        devamkeeu.destroy()
                        videoyazi.destroy()
                        videobaslik.destroy()
                        anamenu.config(state=NORMAL)
                        cikıs.config(state=NORMAL)
                        prgs.destroy()
                        kuryazi1.destroy()
                        yüzdesayi.destroy()
                        fobaslik = tk.Label(baslikutu, text=f"Format Seçimi", bg=acikmavi, fg=baslikyazirengi)
                        fobaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                        fobaslik.place(relwidth=1, relheight=1)
                        foyazi = tk.Label(baslikutu1, text=f"Lütfen Aşağıdan Bir Format Seçin.", bg=arkaplan, fg=yazirengi)
                        foyazi.config(font=("Montserrat Medium", "12"))
                        
                        adyazi.destroy()
                        kuryazi23 = tk.Label(baslikutu1, text=f"Video Adı: {vidbaslik}", bg=arkaplan, fg=yazirengi)
                        kuryazi23.config(font=("Montserrat Medium", "10"))
                        
                        
                        if root.state() != NORMAL:
                            try:
                                tost.show_toast("Lütfen Format Seçin!",f"İndirilen: {brug.split(f'[{rndm}]')[0]} ({klt1()})", threaded=True, icon_path=r"./acemtube.ico")
                            except:
                                print("windows 10 değil")
                        def fmp4():
                            pygame.mixer.Sound.play(click)
                            try:
                                RPC.update(details="Video İndirmede", start=zmn, state="Video Çeviriliyor...", large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887", small_image="videores", small_text="4K 60FPS Kadar Video İndirebilirsiniz.")
                            except:
                                print("dc yürümüyor.")
                            
                            fdevam.destroy()
                            menubb.destroy()
                            fobaslik.destroy()
                            foyazi.destroy()
                            kuryazi23.destroy()
                            çevyazi = tk.Label(baslikutu1, text=f"Video .mp4 formatına çevirilip kaydedilecektir.", bg=arkaplan, fg=yazirengi)
                            çevyazi.config(font=("Montserrat Medium", "12"))
                            
                            gecerliyazi = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=yazirengi)
                            gecerliyazi.config(text=f"Başlatılıyor...")
                            gecerliyazi.config(font=("Montserrat Medium", "10"))
                            gecerliyazi.place(relwidth=1, relheight=0.05, rely=0.25)
                            cevadi3 = tk.Label(baslikutu1, text=f"Video Adı: {vidbaslik} [{rndm}]", bg=arkaplan, fg=yazirengi)
                            cevadi3.config(font=("Montserrat Medium", "10"))
                            cevadi3.place(relwidth=1, relheight=0.05, rely=0.31)
                            kuryazi1 = tk.Label(baslikutu1, text=f"Kaydedilecek Yol: {get_yol()}/Videolar", bg=arkaplan, fg=yazirengi)
                            kuryazi1.config(font=("Montserrat Medium", "10"))
                            kuryazi1.place(relwidth=1, relheight=0.05, rely=0.39)
                            çevbaslik = tk.Label(baslikutu, text=f"Çeviriliyor...", bg=acikmavi, fg=baslikyazirengi)
                            çevbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                            çevbaslik.place(relwidth=1, relheight=1)
                            premyazi.destroy()
                            

                            #thumbpre.place(relx=0.5, rely=0.65, anchor=CENTER)
                            muzikres["muzikres"] = 1
                            s = ttk.Style()
                            s.theme_use("clam")
                            s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
                            prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
                            prgs.place(relx=0.265, rely=0.2)

                            if vidthumbnail != None:

                                çevyazi.place(relwidth=1, relheight=0.1, rely=0.03)
                                gecerliyazi.place(relwidth=1, relheight=0.07, rely=0.54)
                                cevadi3.place(relwidth=1, relheight=0.06, rely=0.6)
                                kuryazi1.place(relwidth=1, relheight=0.08, rely=0.65)
                                prgs.place(relx=0.265, rely=0.5)

                            anamenu.config(state=DISABLED)
                            cikıs.config(state=DISABLED)
                            print("Video .mp4'e çeviriliyor...")
                            print("=============================")
                            print(video_yolu2)
                            print(video_yolu3)
                            
                            #ffmpegbaslat = subprocess.call(f'ffmpeg -i "{video_yolu2}" -c:v libx264 -crf 18 -c:a aac -b:a 320k "{video_yolu3}"', shell=True)
                            #for line in ffmpegbaslat.stdout:
                            #    print("satır " + str(line))
                            if not klt() in [571, 702, 701, 700, 699, 698]:
                                framesayisi = int(subprocess.check_output(f'ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 "{video_yolu2}"'))
                                cmd = f'ffmpeg -i "{video_yolu2}" -c:v libx264 -crf 18 -c:a aac -b:a 320k "{video_yolu3}"'
                                #args = cmd.split()

                                def uznal(framesayisi, gecerliframe, fps):
                                    if fps != "0" and fps !="0.0":
                                        hesap = (framesayisi-gecerliframe)/float(fps)
                                        saniye = round(hesap)
                                        uzunluk = str(datetime.timedelta(seconds = saniye))
                                        if uzunluk.startswith("0:"):
                                          return uzunluk[2:].replace('days,', 'gün,')
                                        else:
                                          return uzunluk.replace('days,', 'gün,')
                                    else:
                                        return "Hesaplanıyor..."


                                p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)

                                for line in p.stdout:
                                    print(str(line))
                                    satır = str(line)
                                    if "frame=" in satır:

                                        gecerliframe = int(satır.split("frame=")[-1].split("fps=")[0].replace(" ", ""))
                                        fps = satır.split("frame=")[-1].split("fps=")[-1].split("q=")[0].replace(" ", "")

                                        yüzdee = 100 * gecerliframe/framesayisi

                                        prgs['value'] = yüzdee
                                        #print(uznal((framesayisi-gecerliframe)/float(sifirverme(fps))) + " " + str((framesayisi-gecerliframe)/float(sifirverme(fps))))
                                        gecerliyazi.config(text=f"İlerleme: %{round(yüzdee, 2)} Kalan Süre: {uznal(framesayisi, gecerliframe, fps)} ({framesayisi} Frame İçinden {gecerliframe} FPS: {fps})")


                                print(str(framesayisi + 1) + " adet frame")
                            else:
                                prgs.config(mode="indeterminate")
                                prgs.start(7)
                                gecerliyazi.config(text="Çeviriliyor...")
                                shutil.move(video_yolu2, video_yolu3)

                            #while True:
                            #  chatter = p.stderr.read(1024)
                            #  print("OUTPUT>>> " + str(chatter.rstrip()))
                            
                            kuryazi1.destroy()
                            çevyazi.destroy()
                            çevbaslik.destroy()
                            prgs.destroy()
                            cevadi3.destroy()
                            pygame.mixer.Sound.play(tik)
                            sonyazi = tk.Label(baslikutu1, text=f"Video başarıyla indirilip .mp4 formatına çevirildi!", bg=arkaplan, fg=yazirengi)
                            sonyazi.config(font=("Montserrat Medium", "12"))
                            sonyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                            sonbaslik = tk.Label(baslikutu, text=f"Tamamlandı!", bg=acikyesil, fg=baslikyazirengi)
                            sonbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                            sonbaslik.place(relwidth=1, relheight=1)
                            
                            kuryazi3 = tk.Label(baslikutu1, text=f"Video Adı: {vidbaslik} [{rndm}]", bg=arkaplan, fg=yazirengi)
                            kuryazi3.config(font=("Montserrat Medium", "10"))
                            kuryazi3.place(relwidth=1, relheight=0.1, rely=0.2)
                            kuryazi = tk.Label(baslikutu1, text=f"Kaydedilen Yol: {get_yol()}/Videolar", bg=arkaplan, fg=yazirengi)
                            kuryazi.config(font=("Montserrat Medium", "10"))
                            kuryazi.place(relwidth=1, relheight=0.1, rely=0.3)

                            
                            
                            anamenu.config(state=NORMAL)
                            cikıs.config(state=NORMAL)
                            song_there = os.path.isfile(video_yolu2)
                            try:
                                RPC.update(details="Video İndirmede", start=zmn, state=f"{brug.split(f'[{rndm}]')[0]} ({klt1()}) İndirildi.", large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887", small_image="videores", small_text="4K 60FPS Kadar Video İndirebilirsiniz.")
                            except:
                                print("dc yürümüyor.")
                            if song_there:
                                os.remove(video_yolu2)
                            if root.state() != NORMAL:
                                try:
                                    tost.show_toast("Video Başarıyla İndirildi!",f"{brug.split(f'[{rndm}]')[0]} ({klt1()}) / .mp4)", threaded=True, icon_path=r"./acemtube.ico")
                                except:
                                    print("windows 10 değil")
                            def dk():
                                pygame.mixer.Sound.play(click)
                                subprocess.Popen(fr'explorer /select,"{video_yolu3}"')
                            def oy():
                                pygame.mixer.Sound.play(click)
                                os.startfile(video_yolu3)
                            oyn = tk.Button(baslikutu1, text=" Oynat ", padx=30, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=oy)
                            oyn.place(rely=0.5, relx= 0.55)
                            dosk = tk.Button(baslikutu1, text=" Klasörde Göster ", padx=5, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dk)
                            dosk.place(rely=0.5, relx= 0.3)
                            
                            if vidthumbnail != None:

                                sonyazi.place(relwidth=1, relheight=0.1, rely=0.03)
                                kuryazi3.place(relwidth=1, relheight=0.07, rely=0.5)
                                kuryazi.place(relwidth=1, relheight=0.06, rely=0.56)
                                #kuryazi1.place(relwidth=1, relheight=0.08, rely=0.65)
                                oyn.place(rely=0.65, relx= 0.55)
                                dosk.place(rely=0.65, relx= 0.3)
                                #prgs.place(relx=0.265, rely=0.5)
                            time.sleep(2)
                            def get_oto1():
                                with open('data.json', 'r') as f:
                                    yol = json.load(f)
                                if "oto_play" in yol:
                                    return yol["oto_play"]
                                else:
                                    return 0
                            if get_oto1() == 1:
                                os.startfile(video_yolu3)
                        def fmkv():
                            
                            print("Video .mkv'ye çeviriliyor...")
                            
                            shutil.move(video_yolu2, video_yolu4)
                            kuryazi23.destroy()
                        
                            fdevam.destroy()
                            menubb.destroy()
                            fobaslik.destroy()
                            foyazi.destroy()
                            pygame.mixer.Sound.play(tik)
                            sonyazi = tk.Label(baslikutu1, text=f"Video başarıyla indirilip .mkv formatına çevirildi!", bg=arkaplan, fg=yazirengi)
                            sonyazi.config(font=("Montserrat Medium", "12"))
                            sonyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                            sonbaslik = tk.Label(baslikutu, text=f"Tamamlandı!", bg=acikyesil, fg=baslikyazirengi)
                            sonbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                            sonbaslik.place(relwidth=1, relheight=1)
                            kuryazi3 = tk.Label(baslikutu1, text=f"Video Adı: {vidbaslik} [{rndm}]", bg=arkaplan, fg=yazirengi)
                            kuryazi3.config(font=("Montserrat Medium", "10"))
                            kuryazi3.place(relwidth=1, relheight=0.1, rely=0.2)
                            kuryazi = tk.Label(baslikutu1, text=f"Kaydedilen Yol: {get_yol()}/Videolar", bg=arkaplan, fg=yazirengi)
                            kuryazi.config(font=("Montserrat Medium", "10"))
                            kuryazi.place(relwidth=1, relheight=0.1, rely=0.3)
                            anamenu.config(state=NORMAL)
                            cikıs.config(state=NORMAL)
                            try:
                                RPC.update(details="Video İndirmede", start=zmn, state=f"{vidbaslik} İndirildi.", large_image="acemtubedc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887", small_image="videores", small_text="4K 60FPS Kadar Video İndirebilirsiniz.")
                            except:
                                print("dc yürümüyor.")
                            if root.state() != NORMAL:
                                try:
                                    tost.show_toast("Video Başarıyla İndirildi!",f"{vidbaslik} [{rndm}] ({klt1()} / .mkv)", threaded=True, icon_path=r"./acemtube.ico")
                                except:
                                    print("windows 10 değil")
                            def dk():
                                pygame.mixer.Sound.play(click)
                                subprocess.Popen(fr'explorer /select,"{video_yolu4}"')
                            def oy():
                                pygame.mixer.Sound.play(click)
                                os.startfile(video_yolu4)
                            oyn = tk.Button(baslikutu1, text=" Oynat ", padx=30, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=oy)
                            oyn.place(rely=0.5, relx= 0.55)
                            dosk = tk.Button(baslikutu1, text=" Klasörde Göster ", padx=5, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dk)
                            dosk.place(rely=0.5, relx= 0.3)
                            premyazi.destroy()
                            thumbpre.place(relx=0.5, rely=0.76, anchor=CENTER)
                            time.sleep(2)
                            def get_oto2():
                                with open('data.json', 'r') as f:
                                    yol = json.load(f)
                                if "oto_play" in yol:
                                    return yol["oto_play"]
                                else:
                                    return 0
                            if get_oto2() == 1:
                                os.startfile(video_yolu4)
                        devamkeeu.destroy()
                        #global mp4
                        #mp4 = tk.Button(baslikutu1, text=" .mp4 ", padx=50, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=fmp4).start)
                        #mp4.place(rely=0.4, relx= 0.2)
                        #global mkv
                        #mkv = tk.Button(baslikutu1, text=" .mkv ", padx=50, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=fmkv).start)
                        #mkv.place(rely=0.4, relx= 0.62)
                        formlist = [".mp4"]

                        if not klt() in [571, 702, 701, 700, 699, 698]:
                            formlist.append(".mkv")
                        
                        menu = tk.StringVar()
                        menu.set("Format Seçiniz")
                        def convbaslat():
                            if menu.get() == ".mp4":
                                mpt = threading.Thread(target=fmp4)
                                mpt.start()
                            elif menu.get() == ".mkv":
                                mkt = threading.Thread(target=fmkv)
                                mkt.start()

                        def deney(menu):
                            pygame.mixer.Sound.play(click)
                            print("brug")
                            print(menu)
 
                            fdevam.config(state=NORMAL)
                        global menubb
                        menubb = tk.OptionMenu(baslikutu1, menu, *formlist, command=deney)
                        menubb.config(bg=koyugri, fg=yazirengi, borderwidth=kenargenisligi)
                        
                        global fdevam
                        fdevam = tk.Button(baslikutu1, text=" Devam ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, state=DISABLED, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=convbaslat).start)
                        

                        if vidthumbnail != None:
                            foyazi.place(relwidth=1, relheight=0.1, rely=0.03)
                            kuryazi23.place(relwidth=1, relheight=0.1, rely=0.5)
                            menubb.place(rely=0.63, relx= 0.5, anchor=CENTER)
                            fdevam.place(rely=0.72, relx= 0.5, anchor=CENTER)
                        else:
                            foyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                            kuryazi23.place(relwidth=1, relheight=0.1, rely=0.2)
                            menubb.pack(pady=150)
                            fdevam.place(rely=0.45, relx= 0.454)
                        
                        def devambas(bob=None):
                            try:
                                fdevam.invoke()
                            except Exception as e:
                                print(e)
                                root.unbind('<Return>')
                        root.bind('<Return>', devambas)
                        
                        
                    except Exception as e:
                        hatakodu = e
                        
                        print(str(hatakodu) + "hataaaaaaaaaaaaa")
                        kalite1 = klt()
                        kalite = klt1()
                        pygame.mixer.Sound.play(hata1)
                        videobaslik.destroy()
                        videoyazi.destroy()
                        try:
                            thumbpre.destroy()
                        except:
                            pass
                        hatabaslik = tk.Label(baslikutu, text=f"Hata!", bg=kirmizi, fg=baslikyazirengi)
                        hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                        hatabaslik.place(relwidth=1, relheight=1)
                        hatayaziyeni = tk.Label(baslikutu1, text=f"Bir Hata Oluştu. Videoda Belirtilen Kalite Olmayabilir. Eğer Var İse Kurulum Yaptığınızdan Emin Olunuz.", bg=arkaplan, fg=yazirengi)
                        hatayaziyeni.config(font=("Montserrat Medium", "9"))
                        hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)
                        anamenu.config(state=NORMAL)
                        prgs.destroy()
                        kuryazi1.destroy()
                        cikıs.config(state=NORMAL)
                        if root.state() != NORMAL:
                            try:
                                tost.show_toast("Hata!",f"Bir Hata Oluştu. Videoda Belirtilen Kalite Olmayabilir. Eğer Var İse Kurulum Yaptığınızdan Emin Olunuz.", threaded=True, icon_path=r"./acemtubered.ico")
                            except:
                                print("windows 10 değil")
                        def bildir():
                            pygame.mixer.Sound.play(click)
                            hatanumara = random.randint(0, 1000000000000)
                            def kld_get():
                                with open('data.json', 'r') as f:
                                    klad = json.load(f)
                                if "kullanici_adi" in klad:
                                    return klad["kullanici_adi"]
                                else:
                                    try:
                                       RPC.close()
                                    except:
                                        print("discord yürütülmeimş")
                                    subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                                    root.destroy()
                                    exit(0)

                            print(f"Hata {hatakodu} Bildiriliyor...")
                            bildir.config(state=DISABLED)
                            try:
                                async def hello():
                                    uri = server
                                    async with websockets.connect(uri) as websocket:
                                        hwidstr = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                                        istek = f"hatabildir-'{kld_get()}' '{datetime.datetime.utcnow() + datetime.timedelta(hours=3)}' 'act{hatanumara}' '{platform.platform()}' '{version}' '{hatakodu}' 'Video' '{hwidstr}'"
                                        print(f"{istek} İsteği Gönderiliyor")
                                        await websocket.send(istek)
                                asyncio.get_event_loop().run_until_complete(hello())
                            except:
                                pass
                            pygame.mixer.Sound.play(tik)
                            bas1yazi = tk.Label(baslikutu1, text=f"Hata Başarı İle Bildirildi. act{hatanumara} Destek Numaranız İle İletişime Geçebilirsiniz. ", bg=acikyesil, fg=yazirengi)
                            bas1yazi.config(font=("Montserrat Medium", "10"))
                            bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                        bildir = tk.Button(baslikutu1, text=" Hata Bildir ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=bildir)
                        bildir.place(rely=0.35, relx= 0.44)
                        if "[WinError 3] The system cannot find the path specified:" in str(hatakodu):
                            with open('data.json', 'r') as f:
                                ky = json.load(f)
                                ky.pop("kayit_yolu")
                            with open('data.json', 'w') as f:
                                json.dump(ky, f, indent=4)
                            ilkbaslangic(anamenu=1)
                else:
                    videobaslik.destroy()
                    pygame.mixer.Sound.play(hata1)
                    hatabaslik = tk.Label(baslikutu, text=f"Hata!", bg=kirmizi, fg=baslikyazirengi)
                    hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    hatabaslik.place(relwidth=1, relheight=1)
                    hatayaziyeni = tk.Label(baslikutu1, text=f"Ses/Video Kayıt Etme Yolu Belirtilmedi. Lütfen Ayarlar Menüsünden Ayarlayınız.", bg=arkaplan, fg=yazirengi)
                    hatayaziyeni.config(font=("Montserrat Medium", "11"))
                    hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)
                    anamenu.config(state=NORMAL)
                    cikıs.config(state=NORMAL)
                    time.sleep(0.5)
                    print(root.state)
                    if root.state == DISABLED:
                        try:
                            tost.show_toast("Hata!",f"Ses/Video Kayıt Etme Yolu Belirtilmedi. Lütfen Ayarlar Menüsünden Ayarlayınız.", threaded=True, icon_path=r"./acemtubered.ico")
                        except:
                            print("windows 10 değil")
            try:      
                sescik1.destroy()
                sescik.destroy()
                linkproc = vgiris.get()
                if "/shorts/" in linkproc:
                    linkyy = "https://youtu.be/" + str(linkproc.split("/shorts/")[-1])
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("Shorts Linki Normal Linke Dönüştürüldü: " + linkproc + " ==> " + linkyy)
                    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
                else:
                    linkyy = linkproc

                global link
                link = linkyy
                print(link)
                vgiris.destroy()
                devamke.destroy()
                #kalite alma ekranı

                arabaslik = tk.Label(baslikutu, text=f"Bilgiler Alınıyor...", bg=acikyesil, fg=baslikyazirengi)
                arabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                arabaslik.place(relwidth=1, relheight=1)
                arayazi = tk.Label(baslikutu1, text=f"Verilen Videonun Bilgileri Alınıyor...", bg=arkaplan, fg=yazirengi)
                arayazi.config(font=("Montserrat Medium", "12"))
                arayazi.place(relwidth=1, relheight=0.1, rely=0.03)
                muzikres["muzikres"] = 1
                s = ttk.Style()
                s.theme_use("clam")
                s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi2, troughcolor=koyugri, bordercolor=cubukrengi2, darkcolor=cubukrengi2, lightcolor=cubukrengi2)
                prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
                prgs.place(relx=0.265, rely=0.15)
                anamenu.config(state=DISABLED)
                cikıs.config(state=DISABLED)

                time.sleep(0.5)
                ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s', 'default_search': 'auto', 'allowplaylist' : False, 'noplaylist' : True,})
                prgs['value'] += 16.66666666666667

                with ydl:
                    result = ydl.extract_info(
                        link.replace(":", " "),
                        download=False,

                    )
                prgs['value'] += 16.66666666666667

                if 'entries' in result:
                    video = result['entries'][0]
                else:
                    # Just a video
                    video = result
                prgs['value'] += 16.66666666666667
                vidthumbnail = None
                try:
                    vidbaslik = video["title"]
                    vidkanal = video["channel"]
                    vidthumbnail = f"https://img.youtube.com/vi/{video['id']}/maxresdefault.jpg"
                except:
                    vidbaslik = "Bilinmiyor."
                    vidkanal =  "Bilinmiyor."
                    print("Youtube Değil")
                print(vidthumbnail)
                adyazi = tk.Label(baslikutu1, text=f"Video Adı: {vidbaslik}", bg=arkaplan, fg=yazirengi)
                adyazi.config(font=("Montserrat Medium", "10"))
                adyazi.place(relwidth=1, relheight=0.1, rely=0.2)
                kanalyazi = tk.Label(baslikutu1, text=f"Kanal Adı: {vidkanal}", bg=arkaplan, fg=yazirengi)
                kanalyazi.config(font=("Montserrat Medium", "10"))
                kanalyazi.place(relwidth=1, relheight=0.07, rely=0.28)
                
                    
                prgs.place(relx=0.265, rely=0.15)
                if vidthumbnail != None:
                    print("thumbbbb")
                    prekapakd = requests.get(vidthumbnail)
                    print("ayak")
                    for chunk in prekapakd.iter_content(chunk_size=chunkboyut):
                        if chunk:
                            prekapakurld = chunk
                    print("pop")
                    thumbkapakc = Image.open(BytesIO(prekapakurld))
                   
                    thumbres = thumbkapakc.resize((resim_aletleri.genislikal(thumbkapakc, 150), 150), Image.Resampling.LANCZOS)
                    print("geneg")

                    global thumbbb
                    thumbbb = ImageTk.PhotoImage(thumbres)
                    print("genego")
                    thumbpre = tk.Label(baslikutu1, image=thumbbb, bg=arkaplan ,fg=acikgri2)
                    print("moo")
                    prgs.place(relx=0.265, rely=0.5)
                    adyazi.place(relwidth=1, relheight=0.1, rely=0.55)
                    kanalyazi.place(relwidth=1, relheight=0.07, rely=0.63)

                    thumbpre.place(relx=0.5, rely=0.3, anchor=CENTER)

                    print("genegeeeeeeeee")

                video_url = video
                print(vidbaslik)
                #print(video["formats"])
                print(vidkanal)

                pp = pprint.PrettyPrinter(indent=1)
                pp.pprint(video["formats"])
                prgs['value'] += 16.66666666666667
                print(vidthumbnail)

                kaliteler = []
                seskaliteler = []
                boyutjson = {
                    "bestvideo": 5000000
                }
                print("======================AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=====================")
                print(boyutjson)
                for kalite in video["formats"]:
                    if not "audio only" in kalite["format"] or kalite["format_id"] == "140":
                        try:
                            vid_blg = kalite["filesize"]
                        except:
                            vid_blg = 50000000
                        print(kalite["format_id"] + " " + kalite["format"] + kalite["ext"] + " " + str(vid_blg))
                        kaliteler.append(kalite["format_id"])
                        boyutjson[str(kalite["format_id"])] = vid_blg
                    else:
                        try:
                            ses_blg = str(kalite["asr"]) + " " + str(kalite["acodec"]) + " " + str(kalite["filesize"])
                        except:
                            ses_blg = "Bilinmiyor."
                        print("Ses Kalitesi: " + kalite["format_id"] + " " + kalite["format"] + " " + kalite["ext"] + " " + ses_blg)
                        seskaliteler.append(kalite["format_id"])

                print(kaliteler)
                prgs['value'] += 16.66666666666667
                time.sleep(0.1)
                prgs['value'] += 16.66666666666667
                time.sleep(0.2)
                kutukalite = []
                if "702" in kaliteler:
                    print(print("8K HDR"))
                    kutukalite.append("4320p HDR")
                if "571" in kaliteler:
                    print("8K")
                    kutukalite.append("4320p")
                if "701" in kaliteler:
                    print("4K HDR")
                    kutukalite.append("2160p HDR")
                if "315" in kaliteler:
                    print("4K/4K 60FPS ")
                    kutukalite.append("2160p 60FPS")
                if "313" in kaliteler:
                    print("4K/4K 30FPS ")
                    kutukalite.append("2160p")
                if "700" in kaliteler:
                    print("1440p HDR")
                    kutukalite.append("1440p HDR")
                if "308" in kaliteler:
                    print("2K/2K 60FPS")
                    kutukalite.append("1440p 60FPS")
                if "271" in kaliteler:
                    print("2K/2K 60FPS ")
                    kutukalite.append("1440p")
                if "699" in kaliteler:
                    print("1080p HDR")
                    kutukalite.append("1080p HDR")
                if "303" in kaliteler:
                    print("1080p 60FPS")
                    kutukalite.append("1080p 60FPS")
                if "248" in kaliteler:
                    print("1080p")
                    kutukalite.append("1080p")
                if "698" in kaliteler:
                    print("720p HDR")
                    kutukalite.append("720p HDR")
                if "302" in kaliteler:
                    print("720p 60FPS")
                    kutukalite.append("720p 60FPS")
                if "247" in kaliteler:
                    print("720p")
                    kutukalite.append("720p")
                if "244" in kaliteler:
                    print("480p")
                    kutukalite.append("480p")
                if "243" in kaliteler:
                    print("360p")
                    kutukalite.append("360p")
                if "242" in kaliteler:
                    print("240p")
                    kutukalite.append("240p")
                if "278" in kaliteler:
                    print("144p")
                    kutukalite.append("144p")
                kutukalite.append("Otomatik")
                print(kutukalite)


                prgs['value'] += 16.66666666666667

                prgs.destroy()
                arabaslik.destroy()
                arayazi.destroy()
                global kalitebaslik

                kalitebaslik = tk.Label(baslikutu, text=f"Kalite Seçimi", bg=acikmavi, fg=baslikyazirengi)
                kalitebaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                kalitebaslik.place(relwidth=1, relheight=0.9)
                global kaliteyazi
                kaliteyazi = tk.Label(baslikutu1, text=f"Lütfen Aşağıdan Bir Kalite Seçin.", bg=arkaplan, fg=yazirengi)
                kaliteyazi.config(font=("Montserrat Medium", "12"))
                kaliteyazi.place(relwidth=1, relheight=0.1, rely=0.03)
                premyazi = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=kirmiziyazi)
                premyazi.config(font=("Montserrat Medium", "12"))
                
                anamenu.config(state=NORMAL)
                cikıs.config(state=NORMAL)

                menu = tk.StringVar()
                menu.set("Kalite Seçiniz")

                def deney(menu):
                    pygame.mixer.Sound.play(click)
                    print("Kalite Seçimi Değiştirildi: '" + menu +"'")

                    global menuu
                    menuu = menu
                    premres = ["4320p", "2160p 60FPS", "2160p", "1440p 60FPS", "1440p", "1080p 60FPS", "1080p", "720p 60FPS", "720p", "Otomatik"]
                    if cevap == "7" or "[7]-" in cevap:
                        if menu in premres: 
                            devamkeeu.config(state=DISABLED)
                            premyazi.config(text="Bu Kaliteyi Kullanmak İçin AcemTube Premium'a İhtiyacınız Var.")
                            pygame.mixer.Sound.play(hata)
                        else:
                            devamkeeu.config(state=NORMAL)
                            premyazi.config(text="")
                    else:
                        devamkeeu.config(state=NORMAL)
                        premyazi.config(text="")

                global menub
                
                menub = tk.OptionMenu(baslikutu1, menu, *kutukalite, command=deney)
                menub.config(bg=koyugri, fg=yazirengi, borderwidth=kenargenisligi)
                #menub.place(rely=0.35, relx=0.42)
                menub.pack(pady=150)
                global devamkeeu
                devamkeeu = tk.Button(baslikutu1, text=" Devam ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, state=DISABLED, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=indbasla).start)
                devamkeeu.place(rely=0.45, relx= 0.45)

                if vidthumbnail != None:
                    adyazi.place(relwidth=1, relheight=0.1, rely=0.48)
                    kanalyazi.place(relwidth=1, relheight=0.08, rely=0.55)
                    menub.place(rely=0.66, relx= 0.5, anchor=CENTER)
                    devamkeeu.place(rely=0.75, relx= 0.5, anchor=CENTER)
                    premyazi.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.83 , anchor=CENTER)
                else:
                    premyazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    adyazi.place(relwidth=1, relheight=0.1, rely=0.15)
                    kanalyazi.place(relwidth=1, relheight=0.08, rely=0.23)
                    menub.pack(pady=150)
                    devamkeeu.place(rely=0.45, relx= 0.45)
                def devambas(bob=None):
                    try:
                        devamkeeu.invoke()
                    except:
                        root.unbind('<Return>')
        
                root.bind('<Return>', devambas)
            except Exception as e:
                pygame.mixer.Sound.play(hata1)
                print("____Hata_____")
                print(e)
                hatakodu = e

                try:
                    arayazi.destroy()
                except:
                    pass
                try:
                    prgs.destroy()
                except:
                    pass
                try:
                    kanalyazi.destroy()
                except:
                    pass
                try:
                    adyazi.destroy()
                except:
                    pass
                try:
                    arabaslik.destroy()
                except:
                    pass
                hatabaslik = tk.Label(baslikutu, text=f"Hata!", bg=kirmizi, fg=baslikyazirengi)
                hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                hatabaslik.place(relwidth=1, relheight=1)
                hatayaziyeni = tk.Label(baslikutu1, text=f"Bir hata oluştu. Video Bilgileri Alınamadı.", bg=arkaplan, fg=yazirengi)
                hatayaziyeni.config(font=("Montserrat Medium", "11"))
                hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)

                anamenu.config(state=NORMAL)
                cikıs.config(state=NORMAL)
                def bildir():
                    
                    pygame.mixer.Sound.play(click)
                    hatanumara = random.randint(0, 1000000000000)
                    def kld_get():
                        with open('data.json', 'r') as f:
                            klad = json.load(f)
                        if "kullanici_adi" in klad:
                            return klad["kullanici_adi"]
                        else:
                            try:
                               RPC.close()
                            except:
                                print("discord yürütülmeimş")
                            subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                            root.destroy()
                            exit(0)

                    print(f"Hata {hatakodu} Bildiriliyor...")
                    bildir.config(state=DISABLED)
                    try:
                        async def hello():
                            uri = server
                            async with websockets.connect(uri) as websocket:
                                hwidstr = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                                istek = f"hatabildir-'{kld_get()}' '{datetime.datetime.utcnow() + datetime.timedelta(hours=3)}' 'act{hatanumara}' '{platform.platform()}' '{version}' '{hatakodu}' 'Video Bilgi' '{hwidstr}'"
                                print(f"{istek} İsteği Gönderiliyor")
                                await websocket.send(istek)
                        asyncio.get_event_loop().run_until_complete(hello())
                    except:
                        pass
                    pygame.mixer.Sound.play(tik)
                    bas1yazi = tk.Label(baslikutu1, text=f"Hata Başarı İle Bildirildi. act{hatanumara} Destek Numaranız İle İletişime Geçebilirsiniz. ", bg=acikyesil, fg=yazirengi)
                    bas1yazi.config(font=("Montserrat Medium", "10"))
                    bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                bildir = tk.Button(baslikutu1, text=" Hata Bildir ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=bildir)
                bildir.place(rely=0.35, relx= 0.44)
                if link == "":
                    hatayaziyeni.config(text=f"Link Girilmedi.")
                    bildir.config(state=DISABLED)
                elif str(e) == "list index out of range":
                    hatayaziyeni.config(text=f"İstenilen Video Bulunamadı!")
                    bildir.config(state=DISABLED)
                    
                if root.state() != NORMAL:
                    try:
                        tost.show_toast("Hata!",f"Bir hata oluştu. Video Bilgileri Alınamadı.", threaded=True, icon_path=r"./acemtubered.ico")
                    except:
                        print("windows 10 değil")
        time.sleep(0.1)
        devamke = tk.Button(baslikutu1, text=" Devam ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=basla).start)
        devamke.place(rely=0.2, relx= 0.45)
        def girisiac():
            try:
                if not vgiris.get().strip(" ") == "":
                    devamke.config(state=NORMAL)
                else:
                    devamke.config(state=DISABLED)
            except Exception as e:
                print(e)
            devamke.after(10, girisiac)
        girisiac()
        def devambas(bob=None):
            try:
                devamke.invoke()
            except:
                vgiris.unbind('<Return>')
 
        vgiris.bind('<Return>', devambas)

    def spotify():
        try:
            RPC.update(details="Spotify İndirmede", state="Link Giriyor", start=zmn, large_image="acemtubedc", small_image="spotify", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
        except:
            print("dc yürümüyor.")
        try:
            verkutu.destroy()
        except:
            print("sürüm ok.")
        pygame.mixer.Sound.play(click)
        print("spotify basıldı")
        ses.config(state=DISABLED)
        hkd.config(state=DISABLED)
        video.config(state=DISABLED)
        ayarlar.config(state=DISABLED)
        spotify.config(state=DISABLED)
        cıkıs.config(state=DISABLED)
        ses.destroy()
        hkd.destroy()

        video.destroy()
        ayarlar.destroy()

        spotify.destroy()
        cıkıs.destroy()
        baslik.destroy()
        engils.destroy()
        baslik.destroy()
        likbaslik = tk.Label(baslikutu, text=f"Spotify", bg=acikyesil, fg=baslikyazirengi)
        likbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
        likbaslik.place(relwidth=1, relheight=1)
        yakyazi = tk.Label(baslikutu1, text=f"Lütfen İndirmek İstediğiniz Listenin/Albümün/Şarkının Linkini Yapıştırınız.", bg=arkaplan, fg=yazirengi)
        yakyazi.config(font=("Montserrat Medium", "12"))
        yakyazi.place(relwidth=1, relheight=0.1, rely=0.03)
        
        def get_yol():
            with open('data.json', 'r') as f:
                yol = json.load(f)
            if "kayit_yolu" in yol:
                if not yol["kayit_yolu"] == "":
                    return yol["kayit_yolu"]
                else:
                    return "Yok"
            else:
                return "Yok"

        def basla():
            pygame.mixer.Sound.play(click)
            anamenu.config(state=DISABLED)
            cikıs.config(state=DISABLED)
            
            if get_yol() != "Yok":
                def indir():
                    pygame.mixer.Sound.play(click)
                    anamenu.config(state=DISABLED)
                    cikıs.config(state=DISABLED)
                    
                    lbaslik.destroy()
                    lyazi.destroy()
                    devamkee.destroy()
                    shpyazi.destroy()

                    #prekapakk.place(rely=0.6, relx=0.5, anchor=CENTER)


                    try:
                        RPC.update(details="Spotify İndiriyor", state=f"{isim} Adlı {mod} İndiriliyor", start=zmn, large_image="acemtubedc", small_image="spotify", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                    except:
                        print("dc yürümüyor.")
                    ibaslik = tk.Label(baslikutu, text=f"İndiriliyor...", bg=acikmavi, fg=baslikyazirengi)
                    ibaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    ibaslik.place(relwidth=1, relheight=1)
                    iyazi = tk.Label(baslikutu1, text=f"{isim} Adlı {mod} İndiriliyor Lütfen Bekleyin...", bg=arkaplan, fg=yazirengi)
                    iyazi.config(font=("Montserrat Medium", "13"))
                    iyazi.place(relwidth=1, relheight=0.1, rely=0.07)

                    indyazi = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=yazirengi)
                    indyazi.config(text=f"İlerleme: %0 ({listesayi} Parça içinden 0 Parça)")
                    indyazi.config(font=("Montserrat Medium", "10"))
                    indyazi.place(relwidth=1, relheight=0.05, rely=0.25)

                    gecerliyazi = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=yazirengi)
                    gecerliyazi.config(text=f"Başlatılıyor...")
                    gecerliyazi.config(font=("Montserrat Medium", "10"))
                    gecerliyazi.place(relwidth=1, relheight=0.05, rely=0.3)
                    muzikres["muzikres"] = 1
                    s = ttk.Style()
                    s.theme_use("clam")
                    s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
                    prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
                    prgs.place(relx=0.265, rely=0.17)
                    prgs.config(mode="indeterminate")
                    prgs.start(7)

                    
                        
                    
                    #s = ttk.Style()
                    #s.theme_use("clam")
                    #s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi2, troughcolor=koyugri, bordercolor=cubukrengi2, darkcolor=cubukrengi2, lightcolor=cubukrengi2)
                    #prgs1 = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
                    #prgs1.place(relx=0.265, rely=0.37)
                    

                    
                    yolyazi = tk.Label(baslikutu1, text=f"Kaydedilecek Yol: {get_yol()}/Spotify/{yapan}/{isim}", bg=arkaplan, fg=yazirengi)
                    yolyazi.config(font=("Montserrat Medium", "9"))
                    yolyazi.place(relwidth=1, relheight=0.05, rely=0.35)

                    if prekapak != None:
                        prekapakk.place(rely=0.3, relx=0.5, anchor=CENTER)
                        iyazi.place(relwidth=1, relheight=0.05, rely=0.04)
                        indyazi.place(relwidth=1, relheight=0.05, rely=0.6)
                        gecerliyazi.place(relwidth=1, relheight=0.05, rely=0.65)
                        yolyazi.place(relwidth=1, relheight=0.05, rely=0.7)
                        prgs.place(relx=0.265, rely=0.52)
                    
                    liste_orda1 = os.path.isdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}")
                    liste_orda7 = os.path.isdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}")
                    liste_orda69 = os.path.isdir(f"{get_yol()}/Spotify")
                    if liste_orda69:
                        print("klasör var")
                    else:
                        try:
                            os.mkdir(f"{get_yol()}/Spotify/")
                        except:
                            with open('data.json', 'r') as f:
                                ky = json.load(f)
                                ky.pop("kayit_yolu")
                            with open('data.json', 'w') as f:
                                json.dump(ky, f, indent=4)
                            ilkbaslangic(anamenu=1)

                            
                        print("klasör yaratıldı")
                    
                    if liste_orda7:
                        print("klasör var")
                    else:
                        os.mkdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}")
                        print("klasör yaratıldı")
                    geçilecek = []
                    if liste_orda1:
                        #print("klasör siliniyor")
                        #shutil.rmtree(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}")
                        #os.mkdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}")
                        print("Klasörde zaten var olup geçilecek şarkılar alınıyor...")
                        geçilecek = os.listdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}")
                        baslik_dtemiz = []
                        for baslk in baslik_listesi:
                            baslik_dtemiz.append(dirtemizle(baslk) + ".mp3")
                        for geçilcek in geçilecek:
                            if geçilcek not in baslik_dtemiz:
                                print("İstenmeyen Parça: " + f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{geçilcek}") 
                                try:
                                    os.remove(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{geçilcek}")
                                except Exception as e:
                                    print("Silinemedi :" + str(e))
                                if geçilcek.endswith(".m4a") or geçilcek.endswith(".part"):
                                    try:
                                        print("Bozuk MP3 kontrol ediliyor....")
                                        os.remove(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{geçilcek.replace('.m4a', '.mp3')}")
                                    except:
                                        try:
                                            os.remove(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{geçilcek.replace('.part', '.mp3')}")
                                        except:
                                            pass
                    else:
                        os.mkdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}")
                        print("klasör yaratıldı")
                    karakterler = ["\\", '"']
                    
                    eklenecek = 100 / listesayi
                    indirildi = 0
                    yuzdeee = 0
                    bar = 0
                    for sarki in baslik_listesi:
                        spt_yolu = os.path.abspath(get_yol() + f"\Spotify\{dirtemizle(yapan)}\{dirtemizle(isim)}\{dirtemizle(sarki)}.%(ext)s")
                        spt_son = os.path.abspath(get_yol() + f"\Spotify\{dirtemizle(yapan)}\{dirtemizle(isim)}\{dirtemizle(sarki)}.mp3")
                        time.sleep(0.1)
                        print(sarki + " indiriliyor...")

                        if mod == "Liste":
                            thumbnail = coverlist[sarki]
                            updget = requests.get(thumbnail)

                            for chunk in updget.iter_content(chunk_size=chunkboyut):
                                if chunk:
                                    thumbdi = chunk


                            prekapakop = Image.open(BytesIO(thumbdi)).resize((170,170), Image.Resampling.LANCZOS)
                            global prekapaku
                            prekapaku = ImageTk.PhotoImage(prekapakop)
                            prekapakk.config(image=prekapaku)
                        try:
                            gecerliyazi.config(text=f"İndirilen: %0 {sarki.replace(' (audio)', '')}")
                            bittibitmedi = []
                            if not f"{dirtemizle(sarki)}.mp3" in geçilecek:
                                print(f"Temizlenmiş : '{sarki}'")
                                try:
                                    ytm = ytmusicapi.YTMusic()
                                    videoId = ytm.search(sarki)[0]["videoId"]
                                    print("videoid--------------")
                                    print(videoId)
                                    if str(videoId) == 'videoId':
                                        print("ID ALINAMADI QUERY GIRILIYOR:" + str(sarki))
                                        videoId = sarki
                                except Exception as e:
                                    print(e)
                                    print("HATA: ID ALINAMADI QUERY GIRILIYOR:" + str(sarki))
                                    videoId = sarki
                                
                                ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'outtmpl': '%(id)s.%(ext)s', 'default_search': 'auto', 'allowplaylist' : False, 'noplaylist' : True,})
                                with ydl:
                                    result = ydl.extract_info(
                                        #sarki.replace(":", " "),
                                        videoId,
                                        download=False,

                                    )
                                
                                if 'entries' in result:
                                    video = result['entries'][0]
                                else:

                                    video = result
                                pp = pprint.PrettyPrinter(indent=1)
                                pp.pprint(video["formats"])

                                ses_kalite_secimi = {}
                                seskaliteler = []
                                boyutliste = []
                                for kalite in video["formats"]:
                                    if not "audio only" in kalite["format"] or not kalite["format_id"] == "140":
                                        pass
                                    else:
                                        try:
                                            ses_blg = str(kalite["filesize"]) + " byte"
                                        except:
                                            ses_blg = "Bilinmiyor."
                                        print("Ses Kalitesi: " + kalite["format_id"] + " " + kalite["format"] + " " + kalite["ext"] + " " + ses_blg)
                                        seskaliteler.append(kalite["format_id"])
                                        ses_kalite_secimi[str(kalite["filesize"])] = str(kalite["format_id"])
                                        try:
                                            boyutliste.append(kalite["filesize"])
                                        except:
                                            pass
                                        
                                sesklt = str(ses_kalite_secimi[str(max(boyutliste))])
                                
                                def prgsbaslat():
                                    print(seskaliteler)
                                    print(boyutliste)
                                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                                    boyut = max(boyutliste)
                                    print(boyut)

                                    yt_boyut = boyut
                                    tamamlanmadı = True
                                    prgs.stop()
                                    prgs.config(mode="determinate")
                                    while tamamlanmadı:
                                        if not "bitti" in bittibitmedi:
                                            onb_klasör = os.listdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}")

                                            gecerliboyut = 0
                                            for onb in onb_klasör:
                                            
                                                sarkitemz = dirtemizle(sarki)
                                                if sarkitemz in onb:
                                                    try:
                                                        onb_dosya = f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{dirtemizle(onb)}"
                                                        boyut = os.path.getsize(onb_dosya)
                                                        #print(onb)
                                                        gecerliboyut += boyut
                                                    except Exception as e:
                                                        print(e)
                                                        pass
                                                else:
                                                    pass
                                                
                                            yüzdee = 100 * float(gecerliboyut)/float(yt_boyut)

                                            if yüzdee > 99:
                                                print("\nYükleme Barı Doldu.")
                                                prgs['value'] = 100
                                                gecerliyazi.config(text=f"{sarki.replace(' (audio)', '')} .mp3'e Çeviriliyor...")  
                                                prgs.config(mode="indeterminate")
                                                prgs.start(7)
                                                tamamlanmadı = False 
                                                break
                                            else:
                                                prgs['value'] = yüzdee

                                                gecerliyazi.config(text=f"{sarki.replace(' (audio)', '')} %{round(yüzdee, 2)} ({round(float(yt_boyut)/1048576, 2)} MB/{round(float(gecerliboyut)/1048576, 2)} MB)")   
                                            time.sleep(0.01)
                                        else:
                                            print("\nYükleme Barı Doldu.")
                                            prgs['value'] = 100
                                            gecerliyazi.config(text=f"{sarki.replace(' (audio)', '')} .mp3'e Çeviriliyor...")  
                                            prgs.config(mode="indeterminate")
                                            prgs.start(7)
                                            break
                            
                                prgsthread = threading.Thread(target=prgsbaslat)
                                prgsthread.start()
                                print(f"Temizlenmiş : '{sarki}'")
                                ydl_opts1 = {
                                        'format': f'{sesklt}',
                                        'default_search': 'auto',
                                        'allowplaylist' : False,
                                        'noplaylist' : True,
                                        'cachedir': False,
                                        'outtmpl': spt_yolu,
                                        'postprocessors': [{
                                            'key': 'FFmpegExtractAudio',
                                            'preferredcodec': 'mp3',
                                            'preferredquality': "320",
                                        }],
                                    }
                                with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
                                    print("Ses indiriliyor, Lütfen bekleyin...")
                                    #ydl.download([sarki.replace(":", " ")])
                                    ydl.download([videoId])
                                    

                            
                            indirildi += 1
                            tamamlanmadı = False
                            bittibitmedi.append("bitti")
                            gecerliyazi.config(text=f"{sarki.replace(' (audio)', '')} Metadata Yazılıyor...")
                            if mod == "Albüm":
                                print("Albüm Metadata Yazılıyor.....")
                                
                                thumbsarkipath = f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{dirtemizle(sarki.replace(' (audio)', ''))}.mp3"
                                print(thumbsarkipath)

                                audiofile = eyed3.load(thumbsarkipath)
                                
                                if (audiofile.tag == None):
                                    audiofile.initTag()
                            
                                audiofile.tag.title = sarki.replace(' (audio)', '').replace(" - " + yapan, "")
                                audiofile.tag.album = isim
                                audiofile.tag.artist = yapan
                                audiofile.tag.publisher = "AcemTube"
                                audiofile.tag.track_num = indirildi
                                audiofile.tag.images.set(3, thumbdir, 'image/jpeg')
                                audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
                            else:
                                if not mod == "Liste":
                                    thumbnail = coverlist[sarki]

                                    updget = requests.get(thumbnail)


                                    for chunk in updget.iter_content(chunk_size=chunkboyut):
                                        if chunk:
                                            thumbdi = chunk
                                
                                thumbsarkipath = f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{dirtemizle(sarki.replace(' (audio)', ''))}.mp3"
                                print(thumbsarkipath)

                                audiofile = eyed3.load(thumbsarkipath)
                                
                                if (audiofile.tag == None):
                                    audiofile.initTag()
                            
                                audiofile.tag.title = sarki.replace(' (audio)', '').replace(" - "+ sanatcisim[sarki], "")
                                audiofile.tag.album = albumlist[sarki]
                                audiofile.tag.artist = sanatcisim[sarki]
                                audiofile.tag.publisher = "AcemTube"
                                audiofile.tag.track_num = indirildi
                                audiofile.tag.images.set(3, thumbdi, 'image/jpeg')
                                audiofile.tag.save(version=eyed3.id3.ID3_V2_3)
                               
                            gecerliyazi.config(text=f"{sarki.replace(' (audio)', '')} Başarıyla İndirildi!")  
                        except Exception as e:
                            print(e)
                        yuzdeee += eklenecek
                        indyazi.config(text=f"İlerleme: %{round(yuzdeee, 2)} ({listesayi} Parça içinden {indirildi} Parça)")
                        bar += eklenecek
                        prgs.stop()
                        if not f"{dirtemizle(sarki)}.mp3" in geçilecek:
                            prekapakk.config(image=prekapakb)
                            prgs.config(mode="determinate")
                            prgs['value'] = 0
                            time.sleep(0.4)
                            prgs['value'] = bar
                            time.sleep(0.4)
                            prgs['value'] = 0
                            time.sleep(0.4)
                            prgs['value'] = bar
                            time.sleep(0.4)
                            prgs['value'] = 0
                            time.sleep(0.3)
                        prgs.config(mode="indeterminate")
                        prgs.start(7)

                    print(f"{isim} Adlı {mod} indirildi!")

                    ibaslik.destroy()
                    prgs.destroy()
                    gecerliyazi.destroy()
                    indyazi.destroy()
                    prekapakk.config(image=prekapakb)
                    pygame.mixer.Sound.play(tik)
                    yolyazi.config(text=f"Kaydedilen Yol: {get_yol()}/Spotify/{yapan}/{isim}")
                    iyazi.destroy()
                    tbaslik = tk.Label(baslikutu, text=f"Tamamlandı!", bg=acikyesil, fg=baslikyazirengi)
                    tbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    yazidahayeni = tk.Label(baslikutu1, text=f"{isim} Adlı {mod} .mp3 Formatı İle Başarıyla Kaydedildi!", bg=arkaplan, fg=yazirengi)
                    yazidahayeni.config(font=("Montserrat Medium", "12"))
                    yazidahayeni.place(relwidth=1, relheight=0.1, rely=0.1)
                    tbaslik.place(relwidth=1, relheight=1)
                    anamenu.config(state=NORMAL)
                    cikıs.config(state=NORMAL)
                    if root.state() != NORMAL:
                        try:
                            tost.show_toast("Tamamlandı!",f"{isim} Adlı {mod} .mp3 Formatı İle Başarıyla Kaydedildi!", threaded=True, icon_path=r"./acemtube.ico")
                        except:
                            print("windows 10 değil")
                    try:
                        RPC.update(details="Spotify İndiriyor", state=f"{isim} Adlı {mod} İndirildi.", start=zmn, large_image="acemtubedc", small_image="spotify", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                    except:
                        print("dc yürümüyor.")

                    listel = os.listdir(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}")
                    
                    def dk():
                            pygame.mixer.Sound.play(click)
                            os.startfile(f'{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}')
                            #subprocess.Popen(f'explorer /select "{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{random.choice(listel)}"')
                    def oy():
                        pygame.mixer.Sound.play(click)
                        os.startfile(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{random.choice(listel)}")

                    oyn = tk.Button(baslikutu1, text=" Oynat ", padx=30, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=oy)
                    oyn.place(rely=0.5, relx= 0.55)
                    dosk = tk.Button(baslikutu1, text=" Klasörde Göster ", padx=5, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dk)
                    dosk.place(rely=0.5, relx= 0.3)

                    if prekapak != None:
                        prekapakk.pack(pady=20)
                        yazidahayeni.place(relwidth=1, relheight=0.05, rely=0.44)
                        yolyazi.place(relwidth=1, relheight=0.05, rely=0.5)
                        oyn.place(rely=0.6, relx= 0.55)
                        dosk.place(rely=0.6, relx= 0.3)

                    time.sleep(1)
                    def get_oto():
                        with open('data.json', 'r') as f:
                            yol = json.load(f)
                        if "oto_play" in yol:
                            return yol["oto_play"]
                        else:
                            return 0
                    if get_oto() == 1:
                        os.startfile(os.startfile(f"{get_yol()}/Spotify/{dirtemizle(yapan)}/{dirtemizle(isim)}/{random.choice(listel)}"))

                print("spotify devamkeeee")
                try:
                    RPC.update(details="Spotify İndiriyor", state=f"Link İşleniyor...", start=zmn, large_image="acemtubedc", small_image="spotify", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("dc yürümüyor.")
                url = giris.get()
                likbaslik.destroy()
                yakyazi.destroy()
                giris.destroy()
                devamke.destroy()
                arabaslik = tk.Label(baslikutu, text=f"Link İşleniyor...", bg=acikyesil, fg=baslikyazirengi)
                arabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                arabaslik.place(relwidth=1, relheight=1)
                arayazi = tk.Label(baslikutu1, text=f"Verilen Link İşleniyor. Lütfen Bekleyin.", bg=arkaplan, fg=yazirengi)
                arayazi.config(font=("Montserrat Medium", "12"))
                arayazi.place(relwidth=1, relheight=0.1, rely=0.03)
                muzikres["muzikres"] = 1
                s = ttk.Style()
                s.theme_use("clam")
                s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi2, troughcolor=koyugri, bordercolor=cubukrengi2, darkcolor=cubukrengi2, lightcolor=cubukrengi2)
                prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="indeterminate")
                prgs.place(relx=0.265, rely=0.15)
                prgs.start(7)

                print("Spotify deneniyor...")
                try:
                    print(url)
                    coverlist = {}
                    sanatcisim = {}
                    albumlist = {}
                    prekapak = None
                    if "/playlist/" in url:
                        try:
                            isim = sty.getIsim(str(url).split("https://open.spotify.com/playlist/")[-1])["name"]
                            print("1")
                            yapan = sty.getIsim(str(url).split("https://open.spotify.com/playlist/")[-1])["owner"]["display_name"]
                            sarkisayisi = sty.getIsim(str(url).split("https://open.spotify.com/playlist/")[-1])["tracks"]["total"]
                            sarkilar = sty.getIsim(str(url).split("https://open.spotify.com/playlist/")[-1])["tracks"]
                        except:
                            isim = sty.getIsim(str(url))["name"]
                            print("2")
                            yapan = sty.getIsim(str(url))["owner"]["display_name"]
                            sarkisayisi = sty.getIsim(str(url))["tracks"]["total"]
                            sarkilar = sty.getIsim(str(url))["tracks"]
                        try:
                            try:
                                prekapak = sty.getIsim(str(url).split("https://open.spotify.com/playlist/")[-1])['images'][0]['url']
                            except:
                                prekapak = sty.getIsim(str(url))['images'][0]['url']
                            print("Playlist Kapak Url: " + str(prekapak))
                        except:
                            print("Playlist Kapak Url Alınamadı. ")
                            prekapak = None
                        
                        spoti = sty.spver()
                        tumparcalar = sarkilar['items']
                        while sarkilar['next']:
                            try:
                                sarkilar = spoti.next(sarkilar)
                                tumparcalar.extend(sarkilar['items'])
                            except Exception as e:
                                print("Genişletme hatası: " + str(e))
                        eklenecek = []
                        for sarki in tumparcalar:
                            try:
                                sanatciarama = []
                                for sanatciadi in sarki["track"]["artists"]:

                                    sanatciarama.append(sanatciadi["name"])

                                sanatcilar = ", ".join(sanatciarama)

                                eklenecek.append(sarki["track"]["name"] + " - " + sanatcilar)
                                coverlist[sarki["track"]["name"] + " - " + sanatcilar] = sarki["track"]["album"]['images'][0]['url']
                                albumlist[sarki["track"]["name"] + " - " + sanatcilar] = sarki["track"]["album"]["name"]
                                sanatcisim[sarki["track"]["name"] + " - " + sanatcilar] = sanatcilar
                            except Exception as e:
                                print("Ekleme hatası: " + str(e))


                        print(sanatcisim)
                        sarkisayisi = len(eklenecek)
                        baslik_listesi = eklenecek
                        print(sarkisayisi)
                        #pp = pprint.PrettyPrinter(indent=1)
                        #pp.pprint(sayi)

                        print(yapan)
                        #baslik_listesi = sty.getTracks(str(url).split("https://open.spotify.com/playlist/")[-1], sarkisayisi=sarkisayisi)
                        mod = "Liste"
                    elif "/album/" in url:
                        try:
                            thumbnail = sty.getAlbüm(str(url).split("https://open.spotify.com/album/")[-1])['images'][0]["url"]
                            print("1")
                        except:
                            thumbnail = sty.getAlbüm(str(url))['images'][0]["url"]
                            print("2")
                        print(thumbnail)

                        updget = requests.get(thumbnail)
                          
                        for chunk in updget.iter_content(chunk_size=chunkboyut):
                            if chunk:
                                thumbdir = chunk
                        try:
                            isim = sty.getAlbüm(str(url).split("https://open.spotify.com/album/")[-1])["name"]
                            yapan = sty.getAlbüm(str(url).split("https://open.spotify.com/album/")[-1])["artists"]
                            sarkilar = sty.getAlbüm(str(url).split("https://open.spotify.com/album/")[-1])["tracks"]
                        except:
                            isim = sty.getAlbüm(str(url))["name"]
                            yapan = sty.getAlbüm(str(url))["artists"]
                            sarkilar = sty.getAlbüm(str(url))["tracks"]

                        sanatciarama = []
                        for sanatciadi in yapan:
                            sanatciarama.append(sanatciadi["name"])
                        sanatcilar = ", ".join(sanatciarama)
                        #url = sty.getTracks(str(url).split("https://open.spotify.com/album/")[-1])

                        eklenecek = []
                        for sarki in sarkilar["items"]:
                            eklenecek.append(sarki["name"] + " - " + sanatcilar)
 
                        sarkisayisi = len(eklenecek)
                        baslik_listesi = eklenecek
                        yapan = sanatcilar
                        prekapak = thumbnail
                        mod = "Albüm"
                    elif "/track/" in url:
                        try:
                            sanatci = sty.getSarki(str(url).split("https://open.spotify.com/track/")[-1])["artists"]
                            print("1")
                        except:
                            sanatci = sty.getSarki(str(url))["artists"]
                            print("2")
                        sanatciarama = []
                        for sanatciadi in sanatci:
                            sanatciarama.append(sanatciadi["name"])
                        sanatcilar = ", ".join(sanatciarama)
                        try:
                            isim =  sty.getSarki(str(url).split("https://open.spotify.com/track/")[-1])["name"]
                        except:
                            isim =  sty.getSarki(str(url))["name"]
                        #yapan = sty.getSarki(str(url).split("https://open.spotify.com/track/")[-1])["owner"]["display_name"]
                        try:
                            url = sty.getSarki(str(url).split("https://open.spotify.com/track/")[-1])
                        except:
                            url = sty.getSarki(str(url))
                        yapan = sanatcilar
                        sarkisayisi = 1
                        
                        
                        aratilcak = isim + " - " + sanatcilar 
                        baslik_listesi = []
                        baslik_listesi.append(aratilcak)
                        coverlist[aratilcak] = url["album"]['images'][0]['url']
                        albumlist[aratilcak] = url["album"]["name"]
                        prekapak = url["album"]['images'][0]['url']
                        sanatcisim[aratilcak] = sanatcilar

                        mod = "Şarkı"

                    if prekapak != None:

                        prekapakd = requests.get(prekapak)

                        for chunk in prekapakd.iter_content(chunk_size=chunkboyut):
                            if chunk:
                                prekapakurld = chunk

                        prekapakc = Image.open(BytesIO(prekapakurld))
                       
                        prekapakres = prekapakc.resize((170,170), Image.Resampling.LANCZOS)
                        global prekapakb
                        prekapakb = ImageTk.PhotoImage(prekapakres)
                        
                    print(baslik_listesi)
                    listesayi = len(baslik_listesi)

                    arabaslik.destroy()
                    arayazi.destroy()
                    anamenu.config(state=NORMAL)
                    cikıs.config(state=NORMAL)
                    try:
                        RPC.update(details="Spotify İndiriyor", state=f"Bulundu!", start=zmn, large_image="acemtubedc", small_image="spotify", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                    except:
                        print("dc yürümüyor.")
                    lbaslik = tk.Label(baslikutu, text=f"{mod} Bulundu!", bg=acikyesil, fg=baslikyazirengi)
                    lbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    lbaslik.place(relwidth=1, relheight=1)
                    lyazi = tk.Label(baslikutu1, text=f"{isim} Adlı {mod}de {listesayi} Adet Şarkı Bulundu!", bg=arkaplan, fg=yazirengi)
                    if mod == "Şarkı":
                        lyazi.config(text=f"{isim} Adlı {mod} Bulundu!")
                    prgs.destroy()
                    lyazi.config(font=("Montserrat Medium", "12"))
                    lyazi.place(relwidth=1, relheight=0.1, rely=0.03)
                    shpyazi = tk.Label(baslikutu1, text=f"Yapan: {yapan}", bg=arkaplan, fg=yazirengi)
                    shpyazi.config(font=("Montserrat Medium", "10"))
                    shpyazi.place(relwidth=1, relheight=0.1, rely=0.15)
                    

                    devamkee = tk.Button(baslikutu1, text=" İndir ", padx=15, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=indir).start)
                    devamkee.place(rely=0.3, relx= 0.45)

                    if prekapak != None:
                        prekapakk = tk.Label(baslikutu1, image=prekapakb, bg=arkaplan ,fg=acikgri2)
                        prekapakk.image = prekapakb
                        prekapakk.pack(pady=20)
                        lyazi.place(relwidth=1, relheight=0.1, rely=0.42)
                        shpyazi.place(relwidth=1, relheight=0.05, rely=0.5)
                        devamkee.pack(pady=47)

                    def devambas(bob=None):
                        try:
                            devamkee.invoke()
                        except:
                            root.unbind('<Return>')
        
                    root.bind('<Return>', devambas)
                    if cevap == "7" or "[7]-" in cevap:
                        if mod == "Albüm" or mod == "Liste":
                            premyazi = tk.Label(baslikutu1, text=f"{mod} İndirebilmek İçin AcemTube Premium'a İhtiyacınız Var.", bg=arkaplan, fg=kirmiziyazi)
                            premyazi.config(font=("Montserrat Medium", "12"))
                            premyazi.place(relwidth=1, relheight=0.1, rely=0.5)
                            devamkee.config(state=DISABLED)
                            pygame.mixer.Sound.play(hata)
                            
                    
                    if root.state() != NORMAL:
                        try:
                            tost.show_toast(f"{mod} Bulundu!", f"{isim} Adlı {mod}de {listesayi} Adet Şarkı Bulundu! Lütfen İndirmeyi Başlatmak İçin Programa Dönünüz.", threaded=True, icon_path=r"./acemtube.ico")
                        except:
                            print("windows 10 değil")

                except Exception as e:
                    pygame.mixer.Sound.play(hata1)
                    print("hata" + str(e))
                    hatakodu = e
                    prgs.destroy()
                    arayazi.destroy()
                    hatabaslik = tk.Label(baslikutu, text=f"Hata!", bg=kirmizi, fg=baslikyazirengi)
                    hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    hatabaslik.place(relwidth=1, relheight=1)
                    hatayaziyeni = tk.Label(baslikutu1, text=f"Bir hata oluştu. Link Geçersiz Veya Gizli Olabilir.", bg=arkaplan, fg=yazirengi)
                    hatayaziyeni.config(font=("Montserrat Medium", "11"))
                    hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)
                    anamenu.config(state=NORMAL)
                    cikıs.config(state=NORMAL)
                    def bildir():
                        pygame.mixer.Sound.play(click)
                        hatanumara = random.randint(0, 1000000000000)
                        def kld_get():
                            with open('data.json', 'r') as f:
                                klad = json.load(f)
                            if "kullanici_adi" in klad:
                                return klad["kullanici_adi"]
                            else:
                                try:
                                   RPC.close()
                                except:
                                    print("discord yürütülmeimş")
                                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                                root.destroy()
                                exit(0)

                        print(f"Hata {hatakodu} Bildiriliyor...")
                        bildir.config(state=DISABLED)
                        try:
                            async def hello():
                                uri = server
                                async with websockets.connect(uri) as websocket:
                                    hwidstr = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                                    istek = f"hatabildir-'{kld_get()}' '{datetime.datetime.utcnow() + datetime.timedelta(hours=3)}' 'act{hatanumara}' '{platform.platform()}' '{version}' '{hatakodu}' 'Spotify' '{hwidstr}'"
                                    print(f"{istek} İsteği Gönderiliyor")
                                    await websocket.send(istek)
                            asyncio.get_event_loop().run_until_complete(hello())
                        except:
                            pass
                        pygame.mixer.Sound.play(tik)
                        bas1yazi = tk.Label(baslikutu1, text=f"Hata Başarı İle Bildirildi. act{hatanumara} Destek Numaranız İle İletişime Geçebilirsiniz. ", bg=acikyesil, fg=yazirengi)
                        bas1yazi.config(font=("Montserrat Medium", "10"))
                        bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    bildir = tk.Button(baslikutu1, text=" Hata Bildir ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=bildir)
                    bildir.place(rely=0.35, relx= 0.44)
                    if url == "":
                        hatayaziyeni.config(text=f"Link Girilmedi.")
                        bildir.config(state=DISABLED)
                    
                    if root.state() != NORMAL:
                        try:
                            tost.show_toast("Hata!",f"Bir hata oluştu. Link Geçersiz Veya Gizli Olabilir.", threaded=True, icon_path=r"./acemtubered.ico")
                        except:
                            print("windows 10 değil")
            else:
                pygame.mixer.Sound.play(hata1)
                yakyazi.destroy()
                likbaslik.destroy()
                devamke.destroy()
                hatabaslik = tk.Label(baslikutu, text=f"Hata!", bg=kirmizi, fg=baslikyazirengi)
                hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                hatabaslik.place(relwidth=1, relheight=1)
                hatayaziyeni = tk.Label(baslikutu1, text=f"Ses/Video Kayıt Etme Yolu Belirtilmedi. Lütfen Ayarlar Menüsünden Ayarlayınız.", bg=arkaplan, fg=yazirengi)
                hatayaziyeni.config(font=("Montserrat Medium", "11"))
                hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.1)
                anamenu.config(state=NORMAL)
                cikıs.config(state=NORMAL)
                if root.state() != NORMAL:
                    try:
                        tost.show_toast("Hata!",f"Ses/Video Kayıt Etme Yolu Belirtilmedi. Lütfen Ayarlar Menüsünden Ayarlayınız.", threaded=True, icon_path=r"./acemtubered.ico")
                    except:
                        print("windows 10 değil")

        giris= tk.Entry(baslikutu1, width=105, bg=aramarengi, borderwidth=kenargenisligi, relief=stil, fg=yazirengi)
        giris.place(rely=0.15, relx=0.07)
        
        devamke = tk.Button(baslikutu1, text=" Devam ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=basla).start)
        devamke.place(rely=0.25, relx= 0.45)
        def girisiac():
            try:
                if not giris.get().strip(" ") == "" and "spotify.com" in giris.get():
                    devamke.config(state=NORMAL)
                else:
                    devamke.config(state=DISABLED)
            except Exception as e:
                print(e)
            devamke.after(10, girisiac)
        girisiac()

        def devambas(bob=None):
            try:
                devamke.invoke()
            except:
                root.unbind('<Return>')
    
        root.bind('<Return>', devambas)

        def cikis():
            pygame.mixer.Sound.play(click)
            pygame.mixer.Sound.play(hata)
            root.attributes('-disabled', True)
            
            def anan():
                print("anan")
                
            print("kapatıldım aq")
            kpw = tk.Tk()
            kpw.title("Emin Misiniz?")
            kpw.resizable(False, False)
            kpw.iconbitmap("acemtubered.ico")
            kpw.protocol("WM_DELETE_WINDOW", anan)
            yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
            yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
            kpw.geometry(f"400x150+{yer2}+{yer3}")
            kpw.attributes("-alpha", seffaflik)
            canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
            canvas.pack()
            emnk = tk.Frame(kpw, bg=arkaplan)
            emnk1 = tk.Frame(kpw, bg=arkaplan)
            emnk.place(relwidth=1, relheight=0.7, rely=0.3)
            emnk1.place(relwidth=1, relheight=0.3)
            emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
            emnb.config(font=("Montserrat ExtraBold", "30", "italic"))
    
            emnb.place(relwidth=1, relheight=0.9)
            
            ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=arkaplan, fg=yazirengi)
            ckyazi.config(font=("Montserrat Medium", "9"))
            ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
            def cikiss():
                pygame.mixer.Sound.play(click)
                try:
                   RPC.close()
                except:
                    print("discord yürütülmeimş")
                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                root.destroy()
                kpw.destroy()
                exit(0)
            def gri():
                pygame.mixer.Sound.play(click)
                root.attributes('-disabled', False)
                kpw.destroy()
    
            cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
            cikıss.place(rely=0.5, relx= 0.25)
            anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
            anamenuu.place(rely=0.5, relx= 0.57)
            kpw.mainloop()

        def anamenu():
            pygame.mixer.Sound.play(click)
            print("anamenu basıldı")
            baslikutu.destroy()
            baslikutu1.destroy()
            ilkbaslangic(anamenu=1)
        
        cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
        cikıs.place(rely=0.87, relx= 0.89)
        anamenu = tk.Button(baslikutu1, text=" Ana Menü ", padx=0, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=anamenu)
        anamenu.place(rely=0.8, relx= 0.89)

        cıkıs.destroy()

    def ayarlar():
        try:
            RPC.update(details="Ayarlarla Oynuyor", start=zmn, large_image="acemtubedc", small_image="ayar", small_text="By: Acem#8887", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
        except:
            print("dc yürümüyor.")
        pygame.mixer.Sound.play(click)
        try:
            verkutu.destroy()
        except:
            print("sürüm ok.")
        print("ayarlar basıldı")
        baslik.destroy()
        ses.destroy()
        video.destroy()
        spotify.destroy()
        ayarlar.destroy()
        hkd.destroy()
        cıkıs.destroy()
        ayarbaslik = tk.Label(baslikutu, text=f"Ayarlar", bg=acikmavi, fg=baslikyazirengi)
        ayarbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
        ayarbaslik.place(relwidth=1, relheight=1)
        def cikis():
            pygame.mixer.Sound.play(click)
            pygame.mixer.Sound.play(hata)
            root.attributes('-disabled', True)
            
            def anan():
                print("anan")
            print("kapatıldım aq")
            kpw = tk.Tk()
            kpw.title("Emin Misiniz?")
            kpw.resizable(False, False)
            kpw.iconbitmap("acemtubered.ico")
            kpw.protocol("WM_DELETE_WINDOW", anan)
            yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
            yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
            kpw.geometry(f"400x150+{yer2}+{yer3}")
            kpw.attributes("-alpha", seffaflik)
            canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
            canvas.pack()
            emnk = tk.Frame(kpw, bg=arkaplan)
            emnk1 = tk.Frame(kpw, bg=arkaplan)
            emnk.place(relwidth=1, relheight=0.7, rely=0.3)
            emnk1.place(relwidth=1, relheight=0.3)
            emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
            emnb.config(font=("Montserrat ExtraBold", "30", "italic"))
    
            emnb.place(relwidth=1, relheight=0.9)
            
            ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=arkaplan, fg=yazirengi)
            ckyazi.config(font=("Montserrat Medium", "9"))
            ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
            def cikiss():
                pygame.mixer.Sound.play(click)
                try:
                   RPC.close()
                except:
                    print("discord yürütülmeimş")
                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                root.destroy()
                kpw.destroy()
                exit(0)
            def gri():
                pygame.mixer.Sound.play(click)
                root.attributes('-disabled', False)
                kpw.destroy()
    
            cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
            cikıss.place(rely=0.5, relx= 0.25)
            anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
            anamenuu.place(rely=0.5, relx= 0.57)
            kpw.mainloop()

        def anamenu():
            pygame.mixer.Sound.play(click)
            print("anamenu basıldı")
            baslikutu.destroy()
            baslikutu1.destroy()
            ilkbaslangic(anamenu=1)

        def kurulum():

            pygame.mixer.Sound.play(click)
            print("kurulum basıldı.")
            ayarbaslik.destroy()
            kurulm.destroy()
            ob.destroy()
            dc.destroy()
            kaydetme.destroy()
            dil.destroy()
            bok.destroy()
            kurbaslik = tk.Label(baslikutu, text=f"Kurulum", bg=acikmavi, fg=baslikyazirengi)
            kurbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            kurbaslik.place(relwidth=1, relheight=0.9)
            kuryazi = tk.Label(baslikutu1, text=f"Eğer İndirmeler İle İlgili Problem Yaşıyorsanız Yeniden Kurulum Yapabilirsiniz.", bg=arkaplan, fg=yazirengi)
            kuryazi.config(font=("Montserrat Medium", "12"))
            kuryazi.place(relwidth=1, relheight=0.1, rely=0.1)
            def devamke():
                pygame.mixer.Sound.play(click)
                subprocess.call("scoop uninstall ffmpeg", shell=True)
                subprocess.call("scoop cache rm ffmpeg", shell=True)
                subprocess.call(f"rmdir /Q /S {os.path.expanduser('~')}\scoop\\", shell=True)
                with open('data.json', 'r') as f:
                    clc = json.load(f)
                clc[str(f"krlm_chk")] = 0
                with open('data.json', 'w') as f:
                    json.dump(clc, f, indent=4)
                
                try:
                    os.startfile("acemtube.exe")
                except:
                    try:
                        os.startfile("acemtube.py")
                    except:
                        print("dosya yok")
                try:
                   RPC.close()
                except:
                    print("discord yürütülmeimş")
                
                root.destroy()
                exit(0)

            devam = tk.Button(baslikutu1, text=" Başla! ", padx=45, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=devamke)
            devam.place(rely=0.3, relx= 0.412)
            #kisi = tk.Button(baslikutu1, text=" Kurulumu Özelleştir ", padx=15, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, state=DISABLED, command=kisiles)
            #kisi.place(rely=0.3, relx= 0.6)

        def obt():
            try:
                RPC.update(details="Ayarlarla Oynuyor", state="Diğer Ayarlar", start=zmn, large_image="acemtubedc", small_image="ayar", small_text="By: Acem#8887", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
            except:
                print("dc yürümüyor.")
            pygame.mixer.Sound.play(click)
            ayarbaslik.destroy()
            kurulm.destroy()
            ob.destroy()
            dc.destroy()
            kaydetme.destroy()
            dil.destroy()
            bok.destroy()
            def get_secim(s="sfx"):
                with open('data.json', 'r') as f:
                    yol = json.load(f)
                if s in yol:
                    return yol[s]
                else:
                    return 1

            def get_oto():
                with open('data.json', 'r') as f:
                    yol = json.load(f)
                if "oto_play" in yol:
                    return yol["oto_play"]
                else:
                    return 0

            def ybbb():
                pygame.mixer.Sound.play(click)
                try:
                    os.startfile("acemtube.exe")
                    try:
                        RPC.close()
                    except:
                        print("discord yürütülmeimş")
                    
                    root.destroy()
                    exit(0)
                except:
                    try:
                        os.startfile("acemtube.py")
                        try:
                           RPC.close()
                        except:
                            print("discord yürütülmeimş")

                        root.destroy()
                        exit(0)
                    except:
                        print("dosya yok")
                        
                
            def seccc():
                    pygame.mixer.Sound.play(click)
                    with open('data.json', 'r') as f:
                        clc = json.load(f)
                    clc[str(f"sfx")] = cbv.get()
                    with open('data.json', 'w') as f:
                        json.dump(clc, f, indent=4)
                    bas1yazi = tk.Label(baslikutu1, text=f"NOT: Değişikliklerin Etki Etmesi İçin Programın Yeniden Başlatılması Gerekir.", bg=kirmizi, fg=yazirengi)
                    bas1yazi.config(font=("Montserrat Medium", "10"))
                    bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    yb = tk.Button(baslikutu1, text=" Yeniden Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybbb)
                    yb.place(rely=0.65, relx= 0.42)
                    if cbv.get() != 0:
                        uc.config(state=NORMAL)
                        ac.config(state=NORMAL)
                        tık.config(state=NORMAL)
                    else:
                        uc.config(state=DISABLED)
                        ac.config(state=DISABLED)
                        tık.config(state=DISABLED)

            def tsec():
                    pygame.mixer.Sound.play(click)
                    with open('data.json', 'r') as f:
                        clc = json.load(f)
                    clc[str(f"tfx")] = tıkv.get()
                    with open('data.json', 'w') as f:
                        json.dump(clc, f, indent=4)
                    bas1yazi = tk.Label(baslikutu1, text=f"NOT: Değişikliklerin Etki Etmesi İçin Programın Yeniden Başlatılması Gerekir.", bg=kirmizi, fg=yazirengi)
                    bas1yazi.config(font=("Montserrat Medium", "10"))
                    bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    yb = tk.Button(baslikutu1, text=" Yeniden Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybbb)
                    yb.place(rely=0.65, relx= 0.42)

            def asec():
                    pygame.mixer.Sound.play(click)
                    with open('data.json', 'r') as f:
                        clc = json.load(f)
                    clc[str(f"afx")] = acv.get()
                    with open('data.json', 'w') as f:
                        json.dump(clc, f, indent=4)
                    bas1yazi = tk.Label(baslikutu1, text=f"NOT: Değişikliklerin Etki Etmesi İçin Programın Yeniden Başlatılması Gerekir.", bg=kirmizi, fg=yazirengi)
                    bas1yazi.config(font=("Montserrat Medium", "10"))
                    bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    yb = tk.Button(baslikutu1, text=" Yeniden Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybbb)
                    yb.place(rely=0.65, relx= 0.42)

            def usec():
                    pygame.mixer.Sound.play(click)
                    with open('data.json', 'r') as f:
                        clc = json.load(f)
                    clc[str(f"ufx")] = ucv.get()
                    with open('data.json', 'w') as f:
                        json.dump(clc, f, indent=4)
                    bas1yazi = tk.Label(baslikutu1, text=f"NOT: Değişikliklerin Etki Etmesi İçin Programın Yeniden Başlatılması Gerekir.", bg=kirmizi, fg=yazirengi)
                    bas1yazi.config(font=("Montserrat Medium", "10"))
                    bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    yb = tk.Button(baslikutu1, text=" Yeniden Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybbb)
                    yb.place(rely=0.65, relx= 0.42)

            def oseccc():
                    pygame.mixer.Sound.play(click)
                    with open('data.json', 'r') as f:
                        clc = json.load(f)
                    clc[str(f"oto_play")] = otov.get()
                    with open('data.json', 'w') as f:
                        json.dump(clc, f, indent=4)
                    
            dahayenibaslik = tk.Label(baslikutu, text=f"Diğer Ayarlar", bg=acikmavi, fg=baslikyazirengi)
            dahayenibaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            dahayenibaslik.place(relwidth=1, relheight=1)

            tıkv = tk.IntVar()
            tık = tk.Checkbutton(baslikutu1, text="Tıklama Sesi", pady=15, padx=13, bg=acikmavi, variable=tıkv, command=tsec)
            tık.place(rely=0.1, relx= 0.42)

            acv = tk.IntVar()
            ac = tk.Checkbutton(baslikutu1, text="Açılış Sesi", pady=15, padx=19, bg=acikmavi, variable=acv, command=asec)
            ac.place(rely=0.1, relx= 0.77)

            ucv = tk.IntVar()
            uc = tk.Checkbutton(baslikutu1, text="Uyarı Sesleri", pady=15, padx=15, bg=acikmavi, variable=ucv, command=usec)
            uc.place(rely=0.3, relx= 0.1)

            cbv = tk.IntVar()
            cb = tk.Checkbutton(baslikutu1, text="Ses Efektleri", pady=15, padx=15, bg=acikmavi, variable=cbv, command=seccc)
            cb.place(rely=0.1, relx= 0.1)

    
            otov = tk.IntVar()
            oto = tk.Checkbutton(baslikutu1, text="Oto Oynatma", pady=15, padx=10, bg=acikmavi, variable=otov, command=oseccc)
            oto.place(rely=0.3, relx= 0.42)
            print(oto.keys())
            if get_secim() != 0:
                cb.select()
            else:
                uc.config(state=DISABLED)
                ac.config(state=DISABLED)
                tık.config(state=DISABLED)
            
            if get_secim("afx") != 0:
                ac.select()

            if get_secim("ufx") != 0:
                uc.select()

            if get_secim("tfx") != 0:
                tık.select()

            if get_oto() != 0:
                oto.select()

            global ob_konsol
            ob_konsol = 0

            def obttt():
                pygame.mixer.Sound.play(click)

                try:
                    shutil.rmtree("./Videolar")
                    os.mkdir("./Videolar")
                    print("önb temizlendi")
                    pygame.mixer.Sound.play(tik)
                    obtt.configure(bg=acikyesil, fg=yazirengi, text="Önbellek Silindi!")
                    obtt.place(rely=0.3, relx=0.75)
                except:
                    print("önb temizlenemedi")
                    try:
                        pygame.mixer.Sound.play(tik)
                        os.mkdir("./Videolar")
                        pygame.mixer.Sound.play(tik)
                        obtt.configure(bg=acikyesil, fg=yazirengi, text="Önbellek Silindi!")
                        obtt.place(rely=0.3, relx=0.75)
                    except:
                        pygame.mixer.Sound.play(hata1)
                        obtt.configure(bg=kirmizi, fg=yazirengi, text="Önbellek Silinemedi!")
                        obtt.place(rely=0.3, relx=0.74)
                try:
                    for dosya in os.listdir(r"./"):
                        if "AcemTube" in dosya and "setup.exe" in dosya:
                            os.remove(dosya)
                            print(dosya + " silindi")
                except:
                    print("Güncellemeler Yok")
                try:
                    shutil.rmtree("gunccache")
                except:
                    print("Güncelleme Dizini Yok.")
                global ob_konsol
                ob_konsol += 1
                print(ob_konsol)
                if ob_konsol == 20:
                    print("Konsol Açılıyor!")
                    time.sleep(0.5)

                    for konsoll in pencerebul.get_konsol_name():
                        win32gui.ShowWindow(konsoll , win32con.SW_SHOW)
                    obtt.configure(bg=kirmizi, fg=yazirengi, text="Konsol Açıldı!")
                    pygame.mixer.Sound.play(hata)
                if ob_konsol == 25:
                    print("Konsol Kapatılıyor!")
                    for konsoll in pencerebul.get_konsol_name():
                        win32gui.ShowWindow(konsoll , win32con.SW_HIDE)
                    obtt.configure(bg=kirmizi, fg=yazirengi, text="Konsol Kapatıldı.")
                    pygame.mixer.Sound.play(hata)

            obtt = tk.Button(baslikutu1, text=" Önbellek Sil ", padx=20, pady=20, foreground="black", borderwidth=kenargenisligi, relief=stil, bg=acikmavi, command=obttt)
            obtt.place(rely=0.3, relx=0.77)
            
        def dece():
            pygame.mixer.Sound.play(click)
            webbrowser.open(dclink)

        def kayityol():
            try:
                RPC.update(details="Ayarlarla Oynuyor", state="Kayıt Yolu Ayarlıyor", start=zmn, large_image="acemtubedc", small_image="ayar", small_text="By: Acem#8887", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
            except:
                print("dc yürümüyor.")
            pygame.mixer.Sound.play(click)
            print("kayıtyol basıldı")
            def get_yol():
                with open('data.json', 'r') as f:
                    yol = json.load(f)
                if "kayit_yolu" in yol:
                    if not yol["kayit_yolu"] == "":
                        return yol["kayit_yolu"]
                    else:
                        return "Yok"
                else:
                    return "Yok"
            ayarbaslik.destroy()
            kurulm.destroy()
            ob.destroy()
            dc.destroy()
            kaydetme.destroy()
            dil.destroy()
            bok.destroy()
            
            def kayyaz():
                pygame.mixer.Sound.play(tik)
                print(dosyaadi)
                devamk.destroy()
                sec.destroy()
                kurulbaslik.destroy()
                basyazi.destroy()
                with open('data.json', 'r') as f:
                    yol = json.load(f)
                yol[str(f"kayit_yolu")] = dosyaadi
                with open('data.json', 'w') as f:
                    json.dump(yol, f, indent=4)
                dahayenibaslik = tk.Label(baslikutu, text=f"Başarılı!", bg=acikyesil, fg=baslikyazirengi)
                dahayenibaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                dahayenibaslik.place(relwidth=1, relheight=1)
                basiyazi = tk.Label(baslikutu1, text=f"Ses/Video Kaydetme Yolu Başarıyla Ayarlandı!", bg=arkaplan, fg=yazirengi)
                basiyazi.config(font=("Montserrat Medium", "12"))
                basiyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                anamenu.config(state=NORMAL)
                

            def kaybasla():
                pygame.mixer.Sound.play(click)
                global dosyaadi
                dosyaadi = tk.filedialog.askdirectory(initialdir="/", title="Kayıt Klasörü Seçiniz.")
                pygame.mixer.Sound.play(click)
                print('"' + dosyaadi + '"')
                if not dosyaadi == "":
                    devamk.config(state=NORMAL)
                    secilyazi.config(text=f"Seçilen Yol: {dosyaadi}", bg=arkaplan, fg=yazirengi)
                else:
                    devamk.config(state=DISABLED)
                    secilyazi.config(text=f"Seçilen Yol: Yok", bg=arkaplan, fg=yazirengi)
                
            sec = tk.Button(baslikutu1, text=" Seç ", padx=22, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kaybasla)
            sec.place(rely=0.31, relx= 0.45)
            kurulbaslik = tk.Label(baslikutu, text=f"Kaydetme Yolu Ayarla", bg=acikmavi, fg=baslikyazirengi)
            kurulbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            kurulbaslik.place(relwidth=1, relheight=0.9)
            basyazi = tk.Label(baslikutu1, text=f"Lütfen Aşağıdaki Tuşa Basıp İndirilen Ses Ve Videoların Gideceği Yolu Belirtin.", bg=arkaplan, fg=yazirengi)
            basyazi.config(font=("Montserrat Medium", "12"))
            basyazi.place(relwidth=1, relheight=0.1, rely=0.1)
            devamk = tk.Button(baslikutu1, text=" Uygula ", padx=17, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, state=DISABLED, command=kayyaz)
            devamk.place(rely=0.41, relx= 0.444)
            global secilyazi
            secilyazi = tk.Label(baslikutu1, text=f"Seçili Yol: {get_yol()}", bg=arkaplan, fg=yazirengi)
            secilyazi.config(font=("Montserrat Medium", "10"))
            secilyazi.place(relwidth=1, relheight=0.1, rely=0.2)
            if get_yolst() == "Yok":
                anamenu.config(state=DISABLED)
        def lisans():
            def lisansayr():
                try:
                    RPC.update(details="Ayarlarla Oynuyor", state="Lisans", start=zmn, large_image="acemtubedc", small_image="ayar", small_text="By: Acem#8887", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("dc yürümüyor.")
                pygame.mixer.Sound.play(click)
                lisns.destroy()
                engils.destroy()
                bashakyazi.destroy()
                bashak1yazi.destroy()
                basbaslik.destroy()
                disc.destroy()
                discb.destroy()
                engil.destroy()
                yenlik.destroy()
                def kld_get():
                    with open('data.json', 'r') as f:
                        klad = json.load(f)
                    if "kullanici_adi" in klad:
                        return klad["kullanici_adi"]
                    else:
                        try:
                           RPC.close()
                        except:
                            print("discord yürütülmeimş")
                        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                        root.destroy()
                        exit(0)
#
                def sif_get():
                    with open('data.json', 'r') as f:
                        klad = json.load(f)
                    if "kullanici_parola" in klad:
                        return klad["kullanici_parola"]
                    else:
                        try:
                           RPC.close()
                        except:
                            print("discord yürütülmeimş")
                        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                        root.destroy()
                        exit(0)
                #print(sif_get())
                def sifirla():
                    pygame.mixer.Sound.play(click)
                    pygame.mixer.Sound.play(hata)
                    def sifirlaok():
                        pygame.mixer.Sound.play(click)
                        with open('data.json', 'r') as f:
                            key = json.load(f)
#
                        key.pop("kullanici_adi")
#
                        with open('data.json', 'w') as f:
                            json.dump(key, f, indent=4)
                        with open('data.json', 'r') as f:
                            key1 = json.load(f)
#
                        key1.pop("kullanici_parola")
#
                        with open('data.json', 'w') as f:
                            json.dump(key1, f, indent=4)
                        try:
                           RPC.close()
                        except:
                            print("discord yürütülmeimş")
                        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                        root.destroy()
                        exit(0)

                    devamke.destroy()
                    devamkeslka.destroy()
                    devamkeli.destroy()
                    hatabaslik = tk.Label(baslikutu, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
                    hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    hatabaslik.place(relwidth=1, relheight=1)
                    actlogolbl.destroy()
                    yakyazi.destroy()
                    hatayaziyeni = tk.Label(baslikutu1, text=f'Eğer Devam Ederseniz Program  "{kld_get()}"  Hesabından Çıkış Yapacaktır. ', bg=arkaplan, fg=yazirengi)
                    hatayaziyeni.config(font=("Montserrat Medium", "11"))
                    hatayaziyeni.place(relwidth=1, relheight=0.1, rely=0.12)
                    devamkeslk = tk.Button(baslikutu1, text=" Çıkış Yap ", padx=10, pady=5, foreground=kirmizi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=sifirlaok)
                    devamkeslk.place(rely=0.26, relx= 0.445)
#
                def lisanssil():
                    pygame.mixer.Sound.play(click)
                    pygame.mixer.Sound.play(hata)
                    def sifirlaok():
                        pygame.mixer.Sound.play(click)
#
                        async def hello():
                            uri = server
                            async with websockets.connect(uri) as websocket:
                                istek = f"makinesil-{kld_get()}"

                                print(f"{istek} İsteği Gönderiliyor")
                                await websocket.send(istek)
#
                        asyncio.get_event_loop().run_until_complete(hello())
#
                        with open('data.json', 'r') as f:
                            key = json.load(f)
#
                        key.pop("kullanici_adi")
#
                        with open('data.json', 'w') as f:
                            json.dump(key, f, indent=4)
                        with open('data.json', 'r') as f:
                            key1 = json.load(f)
#
                        key1.pop("kullanici_parola")
#
                        with open('data.json', 'w') as f:
                            json.dump(key1, f, indent=4)
                        try:
                           RPC.close()
                        except:
                            print("discord yürütülmeimş")
                        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                        root.destroy()
                        exit(0)

                    devamke.destroy()
                    devamkeli.destroy()
                    devamkeslka.destroy()
                    hatabaslik = tk.Label(baslikutu, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
                    hatabaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    hatabaslik.place(relwidth=1, relheight=1)
                    actlogolbl.destroy()
                    yakyazi.destroy()
                    hatayaziyeni = tk.Label(baslikutu1, text=f'Eğer Devam Ederseniz Program  "{kld_get()}"  Hesabından Çıkış Yapacak,\nBu Hesaba Bağlı Olan Diğer Bilgisayarların Kimliklerini Silecek. ', bg=arkaplan, fg=yazirengi)
                    hatayaziyeni.config(font=("Montserrat Medium", "11"))
                    hatayaziyeni.place(relwidth=1, relheight=0.2, rely=0.06)
                    devamkeslk = tk.Button(baslikutu1, text=" Çıkış Yap ", padx=10, pady=5, foreground=kirmizi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=sifirlaok)
                    devamkeslk.place(rely=0.26, relx= 0.445)
#
                def lisanssoz():

                    pygame.mixer.Sound.play(click)
                    print("lisanssöz basıldı")
                    #os.startfile(".\BeniOku\lisans.txt")
                    root.attributes('-disabled', True)
                    kpw = tk.Tk()
                    kpw.title("AcemTube Lisans Sözleşmesi")
                    kpw.resizable(False, False)
                    kpw.iconbitmap("acemtubesetup.ico")
                    def kapa():
                        pygame.mixer.Sound.play(click)
                        kpw.destroy()
                        root.attributes('-disabled', False)
                        root.wm_state('iconic')
                        root.wm_state('normal')

#
                    kpw.protocol("WM_DELETE_WINDOW", kapa)
                    yer2 = str(kpw.winfo_screenwidth()/2 - 740/2).split(".")[0]
                    yer3 = str(kpw.winfo_screenheight()/2 - 510/2).split(".")[0]
                    kpw.geometry(f"740x510+{yer2}+{yer3}")
                    kpw.attributes("-alpha", seffaflik)
                    canvas = tk.Canvas(kpw, height=510, width=740, background=arkaplan)
                    canvas.pack()

                    baslikutu8 = tk.Frame(kpw, bg=acikyesil)
                    baslikutu8.place(relwidth=1, relheight=0.1)
    #
                    baslikutu9 = tk.Frame(kpw, bg=acarka)
                    baslikutu9.place(relwidth=0.85, relheight=0.75, rely=0.1, relx=0.08)
                    yanl = tk.Frame(kpw, bg=arkaplan)
                    yanl.place(relwidth=0.08, relheight=0.75, rely=0.1)
                    yanr = tk.Frame(kpw, bg=arkaplan)
                    yanr.place(relwidth=0.07, relheight=0.75, rely=0.1, relx=0.93)
                    baslikutu7 = tk.Frame(kpw, bg=arkaplan)
                    baslikutu7.place(relwidth=1, relheight=0.15, rely=0.85)
                    hatabaslik = tk.Label(baslikutu8, text=f"AcemTube {version} Lisans Sözleşmesi", bg=acikyesil, fg=baslikyazirengi)
                    hatabaslik.config(font=("Montserrat ExtraBold", "27", "italic"))
                    hatabaslik.place(relwidth=1, relheight=1)
                    text_scroll = tk.Scrollbar(baslikutu9)
                    text_scroll.pack(side=RIGHT, fill=Y)

                    lisanstxt = tk.Text(baslikutu9, width=740, height=480, font=("Montserrat Medium", 10), bg=acarka, fg=yazirengi, borderwidth=kenargenisligi, relief=stil, selectbackground=acikyesil, yscrollcommand=text_scroll.set)
                    lisanstxt.pack()

                    text_scroll.config(command=lisanstxt.yview)
                    yb = tk.Button(baslikutu7, text=" Kapat ", padx=15, pady=10, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kapa)
                    yb.place(rely=0.2, relx=0.45)
                    lisanstxt.insert(0.0, soz)

                    lisanstxt.config(state=DISABLED)
                    kpw.mainloop()
#
#
#
                actlogolbl.config(image=actlogol)
                likbaslik = tk.Label(baslikutu, text=f"Lisans", bg=acikyesil, fg=baslikyazirengi)
                likbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                likbaslik.place(relwidth=1, relheight=1)
                yakyazi = tk.Label(baslikutu1, text=f'Acemtube {version}  "{kld_get()}"  İsimli Hesap İle Etkinleştirildi.\nAşağıdan Lisans Sözleşmesini Okuyabilirsiniz. ', bg=arkaplan, fg=yazirengi)
                yakyazi.config(font=("Montserrat Medium", "11"))
                yakyazi.place(relwidth=1, relheight=0.1, rely=0.17)
#
                devamke = tk.Button(baslikutu1, text=" Çıkış Yap ", padx=10, pady=5, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=sifirla)
                devamke.place(rely=0.31, relx= 0.445)
                devamkeli = tk.Button(baslikutu1, text="Tüm Cihazlardan Çık", padx=10, pady=5, foreground=kirmizi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=lisanssil)
                devamkeli.place(rely=0.41, relx= 0.41)
                devamkeslka = tk.Button(baslikutu1, text=" Lisans Sözleşmesi ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=lisanssoz)
                devamkeslka.place(rely=0.5, relx= 0.416)

                if offline_modu:
                    devamkeli.config(state=DISABLED)

            try:
                RPC.update(details="Hakkında Menüsünde", start=zmn, large_image="acemtubedc", small_image="message", small_text="By: Acem#8887", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
            except:
                print("dc yürümüyor.")
            pygame.mixer.Sound.play(click)
            try:
                verkutu.destroy()
            except:
                print("sürüm ok.")
            print("hakkında basıldı")
            ayarbaslik.destroy()
            kurulm.destroy()
            ob.destroy()
            dc.destroy()
            kaydetme.destroy()
            dil.destroy()
            bok.destroy()
            def cikis():
                pygame.mixer.Sound.play(click)
                pygame.mixer.Sound.play(hata)
                root.attributes('-disabled', True)

                def anan():
                    print("anan")
                print("kapatıldım aq")
                kpw = tk.Tk()
                kpw.title("Emin Misiniz?")
                kpw.resizable(False, False)
                kpw.iconbitmap("acemtubered.ico")
                kpw.protocol("WM_DELETE_WINDOW", anan)
                yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
                yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
                kpw.geometry(f"400x150+{yer2}+{yer3}")
                kpw.attributes("-alpha", seffaflik)
                canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
                canvas.pack()
                emnk = tk.Frame(kpw, bg=arkaplan)
                emnk1 = tk.Frame(kpw, bg=arkaplan)
                emnk.place(relwidth=1, relheight=0.7, rely=0.3)
                emnk1.place(relwidth=1, relheight=0.3)
                emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
                emnb.config(font=("Montserrat ExtraBold", "30", "italic"))

                emnb.place(relwidth=1, relheight=0.9)

                ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=arkaplan, fg=yazirengi)
                ckyazi.config(font=("Montserrat Medium", "9"))
                ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
                def cikiss():
                    pygame.mixer.Sound.play(click)
                    try:
                       RPC.close()
                    except:
                        print("discord yürütülmeimş")
                    subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                    root.destroy()
                    kpw.destroy()
                    exit(0)
                def gri():
                    pygame.mixer.Sound.play(click)
                    root.attributes('-disabled', False)
                    kpw.destroy()

                cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
                cikıss.place(rely=0.5, relx= 0.25)
                anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
                anamenuu.place(rely=0.5, relx= 0.57)

                kpw.mainloop()

            def anamenu():
                pygame.mixer.Sound.play(click)
                print("anamenu basıldı")
                baslikutu.destroy()
                baslikutu1.destroy()
                ilkbaslangic(anamenu=1)
            def yenilikler():
                pygame.mixer.Sound.play(click)
                try:
                    RPC.update(details="Hakkında Menüsünde", state=f"{version} Yeniliklerine Bakıyor.", start=zmn, large_image="acemtubedc", small_image="message", small_text="By: Acem#8887", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("dc yürümüyor.")
                print("yenilikler basıldı")
                likbaslik = tk.Label(baslikutu, text=f"Yenilikler", bg=acikyesil, fg=baslikyazirengi)
                likbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                likbaslik.place(relwidth=1, relheight=1)
                lisns.destroy()
                yenlik.destroy()
                
                
                time.sleep(0.1)
                actlogolbl.destroy()
                time.sleep(0.1)
                engils.destroy()
                time.sleep(0.1)
                bashakyazi.destroy()
                time.sleep(0.1)
                bashak1yazi.destroy()
                time.sleep(0.1)
                basbaslik.destroy()
                time.sleep(0.1)
                disc.place(rely=0.73, relx= 0.1)
                time.sleep(0.1)
                discb.place(rely=0.73, relx= 0.4)
                time.sleep(0.1)
                engil.place(rely=0.73, relx= 0.7)
                time.sleep(0.1)
                anagunyazi = tk.Label(baslikutu1, text=f"{version} Yenilikleri:", bg=arkaplan, fg=yazirengi)
                anagunyazi.config(font=("Montserrat Medium", "12"))
                anagunyazi.place(relwidth=1, relheight=0.1, rely=0.01)
                time.sleep(0.1)

                yenilikler = """
3.1.2 Yenilikleri:\n
- Hata Düzeltme Ve İyileştirmeler\n

3.1.1 Yenilikleri:\n
- 8K Video desteği Getirildi.\n
- Temalar ve Kalite Seçme Menüsü Düzeltildi.\n
- Ana Tema M O O D Y olarak değiştirildi.
- Windows 11 Desteği Getirildi.\n
- İstediğiniz Ses Efektlerini Açıp Kapatma Özelliği Eklendi.\n
- Spotify İndirme Arayüzünde Albüm Kapağı Görseli Eklendi.\n
- Video İndirme Arayüzüne Albüm Kapağı Görseli Eklendi.\n
- İndirme Hızları Optimize Edildi.\n
- Video ve Seslerin İndirilememesine Neden Olan Bir Hata\n Düzeltildi.\n
- Offline Mod'ta Hatalar Giderildi.\n
- Spotify Listesi İndirmede Metadata Yazma Hızlandırıldı.\n
- Spotify İndirmelerinde Bazı Şarkıların Yanlışlıkla Sansürlü, Canlı Performans\n veya Klip Versiyonlarının İndirilmesine Neden Olan Bir Hata Giderildi.\n
- Spotify ve Youtube İndirmede Başlığında ':' Bulunan Şarkıların İndirilmeden\n Geçilmesine Neden Olan Bir Hata Giderildi.\n
3.1 Yenilikleri:\n
- Yenilikler Menüsü Yenilendi. ✨\n
- Programa Offline Mod Eklendi.\n
- Yeni Bir Tema Eklendi: INDUSTRIAL\n
- W H I T E O U T Teması Kaldırıldı.\n
- Video İndirmede Format Seçme Menüsü Yeniden Dizayn Edildi\n
- Video İndirmede .mkv Çevirici Sıfırdan Yazıldı.\n
- İndirme Menülerinde Devam Tuşu, Link Kutuları Doldurulmadığı Sürece Devre Dışı\n Olması Özelliği Eklendi.\n
- YouTube Üzerindeki Yaş Kısıtlamalı Videoların İndirilememesine Neden Olan Bir Hata\n Giderildi. 😏\n
- Spotify İndirmelerinde Artık Eğer Klasör Boş Değilse Önceden İndirilen Şarkılar\n Silinmeyecektir, Bozuk mp3'Ler Ayıklanıp Metadata'ları Güncellenecektir.\n
- Spotify İndirmede Parçalara Listedeki Sıralama Numaraları Eklendi.\n
- Artık Spotify İndirmede Albüm Kapak Resimlerinin Dosyaları Önbelleklenmeden\n Yazılacak.\n
- Oynatıcıda Herhangi Bir İndirme Ekranından Çıktıktan Sonra İlerleme Barı\n Ve Ses Barının Bozulmasına Sebep Olan Bir Hata düzeltildi.\n
- Oynatıcıda Şarkı Geçişlerinde Çıkan Click Sesi Kaldırıldı.\n
- Oynatıcıya Albüm Kapağı Resmi Eklendi\n
- Oynatıcıya Özel Klasör Ekleme Özelliği Eklendi.\n
- Oynatıcıda Geri Tuşunun İki Şarkı Geriye Gitmesine Neden Olan Bir Hata Giderildi.\n
- Oynatıcının Desteklenmeyen Formatlarda Şarkıları Geçememesine Neden Olan Hatalar Düzeltildi.\n
- Oynatıcının Karışık Çalma Modu Sıfırdan Yazıldı.\n
- Oynatıcının Arayüzünde Ufak Düzeltmeler Yapıldı.\n
- Oynatıcıda, Parça Listesinin Sıralaması Şarkıların Numaralarına Dayalı Olarak\n Sıralanıcaktır.\n
- Oynatıcı Albüm Kapağı İçin Üç Yeni Tema Ayarı Eklendi: 'thumbnailrengi',\n 'thumbnailikonrengi', 'thumbnaildolgu'\n
- Oynatıcıya Klavye Üzerindeki Medya Kontrol Tuşlarına Uyumluluk Getirildi.\n
- Oynatıcıda Şarkı Listesinde Backspace Tuşu İle Bir Üst Dizine Gitme Eklendi.\n
"""
                
                baslikutu9 = tk.Frame(baslikutu1, bg=acarka)
                baslikutu9.place(relwidth=0.85, relheight=0.60, rely=0.1, relx=0.08)
                text_scroll = tk.Scrollbar(baslikutu9)
                time.sleep(0.1)
                text_scroll.pack(side=RIGHT, fill=Y)


                lisanstxt = tk.Text(baslikutu9, width=740, height=390, font=("Montserrat Medium", 10), bg=acarka, fg=yazirengi, borderwidth=kenargenisligi, relief=stil, selectbackground=acikyesil, yscrollcommand=text_scroll.set)
                lisanstxt.pack()
                lisanstxt.config(state=DISABLED)

                
                text_scroll.config(command=lisanstxt.yview)

                satırliste = yenilikler.splitlines()
                for yenilik in satırliste:
                    time.sleep(0.009)

                    lisanstxt.config(state=NORMAL)
                    lisanstxt.insert(END, "\n" + yenilik)
                    lisanstxt.config(state=DISABLED)
                    lisanstxt.see(END)
                time.sleep(0.05)
                lisanstxt.see(0.0)
                #lisanstxt.config(state=NORMAL)
                #lisanstxt.insert(0.0, yenilikler)
                #lisanstxt.config(state=DISABLED)

                #gunyazi9 = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=yazirengi)
                #gunyazi9.config(font=("Montserrat Medium", "9"))
                #gunyazi9.place(relwidth=1, relheight=0.03, rely=0.74)


            cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
            cikıs.place(rely=0.87, relx= 0.89)
            anamenu = tk.Button(baslikutu1, text=" Ana Menü ", padx=0, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=anamenu)
            anamenu.place(rely=0.8, relx= 0.89)

            #anamenu.place(rely=0.7, relx= 0.89)
            #cikıs.place(rely=0.77, relx= 0.89)
            basbaslik = tk.Label(baslikutu, text=f"Hakkında", bg=acikyesil, fg=baslikyazirengi)
            basbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            basbaslik.place(relwidth=1, relheight=1)

            global actlogo
            actlogo = ImageTk.PhotoImage(Image.open("acemtubesetups.png"))
            global actlogol
            actlogol = ImageTk.PhotoImage(Image.open("acemtubes.png"))
            actlogolbl = tk.Label(baslikutu1, image=actlogo, bg=arkaplan ,fg=acikgri2)
            actlogolbl.pack(pady=15)

            time.sleep(0.1)
            bashakyazi = tk.Label(baslikutu1, text=f"AcemTube Yüksek Kaliteli Spotify, Ses, Video İndirme Programıdır. \n 4K 60 FPS Kaliteye Kadar Video Ve 320 Kbps Kaliteye Kadar Ses İndirme Seçenekleri Vardır.", bg=arkaplan, fg=yazirengi)
            bashakyazi.config(font=("Montserrat Medium", "11"))
            bashakyazi.place(relwidth=1, relheight=0.1, rely=0.2)
            time.sleep(0.1)
            bashak1yazi = tk.Label(baslikutu1, text=f"Sürüm: {version} ({tarih}). Python Dilinde Acem Tarafından Yazılmıştır.", bg=arkaplan, fg=yazirengi)
            bashak1yazi.config(font=("Montserrat Medium", "10"))
            bashak1yazi.place(relwidth=1, relheight=0.1, rely=0.3)
            time.sleep(0.1)
            disc.place(rely=0.45, relx= 0.1)
            time.sleep(0.1)
            discb.place(rely=0.45, relx= 0.4)
            time.sleep(0.1)
            engil.place(rely=0.45, relx= 0.7)
            time.sleep(0.1)
            lisns = tk.Button(baslikutu1, text=" Lisans ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=lisansayr)
            lisns.place(rely=0.63, relx= 0.45)
            time.sleep(0.1)
            yenlik = tk.Button(baslikutu1, text=f"{version} Yenilikleri", padx=17.8, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=yenilikler).start)
            yenlik.place(rely=0.73, relx= 0.419)
            
 
           

        def dill():
            pygame.mixer.Sound.play(click)
            #disc.place(rely=0.5, relx= 0.1)
            #discb.place(rely=0.5, relx= 0.4)
            #engil.place(rely=0.5, relx= 0.7)
            #webbrowser.open(dclink)
            ayarbaslik.destroy()
            kurulm.destroy()
            ob.destroy()
            dc.destroy()
            kaydetme.destroy()
            dil.destroy()
            bok.destroy()
            likbaslik = tk.Label(baslikutu, text=f"Temalar", bg=acikmavi, fg=baslikyazirengi)
            likbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            likbaslik.place(relwidth=1, relheight=1)
            yakyazi = tk.Label(baslikutu1, text=f"Aşağıdan İstediğiniz Temayı Seçin.", bg=arkaplan, fg=yazirengi)
            yakyazi.config(font=("Montserrat Medium", "12"))
            yakyazi.place(relwidth=1, relheight=0.1, rely=0.1)

            menu = tk.StringVar()
            menu.set(altyazi)
            
            temalist = []
            silinenler = []
            temadir = os.listdir(r"./temalar")
            temalist.append("B L Λ C K O U T")
            for tema in temadir:
                if tema.endswith(".actema"):
                    temalist.append(tema.split(".actema")[0])

            def clicky(menu):
                pygame.mixer.Sound.play(click)
                temauyg.config(state=NORMAL)
                if menu == "B L Λ C K O U T" or menu in silinenler:
                    temasil.config(state=DISABLED)
                    
                else:
                    temasil.config(state=NORMAL)
                    temauyg.config(state=NORMAL)
            def temayaz():
                pygame.mixer.Sound.play(click)
                menooo = menu.get()
                if menu.get() != "B L Λ C K O U T":
                    secilentema = fr"./temalar/{menu.get()}.actema"
                    with open('data.json', 'r') as f:
                        yol = json.load(f)
                    yol[str(f"tema_yolu")] = secilentema
                    with open('data.json', 'w') as f:
                        json.dump(yol, f, indent=4)
                else:
                    with open('data.json', 'r') as f:
                        yol = json.load(f)
                    yol[str(f"tema_yolu")] = 0
                    with open('data.json', 'w') as f:
                        json.dump(yol, f, indent=4)
                pygame.mixer.Sound.play(tik)
                temauyg.destroy()
                temaekle.destroy()
                menub.destroy()
                dahayenibaslik = tk.Label(baslikutu, text=f"Başarılı!", bg=acikyesil, fg=baslikyazirengi)
                dahayenibaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                dahayenibaslik.place(relwidth=1, relheight=1)
                basiyazi = tk.Label(baslikutu1, text=f"Tema Başarıyla Ayarlandı!", bg=arkaplan, fg=yazirengi)
                basiyazi.config(font=("Montserrat Medium", "12"))
                basiyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                secilyazi = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=yazirengi)
                secilyazi.config(font=("Montserrat Medium", "10"))
                secilyazi.place(relwidth=1, relheight=0.1, rely=0.2)
                secilyazi.config(text=f"Seçilen Tema: {menooo}", bg=arkaplan, fg=yazirengi)
                bas1yazi = tk.Label(baslikutu1, text=f"NOT: Değişikliklerin Etki Etmesi İçin Programın Yeniden Başlatılması Gerekir.", bg=kirmizi, fg=yazirengi)
                bas1yazi.config(font=("Montserrat Medium", "10"))
                bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                def ybbb():
                    pygame.mixer.Sound.play(click)
                    try:
                        os.startfile("acemtube.exe")
                        try:
                            RPC.close()
                        except:
                            print("discord yürütülmeimş")
                        root.destroy()
                        exit(0)
                    except:
                        try:
                            os.startfile("acemtube.py")
                            try:
                               RPC.close()
                            except:
                                print("discord yürütülmeimş")
                            root.destroy()
                            exit(0)
                        except:
                            print("dosya yok")
                yb = tk.Button(baslikutu1, text=" Yeniden Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybbb)
                yb.place(rely=0.65, relx= 0.42)

            temauyg = tk.Button(baslikutu1, text=" Uygula ", padx=17, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, state=DISABLED, command=temayaz)
            temauyg.place(rely=0.3, relx= 0.444)
            
            def temae():
                pygame.mixer.Sound.play(click)
                print("temaeekle basıldı")
                def get_yol():
                    with open('data.json', 'r') as f:
                        yol = json.load(f)
                    if "kayit_yolu" in yol:
                        if not yol["kayit_yolu"] == "":
                            return yol["kayit_yolu"]
                        else:
                            return "/"
                    else:
                        return "/"
                temasil.destroy()
                menub.destroy()
                temauyg.destroy()
                yakyazi.destroy()
                temaekle.destroy()
                
                def kayyaz():
                    pygame.mixer.Sound.play(tik)
                    print(dosyaadi)
                    devamk.destroy()
                    sec.destroy()
                    kurulbaslik.destroy()
                    basyazi.destroy()
                    shutil.copy(dosyaadi, r"./temalar")
                    dosyaadi1 = dosyaadi.split("/")[-1]
                    yenitema = fr"./temalar/{dosyaadi1}"
                    with open('data.json', 'r') as f:
                        yol = json.load(f)
                    yol[str(f"tema_yolu")] = yenitema
                    with open('data.json', 'w') as f:
                        json.dump(yol, f, indent=4)
                    dahayenibaslik = tk.Label(baslikutu, text=f"Başarılı!", bg=acikyesil, fg=baslikyazirengi)
                    dahayenibaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    dahayenibaslik.place(relwidth=1, relheight=1)
                    basiyazi = tk.Label(baslikutu1, text=f"Yeni Tema Başarıyla Eklendi!", bg=arkaplan, fg=yazirengi)
                    basiyazi.config(font=("Montserrat Medium", "12"))
                    basiyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                    bas1yazi = tk.Label(baslikutu1, text=f"NOT: Değişikliklerin Etki Etmesi İçin Programın Yeniden Başlatılması Gerekir.", bg=kirmizi, fg=yazirengi)
                    bas1yazi.config(font=("Montserrat Medium", "10"))
                    bas1yazi.place(relwidth=1, relheight=0.1, rely=0.5)
                    def ybbb():
                        pygame.mixer.Sound.play(click)
                        try:
                            os.startfile("acemtube.exe")
                            try:
                                RPC.close()
                            except:
                                print("discord yürütülmeimş")
                            root.destroy()
                            exit(0)
                        except:
                            try:
                                os.startfile("acemtube.py")
                                try:
                                   RPC.close()
                                except:
                                    print("discord yürütülmeimş")
                                root.destroy()
                                exit(0)
                            except:
                                print("dosya yok")
                    yb = tk.Button(baslikutu1, text=" Yeniden Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybbb)
                    yb.place(rely=0.65, relx= 0.42)

                def kaybasla():
                    pygame.mixer.Sound.play(click)
                    global dosyaadi
                    dosyaadi = tk.filedialog.askopenfilename(initialdir = get_yol(), title = "Tema Seçiniz.", filetypes = (("AcemTube Temaları","*.actema"),("Tüm Dosyalar","*.*")))
                    pygame.mixer.Sound.play(click)
                    print('"' + dosyaadi + '"')
                    if not dosyaadi == "":
                        devamk.config(state=NORMAL)
                        secilyazi.config(text=f"Eklenen Tema: {dosyaadi}", bg=arkaplan, fg=yazirengi)
                    else:
                        devamk.config(state=DISABLED)
                        secilyazi.config(text=f"", bg=arkaplan, fg=yazirengi)
                
                sec = tk.Button(baslikutu1, text=" Seç ", padx=22, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kaybasla)
                sec.place(rely=0.31, relx= 0.45)
                kurulbaslik = tk.Label(baslikutu, text=f"Tema Ekle", bg=acikmavi, fg=baslikyazirengi)
                kurulbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                kurulbaslik.place(relwidth=1, relheight=0.9)
                basyazi = tk.Label(baslikutu1, text=f"Lütfen Aşağıdaki Tuşa Basıp Eklemek İstediğiniz Temayı Seçin.", bg=arkaplan, fg=yazirengi)
                basyazi.config(font=("Montserrat Medium", "12"))
                basyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                devamk = tk.Button(baslikutu1, text=" Uygula ", padx=17, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, state=DISABLED, command=kayyaz)
                devamk.place(rely=0.41, relx= 0.444)
                global secilyazi
                secilyazi = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=yazirengi)
                secilyazi.config(font=("Montserrat Medium", "10"))
                secilyazi.place(relwidth=1, relheight=0.1, rely=0.2)

            def temayisil():
                pygame.mixer.Sound.play(click)
                temasil.config(state=DISABLED)

                silinecek = menu.get()
                os.remove(r"./temalar/" + silinecek + ".actema")
                silinenler.append(silinecek)
                menu.set("B L Λ C K O U T")
                

            temaekle = tk.Button(baslikutu1, text=" Tema Ekle ", padx=5, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=temae)
            temaekle.place(rely=0.41, relx= 0.45)
            def temaindirb():
                pygame.mixer.Sound.play(click)
                webbrowser.open(temalink)

            temaindir = tk.Button(baslikutu1, text=" Tema İndir ", padx=5, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=temaindirb)
            temaindir.place(rely=0.71, relx= 0.45)

            menub = tk.OptionMenu(baslikutu1, menu, *temalist, command=clicky)

            temasil = tk.Button(baslikutu1, text=" Temayı Sil ", padx=5, pady=5, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=temayisil)
            temasil.place(rely=0.51, relx= 0.45)
            if menu.get() == "B L Λ C K O U T" or menu.get() in silinenler:
                temasil.config(state=DISABLED)
                
            else:
                temasil.config(state=NORMAL)
                temauyg.config(state=NORMAL)
            menub.config(bg=koyugri, fg=yazirengi, borderwidth=kenargenisligi)
            #menub.place(rely=0.19, relx=0.42)
            menub.pack(pady=90)

        def surumbitiyor():
            pygame.mixer.Sound.play(click)
            cikıs.destroy()
            anamenu.destroy()
            kurulm.destroy()
            ob.destroy()
            dc.destroy()
        
            root.title(f"AcemTube Güncelleyici")
            
            root.iconbitmap("acemtubesetup.ico")
            yer2 = str(root.winfo_screenwidth()/2 - 700/2).split(".")[0]
            yer3 = str(root.winfo_screenheight()/2 - 400/2).split(".")[0]
            root.geometry(f"700x400")
           
            baslikutu.destroy()
            baslikutu1.destroy()


            emnk = tk.Frame(root, bg=arkaplan)
            emnk1 = tk.Frame(root, bg=arkaplan)
            emnk.place(relwidth=1, relheight=0.8, rely=0.2)
            emnk1.place(relwidth=1, relheight=0.2)
            emnb = tk.Label(emnk1, text=f"AcemTube Güncelleyici", bg=acikmavi, fg=baslikyazirengi)
            emnb.config(font=("Montserrat ExtraBold", "30", "italic"))    
            emnb.place(relwidth=1, relheight=0.9)

            ckyazi = tk.Label(emnk, text=f"Kontrol Ediliyor...", bg=arkaplan, fg=yazirengi)
            ckyazi.config(font=("Montserrat Medium", "9"))
            ckyazi.place(relwidth=1, relheight=0.15, rely=0.2)
            ckyazi1 = tk.Label(emnk, text=f"Kontrol Ediliyor...", bg=arkaplan, fg=yazirengi)
            ckyazi1.config(font=("Montserrat Medium", "9"))
            ckyazi1.place(relwidth=1, relheight=0.15, rely=0.3)
            
            def cikiss():
                pygame.mixer.Sound.play(click)
                root.destroy()
                ilkbaslangic(anamenu=2)
                root.attributes('-disabled', False)
            def gri():
                pygame.mixer.Sound.play(click)
                try:
                    RPC.update(details="AcemTube Güncelleyici", start=zmn, state="İndiriliyor", large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("discord yürümüyor.")
                emnk.destroy()
                emnk1.destroy()
                emnb.destroy()
                cikıss.destroy()
                anamenuu.destroy()
                yer = str(root.winfo_screenwidth()/2 - 350/2).split(".")[0]
                yer1 = str(root.winfo_screenheight()/2 - 100/2).split(".")[0]
                root.geometry(f"350x90+{yer}+{yer1}")
                root.overrideredirect(1)
                
                #baslikutu = tk.Frame(root, bg=acikmavi)
                #baslikutu.place(relwidth=1, relheight=0.1)
                #008000
                #313542
                baslikutu1 = tk.Frame(root, bg=arkaplan)
                baslikutu1.place(relwidth=1, relheight=1)
                baslik = tk.Label(baslikutu1, text=f" AcemTube", bg=arkaplan, fg=baslikyazirengi)
                baslik.config(font=("Montserrat ExtraBold", "29", "bold italic"))
                baslik1 = tk.Label(baslikutu1, text=f"Güncelleniyor...", bg=arkaplan, fg=baslikyazirengi)
                baslik1.config(font=("Montserrat ExtraBold", "12", "bold italic"))
                baslik.place(relwidth=0.7, relheight=0.6, relx=0.255)
                baslik1.place(relwidth=0.65, relheight=0.22, relx=0.3, rely=0.5)
                frm = tk.Frame()
                logo = ImageTk.PhotoImage(Image.open("acemtubesetups.png"))
                rlbl = tk.Label(baslikutu1, image=logo, bg=arkaplan ,fg=acikgri2)
                rlbl.place(relwidth=0.3, relheight=0.83)
                muzikres["muzikres"] = 1
                s = ttk.Style()
                s.theme_use("clam")

                s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
                prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="indeterminate")
                prgs.place(rely=0.791)
                prgs.start(24)
                try:
                    os.mkdir("gunccache")
                except:
                    print("dizin zaten var")
                dosyaadi = updlink.split("/")[-1]
                try:
                    os.remove(dosyaadi)
                    print("dosya var")
                except:
                    pass
                time.sleep(3)
                baslik1.config(text="İndiriliyor...")
                updget = requests.get(updlink)
                print(dosyaadi)
                
                baslik1.config(text="Yazılıyor...")
                time.sleep(1)
                with open(dosyaadi, "wb") as f:
                    for chunk in updget.iter_content(chunk_size=chunkboyut):
                        if chunk:
                            f.write(chunk)
                shutil.move(dosyaadi, r"./gunccache")
                baslik1.config(text="Temizleniyor...")
                sayi = 0
                for dosya in os.listdir(r"./"):
                    if "AcemTube" in dosya and "setup.exe" in dosya:
                        os.remove(dosya)
                        print(dosya + " silindi")
                        sayi += 1
                        baslik1.config(text=f"Temizleniyor: ({sayi})...")
                        time.sleep(0.5)
                
                baslik1.config(text="Yürütülüyor...")
                time.sleep(1)
                shutil.move( r"./gunccache/" + dosyaadi, r"./")
                try:
                    shutil.rmtree("gunccache")
                except:
                    print("dizin yok")
        
                baslik1.config(text="Tamamlandı!   ")
                time.sleep(0.5)
                os.startfile(f"{dosyaadi}")
                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)

            cikıss = tk.Button(emnk, text= "       Çıkış       ", padx=30, pady=10, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
            cikıss.place(rely=0.5, relx= 0.25)
            anamenuu = tk.Button(emnk, text=" Güncellemeyi İndir ", padx=20, pady=10, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=gri).start)
            anamenuu.place(rely=0.5, relx= 0.55)
            anamenuu.config(state=DISABLED)
            if verakt == "2" or verakt == "0":
                ckyazi.config(text=f"Yeni Bir Güncelleme ({guncelsurumadi}) Mevcut! Hemen İndirmek İçin Aşağıdaki Butona Basın. Geçerli Sürüm: ({version})")
                ckyazi1.config(text=f"Geçerli Sürüm: ({version}) Yeni Sürüm: ({guncelsurumadi})")
                anamenuu.config(state=NORMAL)
                emnb.config(text="Güncelleme Mevcut.", bg="#ff7b00")
                try:
                    RPC.update(details="AcemTube Güncelleyici", start=zmn, state="Güncelleme Mevcut", large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("discord yürümüyor.")
            else:
                try:
                    RPC.update(details="AcemTube Güncelleyici", start=zmn, state=f"Sürüm ({version}) Güncel", large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("discord yürümüyor.")
                ckyazi.config(text=f"Sürümünüz Güncel.")    
                ckyazi1.config(text=f"Geçerli Sürüm: ({version})")

        engils.destroy()
        cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, bg=koyugri, command=cikis)
        cikıs.place(rely=0.87, relx= 0.89)
        anamenu = tk.Button(baslikutu1, text=" Ana Menü ", padx=0, pady=1, foreground=yazirengi, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, bg=koyugri, command=anamenu)
        anamenu.place(rely=0.8, relx= 0.89)
        kurulm = tk.Button(baslikutu1, text=" Kurulum ", padx=46, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kurulum)
        kurulm.place(rely=0.1, relx= 0.1)
        ob = tk.Button(baslikutu1, text=" Diğer Ayarlar ", padx=31, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=obt)
        ob.place(rely=0.1, relx= 0.7)
        dc = tk.Button(baslikutu1, text=" Güncellemeleri Al ", padx=25, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=surumbitiyor).start)
        dc.place(rely=0.1, relx= 0.4)

        kaydetme = tk.Button(baslikutu1, text="İndirme Yolu", padx=38, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kayityol)
        kaydetme.place(rely=0.45, relx= 0.1)
        
        dil = tk.Button(baslikutu1, text=" Temalar ", padx=45, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dill)
        dil.place(rely=0.45, relx= 0.7)
        bok = tk.Button(baslikutu1, text="Hakkında", padx=49, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=lisans).start)
        bok.place(rely=0.45, relx= 0.4)
        if offline_modu:
            kurulm.config(state=DISABLED)
            dc.config(state=DISABLED)
        if get_yolst() == "Yok":
            kaydetme.invoke()
    def cıkıs():
        pygame.mixer.Sound.play(click)
        pygame.mixer.Sound.play(click)
        pygame.mixer.Sound.play(hata)
        root.attributes('-disabled', True)
        
        def anan():
            print("anan")
        print("kapatıldım aq")
        kpw = tk.Tk()
        kpw.title("Emin Misiniz?")
        kpw.resizable(False, False)
        kpw.iconbitmap("acemtubered.ico")
        kpw.protocol("WM_DELETE_WINDOW", anan)
        yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
        yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
        kpw.geometry(f"400x150+{yer2}+{yer3}")
        kpw.attributes("-alpha", seffaflik)
        canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
        canvas.pack()
        emnk = tk.Frame(kpw, bg=arkaplan)
        emnk1 = tk.Frame(kpw, bg=arkaplan)
        emnk.place(relwidth=1, relheight=0.7, rely=0.3)
        emnk1.place(relwidth=1, relheight=0.3)
        emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
        emnb.config(font=("Montserrat ExtraBold", "30", "italic"))
    
        emnb.place(relwidth=1, relheight=0.9)
        
        ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=arkaplan, fg=yazirengi)
        ckyazi.config(font=("Montserrat Medium", "9"))
        ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
        def cikiss():
            pygame.mixer.Sound.play(click)
            try:
               RPC.close()
            except:
                print("discord yürütülmeimş")
            subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
            root.destroy()
            kpw.destroy()
            exit(0)
        def gri():
            pygame.mixer.Sound.play(click)
            root.attributes('-disabled', False)
            kpw.destroy()
    
        cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
        cikıss.place(rely=0.5, relx= 0.25)
        anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
        anamenuu.place(rely=0.5, relx= 0.57)
        kpw.mainloop()

    def restart_arayuz():
        root.destroy()
        ilkbaslangic(anamenu=3)

    anamenures = tk.Button(root, text="", padx=1, pady=1, foreground=arkaplan, bg=arkaplan, activebackground=arkaplan, activeforeground=arkaplan, highlightbackground=arkaplan, borderwidth=kenargenisligi, relief=stil, command=restart_arayuz)
    anamenures.place(rely=0.1, relx= 0.1)

    def mp3oynatici():
        if muzikres["muzikres"] == 0:
            pygame.mixer.music.fadeout(900)

            print("mp3")
            try:
                RPC.update(details="Oynatıcıda", large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
            except:
                print("dc yürümüyor.")
            try:
                verkutu.destroy()
            except:
                print("sürüm ok.")

            def get_yol():
                with open('data.json', 'r') as f:
                    yol = json.load(f)
                if "kayit_yolu" in yol:
                    if not yol["kayit_yolu"] == "":
                        return yol["kayit_yolu"]
                    else:
                        return "Yok"
                else:
                    return "Yok"
            pygame.mixer.Sound.play(click)
            print("spotify basıldı")
            ses.config(state=DISABLED)
            hkd.config(state=DISABLED)
            video.config(state=DISABLED)
            ayarlar.config(state=DISABLED)
            spotify.config(state=DISABLED)
            cıkıs.config(state=DISABLED)
            ses.destroy()
            hkd.destroy()

            video.destroy()
            ayarlar.destroy()

            spotify.destroy()
            cıkıs.destroy()
            baslik.destroy()
            engils.destroy()
            baslik.destroy()
            likbaslik = tk.Label(baslikutu, text=f"Oynatıcı", bg=acikmavi, fg=baslikyazirengi)
            likbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            likbaslik.place(relwidth=1, relheight=1)
            oynyazi = tk.Label(baslikutu1, text=f" ", bg=arkaplan, fg=yazirengi)
            oynyazi.config(font=("Montserrat Medium", "12"))
            oynyazi.place(relwidth=1, relheight=0.1, rely=0.62)

            if offline_modu:
                likbaslik.config(text="Offline Oynatıcı")
 
            def uznal(sure):
                if sure != 0 or sure != -1:
                    saniye = round(sure / 1000)
                    uzunluk = str(datetime.timedelta(seconds = saniye))
                    if uzunluk.startswith("0:"):
                      return uzunluk[2:].replace('days,', 'gün,')
                    else:
                      return uzunluk.replace('days,', 'gün,')
                else:
                    return "00:00"

            def uznals(sure):
                if sure != 0 or sure != -1:
                    saniye = round(sure)
                    uzunluk = str(datetime.timedelta(seconds = saniye))
                    if uzunluk.startswith("0:"):
                      return uzunluk[2:].replace('days,', 'gün,')
                    else:
                      return uzunluk.replace('days,', 'gün,')
                else:
                    return "00:00"



            def ilerlet(bob):
                print(bob)
                suan = pygame.mixer.music.get_pos()
                oynatici["oynatildi"] = float(bob) * 1000
                #pygame.mixer.music.set_pos(float(bob))
                pygame.mixer.music.play(loops=0, start=float(bob))
                oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)

            global s
            s = ttk.Style()
            #style.theme_use()
            s.configure("TScale", background=arkaplan, foreground=acikmavi)
            #print(style.theme_use())
            print(s.theme_names())
            ilerleme = ttk.Scale(baslikutu1, from_=0, to=100, length=500, orient=HORIZONTAL, value=0, command=ilerlet)

            oynatici = {
                "loop": "sira",
                "karistir": 0,
                "oynatildi": 0,
                "sesyzd": 0
            }
            def albumkapakuygula():
                try:
                    sarkikonumu = oynatici["sira"][oynatici["konum"]]

                    tagler = ID3(sarkikonumu)
                    resim = tagler.get("APIC:").data
                    imag = Image.open(BytesIO(resim))
                    
                    if imag.width != imag.height:
                        imag = resim_aletleri.kareyegenislet(imag, resim_aletleri.hexecevir(thumbnaildolgu))

                    yeniboyut = imag.resize((240,240), Image.Resampling.LANCZOS)

                    global albumpng
                    albumpng = ImageTk.PhotoImage(yeniboyut)
                    albumkapak.config(image=albumpng)
                except:
                    albumkapak.config(image=albumkapakpng)

            def sarkisuresial():
                suan = pygame.mixer.music.get_pos() + oynatici["oynatildi"]

                #print(int(suan))
                sureyazi.config(text=str(uznal(int(suan))))
                ilerleme.config(value=suan/1000)
                sureyazi.after(100, sarkisuresial)

            sureyazi = tk.Label(baslikutu1, text=f"00:00", bg=arkaplan, fg=yazirengi)
            sureyazi.config(font=("Montserrat Medium", "9"))
            sureyazi.place(relwidth=0.05, relheight=0.05, rely=0.7, relx=0.10)
            kalanyazi = tk.Label(baslikutu1, text=f"00:00", bg=arkaplan, fg=yazirengi)
            kalanyazi.config(font=("Montserrat Medium", "9"))
            kalanyazi.place(relwidth=0.05, relheight=0.05, rely=0.7, relx=0.85)
            sarkisuresial()

            def customklasor():
                with open('data.json', 'r') as f:
                    bilgiler = json.load(f)
                if "ozelklasor" in bilgiler:
                    return bilgiler["ozelklasor"]
                else:
                    return {}

            sarkisecimi = tk.Listbox(baslikutu1, bg=arkaplan, fg=yazirengi, width=95, height=15, bd=0, activestyle="none", selectbackground=acikyesil)
            sarkisecimi.pack(pady=40)
            sarkisecimi.insert(tk.END, "Spotify")
            sarkisecimi.insert(tk.END, "YouTube")
            ozelklasorisimleri = customklasor().keys()
            for klasorisim in ozelklasorisimleri:
                sarkisecimi.insert(tk.END, klasorisim)
            sarkisecimi.insert(tk.END, ">Özel Klasörleri Düzenle")

            global oynattuspng
            gerituspng = ImageTk.PhotoImage(file="previus.png")
            global oynattuspng
            ilerituspng = ImageTk.PhotoImage(file="next.png")
            global oynattuspng
            oynattuspng = ImageTk.PhotoImage(file="play.png")
            global durdurtuspng
            durdurtuspng = ImageTk.PhotoImage(file="pause.png")
            global karistirtuspng
            karistirtuspng = ImageTk.PhotoImage(file="shuffle.png")
            global karisiktuspng
            karisiktuspng = ImageTk.PhotoImage(file="shuffleg.png")
            global looptuspng
            looptuspng = ImageTk.PhotoImage(file="loop.png")
            global loopgpng
            loopgpng = ImageTk.PhotoImage(file="loopg.png")
            global loop1png
            loop1png = ImageTk.PhotoImage(file="loop1.png")
            global mutepng
            mutepng = ImageTk.PhotoImage(file="mute.png")
            global unmutepng
            unmutepng = ImageTk.PhotoImage(file="unmute.png")
            global albumkapakpng
            #
            alk = Image.open("albumcovr.png") 
            alk2 = albmkpk = Image.new(alk.mode, (240, 240), resim_aletleri.hexecevir(thumbnailikonrengi))
            albmkpk = Image.new(alk.mode, (240, 240), resim_aletleri.hexecevir(thumbnailrengi))
            albmkpk.paste(alk2, (0, 0), alk)
            albumkapakpng = ImageTk.PhotoImage(albmkpk)
            

            ilerleme.pack()

            tuscercevesi = tk.Frame(baslikutu1, bg=arkaplan)  

            tuscercevesi.pack(pady= 10)

            sesyzd = tk.Label(baslikutu1, text=f"%50", bg=arkaplan, fg="#ffffff")
            sesyzd.config(font=("Montserrat Medium", "7"))

            def sesayr(bob):
                print(bob)
                pygame.mixer.music.set_volume(float(bob))
                sesyzd.config(text="%" + str(round(100 * round(float(bob), 2))))
                if float(bob) == float(0.0):
                    mutetus.config(state=NORMAL, image=mutepng)
                else:
                    mutetus.config(state=NORMAL, image=unmutepng) 

            sesayrb = ttk.Scale(baslikutu1, from_=0, to=1, length=130, orient=HORIZONTAL, value=0.5, command=sesayr)
            sesayrb.pack(pady= 5)
            pygame.mixer.music.set_volume(0.5)

            def mutefunc():
                pygame.mixer.Sound.play(click)
                if float(sesayrb.get()) != (0.0):
                    gecerlises = float(sesayrb.get())
                    mutetus.config(state=NORMAL, image=mutepng)
                    pygame.mixer.music.set_volume(0)
                    sesayrb.config(value=0)
                    sesyzd.config(text="%0")
                    oynatici["sesyzd"] = gecerlises
                else:
                    gecerlises = oynatici["sesyzd"]
                    mutetus.config(state=NORMAL, image=unmutepng)
                    pygame.mixer.music.set_volume(gecerlises)
                    sesayrb.config(value=gecerlises)
                    sesyzd.config(text="%" + str(round(100 * round(float(gecerlises), 2))))

            def geri(klik=True):
                if klik:
                    pygame.mixer.Sound.play(click)
                
                konum = oynatici["konum"] 
                sira = oynatici["sira"]
                oynatici["oynatildi"] = 0
                print(sira)
                print(konum)
                try:
                    if konum > 0:
                        pygame.mixer.music.load(sira[konum])
                        pygame.mixer.music.play(loops=0)
                        oynyazi.config(text=sira[konum].split("/")[-1].replace(".mp3", ""))
                        ilerleme.config(state=NORMAL, to=MP3(sira[konum]).info.length, value=0)
                        zamn = int(datetime.datetime.now().timestamp())
                        try:
                            RPC.update(details="Şarkı Dinliyor", state=sira[konum].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                        except:
                            print("dc yürümüyor.")
                        albumkapakuygula()
                        if oynatici["loop"] == "gecerli":
                            pygame.mixer.music.load(sira[konum + 1])
                            pygame.mixer.music.play(loops=0)
                            oynyazi.config(text=sira[konum + 1].split("/")[-1].replace(".mp3", ""))
                            kalanyazi.config(text=uznals(MP3(sira[konum + 1]).info.length))
                            oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                            ilerleme.config(state=NORMAL, to=MP3(sira[konum + 1]).info.length, value=0)
                            albumkapakuygula()
                            zamn = int(datetime.datetime.now().timestamp())
                            try:
                                RPC.update(details="Şarkı Dinliyor", state=sira[konum + 1].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")
                        else:
                            oynatici["konum"] = oynatici["konum"] - 1
                            pygame.mixer.music.load(sira[konum - 1])
                            pygame.mixer.music.play(loops=0)
                            oynyazi.config(text=sira[konum - 1].split("/")[-1].replace(".mp3", ""))
                            kalanyazi.config(text=uznals(MP3(sira[konum - 1]).info.length))
                            oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                            ilerleme.config(state=NORMAL, to=MP3(sira[konum - 1]).info.length, value=0)
                            albumkapakuygula()
                            zamn = int(datetime.datetime.now().timestamp())
                            try:
                                RPC.update(details="Şarkı Dinliyor", state=sira[konum - 1].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")
                    else:
                        pygame.mixer.music.load(sira[0])
                        pygame.mixer.music.play(loops=0)
                        oynyazi.config(text=sira[0].split("/")[-1].replace(".mp3", ""))
                        kalanyazi.config(text=uznals(MP3(sira[0]).info.length))
                        oynatici["konum"] = 0
                        oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                        ilerleme.config(state=NORMAL, to=MP3(sira[0]).info.length, value=0)
                        albumkapakuygula()
                        zamn = int(datetime.datetime.now().timestamp())
                        try:
                            RPC.update(details="Şarkı Dinliyor", state=sira[0].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                        except:
                            print("dc yürümüyor.")
                except: 
                    if not oynatici["konum"] < 1:
                        oynatici["konum"] = konum - 1
                        geri(klik=False)

            def durdur():
                pygame.mixer.Sound.play(click)
                pygame.mixer.music.pause()
                oynattus.config(command=oynat, image=oynattuspng)

            def oynat():
                pygame.mixer.Sound.play(click)
                pygame.mixer.music.unpause()
                oynattus.config(command=durdur, image=durdurtuspng)

            def ileri(klik=True):
                if klik:
                    pygame.mixer.Sound.play(click)

                konum = oynatici["konum"] + 1
                sira = oynatici["sira"]
                oynatici["oynatildi"] = 0
                try:
                    if not konum >= len(sira):
                        if not oynatici["loop"] == "gecerli":
                            pygame.mixer.music.load(sira[konum])
                            pygame.mixer.music.play(loops=0)
                            oynyazi.config(text=sira[konum].split("/")[-1].replace(".mp3", ""))
                            kalanyazi.config(text=uznals(MP3(sira[konum]).info.length))
                            oynatici["konum"] = oynatici["konum"] + 1
                            oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                            ilerleme.config(state=NORMAL, to=MP3(sira[konum]).info.length, value=0)
                            albumkapakuygula()
                            zamn = int(datetime.datetime.now().timestamp())
                            try:
                                RPC.update(details="Şarkı Dinliyor", state=sira[konum].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")

                        else:
                            pygame.mixer.music.load(sira[konum -1])
                            pygame.mixer.music.play(loops=0)
                            oynyazi.config(text=sira[konum - 1].split("/")[-1].replace(".mp3", ""))
                            kalanyazi.config(text=uznals(MP3(sira[konum - 1]).info.length))
                            oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                            ilerleme.config(state=NORMAL, to=MP3(sira[konum - 1]).info.length, value=0)
                            albumkapakuygula()
                            zamn = int(datetime.datetime.now().timestamp())
                            try:
                                RPC.update(details="Şarkı Dinliyor", state=sira[konum - 1].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")

                    else:
                        pygame.mixer.music.load(sira[0])
                        pygame.mixer.music.play(loops=0)
                        if oynatici["loop"] == "sira":
                            oynatici["konum"] = 0
                            pygame.mixer.music.load(sira[0])
                            pygame.mixer.music.play(loops=0)
                            oynyazi.config(text=sira[0].split("/")[-1].replace(".mp3", ""))
                            kalanyazi.config(text=uznals(MP3(sira[0]).info.length))
                            oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                            ilerleme.config(state=NORMAL, to=MP3(sira[0]).info.length, value=0)
                            albumkapakuygula()
                            zamn = int(datetime.datetime.now().timestamp())
                            try:
                                RPC.update(details="Şarkı Dinliyor", state=sira[0].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")
                        elif oynatici["loop"] == "gecerli":
                            pygame.mixer.music.load(sira[konum -1])
                            pygame.mixer.music.play(loops=0)
                            oynyazi.config(text=sira[konum - 1].split("/")[-1].replace(".mp3", ""))
                            kalanyazi.config(text=uznals(MP3(sira[konum - 1]).info.length))
                            oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                            ilerleme.config(state=NORMAL, to=MP3(sira[konum - 1]).info.length, value=0)
                            albumkapakuygula()
                            zamn = int(datetime.datetime.now().timestamp())
                            try:
                                RPC.update(details="Şarkı Dinliyor", state=sira[konum - 1].split("/")[-1].replace(".mp3", ""), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")
                        elif oynatici["loop"] == "kapali":
                            pygame.mixer.music.stop()
                            oynyazi.config(text=" ")
                            kalanyazi.config(text="00:00")
                            geritus.config(state=DISABLED)
                            ileritus.config(state=DISABLED)
                            ileritus.config(state=DISABLED)
                            karisiktus.config(state=DISABLED, image=karistirtuspng)
                            oynattus.config(state=DISABLED, command=oynat, image=oynattuspng)
                            looptus.config(state=DISABLED)
                            ilerleme.config(state=DISABLED, to=100, value=0)
                            albumkapak.config(image=albumkapakpng)
                            try:
                                RPC.update(details="Oynatıcıda", large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")
                except:
                    if not konum >= len(sira):
                        oynatici["konum"] = konum
                        print("Bu parça oynatılamıyor.")
                        ileri(klik=False)
                    else:
                        if not oynatici["loop"] == "kapali":
                            oynatici["konum"] = 0
                            ileri(klik=False)
                        else:
                            pygame.mixer.music.stop()
                            oynyazi.config(text=" ")
                            kalanyazi.config(text="00:00")
                            geritus.config(state=DISABLED)
                            ileritus.config(state=DISABLED)
                            ileritus.config(state=DISABLED)
                            karisiktus.config(state=DISABLED, image=karistirtuspng)
                            oynattus.config(state=DISABLED, command=oynat, image=oynattuspng)
                            looptus.config(state=DISABLED)
                            ilerleme.config(state=DISABLED, to=100, value=0)
                            albumkapak.config(image=albumkapakpng)
                            try:
                                RPC.update(details="Oynatıcıda", large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                            except:
                                print("dc yürümüyor.")


            def sec(bob, fnc=False):
                pygame.mixer.Sound.play(click)
                secim = sarkisecimi.get(tk.ACTIVE)
                if fnc:
                    secim = bob
                print(secim)
                
                if secim == "Spotify":
                    sarkisecimi.delete(0, tk.END)
                    oynatici["gecerlipath"] = f"{get_yol()}/Spotify"
                    gecerlipath = oynatici["gecerlipath"]
                    try:
                        klasörler = os.listdir(gecerlipath)
                    except:
                        klasörler = []
                    for klasör in klasörler:
                        if not klasör.endswith(".part"):
                            sarkisecimi.insert(tk.END, klasör.replace(".mp3", "   "))
                    sarkisecimi.insert(tk.END, ">Klasörde Göster")
                    sarkisecimi.insert(tk.END, ">Geri")
                elif secim == "YouTube":
                    sarkisecimi.delete(0, tk.END)
                    oynatici["gecerlipath"] = f"{get_yol()}/Sesler"
                    gecerlipath = oynatici["gecerlipath"]
                    try:
                        klasörler = os.listdir(gecerlipath)
                    except:
                        klasörler = []
                    for klasör in klasörler:
                        if not klasör.endswith(".part"):
                            sarkisecimi.insert(tk.END, klasör.replace(".mp3", "   "))
                    sarkisecimi.insert(tk.END, ">Klasörde Göster")
                    sarkisecimi.insert(tk.END, ">Geri")
                elif secim == ">Özel Klasörleri Düzenle":
                    def ekle():
                        pygame.mixer.Sound.play(click)
                        eklekaldirm.destroy()
                        sarkisecimi.focus_set()
                        print("Yeni Klasör Ekleniyor!")
                        dosyaadi = tk.filedialog.askdirectory(initialdir="/", title="Özel Müzik Klasörünüzü Seçiniz.")
                        pygame.mixer.Sound.play(click)
                        print('"' + dosyaadi + '"')
                        if not dosyaadi == "":
                            print("Özel Klasör Seçildi ve Ekleniyor.")
                            kpw = tk.Tk()
                            kpw.title("Özel Klasör Ekleme")
                            kpw.resizable(False, False)
                            kpw.iconbitmap("acemtubel.ico")
                            yer2 = str(kpw.winfo_screenwidth()/2 - 450/2).split(".")[0]
                            yer3 = str(kpw.winfo_screenheight()/2 - 300/2).split(".")[0]

                            def kapa():
                                pygame.mixer.Sound.play(click)
                                kpw.destroy()
                                root.attributes('-disabled', False)
                                root.wm_state('iconic')
                                root.wm_state('normal')

                            kpw.protocol("WM_DELETE_WINDOW", kapa)
                            kpw.geometry(f"450x300+{yer2}+{yer3}")
                            kpw.attributes("-alpha", seffaflik)
                            root.attributes('-disabled', True)
                            canvas = tk.Canvas(kpw, height=300, width=450, background=acikgri2)
                            canvas.pack()
                            emnk = tk.Frame(kpw, bg=arkaplan)
                            emnk1 = tk.Frame(kpw, bg=arkaplan)
                            emnk.place(relwidth=1, relheight=0.8, rely=0.2)
                            emnk1.place(relwidth=1, relheight=0.2)
                            emnb = tk.Label(emnk1, text=f"Özel Klasör İsmi", bg=acikyesil, fg=baslikyazirengi)
                            emnb.config(font=("Montserrat ExtraBold", "30", "italic"))

                            emnb.place(relwidth=1, relheight=0.9)

                            ckyazi = tk.Label(emnk, text=f"Lütfen Özel Klasörünüze Menüde Görünecek Bir İsim Verin.", bg=arkaplan, fg=yazirengi)
                            ckyazi.config(font=("Arial", "9"))
                            ckyazi.place(relwidth=1, relheight=0.2, rely=0.1)

                            ckyazi1 = tk.Label(emnk, text=f"", bg=arkaplan, fg=kirmiziyazi)
                            ckyazi1.config(font=("Arial", "14"))
                            ckyazi1.place(relwidth=1, relheight=0.15, rely=0.7)

                            giris3 = tk.Entry(emnk, width=7, bg=aramarengi, borderwidth=kenargenisligi, relief=stil, font=("Montserrat Medium", 20) , justify='center', fg=yazirengi)
                            giris3.pack(pady=80)
                            def epostabasla():
                                pygame.mixer.Sound.play(click)
                                temizkod = "".join(str(giris3.get()).split("-")).strip()

                                if temizkod != "":
                                    print("'" + dosyaadi + "' ,'" + temizkod + "' Adı ile Ekleniyor.")
                                    with open('data.json', 'r') as f:
                                        yzd = json.load(f)
                                    if not "ozelklasor" in yzd:
                                        yzd["ozelklasor"] = {}
                                    yzd["ozelklasor"][f"{temizkod}"] = str(dosyaadi)
                                    with open('data.json', 'w') as f:
                                        json.dump(yzd, f, indent=4)
                                    sarkisecimi.delete(0, tk.END)
                                    sarkisecimi.insert(tk.END, "Spotify")
                                    sarkisecimi.insert(tk.END, "YouTube")
                                    ozelklasorisimleri = customklasor().keys()
                                    for klasorisim in ozelklasorisimleri:
                                        sarkisecimi.insert(tk.END, klasorisim)
                                    sarkisecimi.insert(tk.END, ">Özel Klasörleri Düzenle")

                                    kpw.destroy()
                                    root.attributes('-disabled', False)
                                    root.wm_state('iconic')
                                    root.wm_state('normal')
                                else:

                                    ckyazi1.config(text="Lütfen Bir İsim Giriniz.")
                                    pygame.mixer.Sound.play(hata1)
                                    emnb.config(bg=kirmizi)

                            devamke = tk.Button(emnk, text=" Ekle! ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=epostabasla)
                            devamke.place(rely=0.55, relx=0.44)
                        else:
                            root.attributes('-disabled', False)
                    def kaldır():
                        pygame.mixer.Sound.play(click)
                        secim = klasorsecimi.get(tk.ACTIVE)
                        print(secim + " kaldır basıldı")
                        kaldirilcak = customklasor()
                        kaldirilanjson = kaldirilcak.pop(secim, None)
                        print(kaldirilanjson)
                        print(kaldirilcak)
                        
                        with open('data.json', 'r') as f:
                            kls = json.load(f)
                        kls[str(f"ozelklasor")] = kaldirilcak
                        with open('data.json', 'w') as f:
                            json.dump(kls, f, indent=4)

                        klasorsecimi.delete(0, tk.END)
                        ozelklasorisimler = customklasor().keys()
                        for klasorisim in ozelklasorisimler:
                            klasorsecimi.insert(tk.END, klasorisim)
                        sarkisecimi.delete(0, tk.END)
                        sarkisecimi.insert(tk.END, "Spotify")
                        sarkisecimi.insert(tk.END, "YouTube")
                        ozelklasorisimleri = customklasor().keys()
                        for klasorisim in ozelklasorisimleri:
                            sarkisecimi.insert(tk.END, klasorisim)
                        sarkisecimi.insert(tk.END, ">Özel Klasörleri Düzenle")
                    def bas(naber=None):
                        secim = klasorsecimi.get(tk.ACTIVE)
                        exyol = customklasor()[secim].replace("/", "\\")
                        print(exyol)
                        subprocess.Popen(f'explorer "{exyol}"')
                        pygame.mixer.Sound.play(click)

                    eklekaldirm = tk.Tk()
                    eklekaldirm.title("Özel Klasör Ekleme")
                    eklekaldirm.resizable(False, False)
                    eklekaldirm.iconbitmap("acemtubel.ico")
                    yer2 = str(eklekaldirm.winfo_screenwidth()/2 - 450/2).split(".")[0]
                    yer3 = str(eklekaldirm.winfo_screenheight()/2 - 300/2).split(".")[0]

                    def kapa():
                        pygame.mixer.Sound.play(click)
                        eklekaldirm.destroy()
                        root.attributes('-disabled', False)
                        root.wm_state('iconic')
                        root.wm_state('normal')
                        sarkisecimi.focus_set()

                    eklekaldirm.protocol("WM_DELETE_WINDOW", kapa)
                    eklekaldirm.geometry(f"450x300+{yer2}+{yer3}")
                    eklekaldirm.attributes("-alpha", seffaflik)
                    root.attributes('-disabled', True)
                    canvas = tk.Canvas(eklekaldirm, height=300, width=450, background=acikgri2)
                    canvas.pack()
                    emnk = tk.Frame(eklekaldirm, bg=arkaplan)
                    emnk1 = tk.Frame(eklekaldirm, bg=arkaplan)
                    emnk.place(relwidth=1, relheight=0.8, rely=0.2)
                    emnk1.place(relwidth=1, relheight=0.2)
                    emnb = tk.Label(emnk1, text=f"Özel Klasörleri Düzenle", bg=acikyesil, fg=baslikyazirengi)
                    emnb.config(font=("Montserrat ExtraBold", "25", "italic"))

                    emnb.place(relwidth=1, relheight=0.9)

                    ckyazi = tk.Label(emnk, text=f"Bu Menüden Kendi Müzik Klasörlerinizi Ekleyebilir/Kaldırabilirsiniz.", bg=arkaplan, fg=yazirengi)
                    ckyazi.config(font=("Arial", "9"))
                    ckyazi.place(relwidth=1, relheight=0.2, rely=0.01)

                    klasorsecimi = tk.Listbox(emnk, bg=arkaplan, fg=yazirengi, width=60, height=6, bd=0, activestyle="none", selectbackground=acikyesil)
                    klasorsecimi.pack(pady=43)
                    klasorsecimi.bind('<Double-Button>', bas)
                    klasorsecimi.bind('<Return>', bas)
                    ozelklasorisimler = customklasor().keys()
                    for klasorisim in ozelklasorisimler:
                        klasorsecimi.insert(tk.END, klasorisim)
                        

                    devamke = tk.Button(emnk, text="   Ekle   ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ekle)
                    devamke.place(rely=0.65, relx=0.3)
                    kaldirbuton = tk.Button(emnk, text=" Kaldır ", padx=10, pady=5, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kaldır)
                    kaldirbuton.place(rely=0.65, relx=0.55)

                elif secim == ">Klasörde Göster":
                    print(oynatici["gecerlipath"])
                    #if not oynatici["gecerlipath"] == "Spotify" and not oynatici["gecerlipath"] == "YouTube":
                    exyol = oynatici["gecerlipath"].replace("/", "\\")
                    subprocess.Popen(f'explorer "{exyol}"')
                elif secim in customklasor():
                    sarkisecimi.delete(0, tk.END)
                    oynatici["gecerlipath"] = customklasor()[f"{secim}"]
                    gecerlipath = oynatici["gecerlipath"]
                    try:
                        klasörler = os.listdir(gecerlipath)
                    except:
                        klasörler = []
                    for klasör in klasörler:
                        if not klasör.endswith(".part"):
                            sarkisecimi.insert(tk.END, klasör.replace(".mp3", "   "))
                    sarkisecimi.insert(tk.END, ">Klasörde Göster")
                    sarkisecimi.insert(tk.END, ">Geri")
                elif secim[-3:] == "   ":
                    print("oynat")
                    yol = oynatici["gecerlipath"] + "/"
                    sira = []
                    konum = 0
                    bulundu = False
                    karistir = 0
                    sarklar = []
                    
                    #sarkiorganize
                    siralamadict = {}
                    olmayanlar = []
                    try:
                        klasörler = os.listdir(yol.replace("//", "/"))
                    except:
                        klasörler = []
                    for dosya in klasörler:
                        if dosya.endswith(".mp3"):
                            dosnum = eyed3.load(oynatici["gecerlipath"] + "/" + dosya).tag.track_num[0]

                            if not str(dosnum) in siralamadict and not dosnum == None and not dosnum == "None":
                                siralamadict[str(eyed3.load(oynatici["gecerlipath"] + "/" + dosya).tag.track_num[0])] = dosya
                            else:
                                olmayanlar.append(dosya)
                        else:
                            olmayanlar.append(dosya)
                    
                    
                    #print(siralamadict)
                    #print(olmayanlar)
                    intglist = []

                    for key in siralamadict.keys():
                        intglist.append(int(key))

                    try:
                        sınır = max(intglist)
                    except:
                        sınır = 0
                    
                    print(sınır)
                    metalı = []
                    
                    dongsayi = 1
                    while True:
                        if not sınır == 0:
                            try:
                                dosy = siralamadict[str(dongsayi)]
                            except:
                                if not dongsayi == sınır:
                                    dongsayi += 1
                                    continue
                                else:
                                    break
                            #print(dosy)
                            metalı.append(dosy)
                            if not dongsayi == sınır:
                                dongsayi += 1
                            else:
                                break
                        else:
                            break

                    eklenecek = metalı + olmayanlar
                    for olmayan in eklenecek:
                        sarklar.append(olmayan)

                    for sarki in sarklar:
                        
                        sira.append(yol.replace("//", "/") + sarki)
                        if sarki == secim.replace("   ", ".mp3"):
                                bulundu = True

                        if not bulundu:
                           konum += 1


                        #    print(sira)
                        #    print(sira[konum])
                        #print(konum)

                    #print(sira)
                    #print(sira[konum])
                    oynatici["sira"] = sira
                    oynatici["konum"] = konum
                    oynatici["karistir"] = karistir
                    oynatici["oynatildi"] = 0
                    pygame.mixer.music.load(yol.replace("//", "/") + secim.replace("   ", ".mp3"))
                    pygame.mixer.music.play(loops=0)
                    oynyazi.config(text=secim.rstrip())
                    kalanyazi.config(text=uznals(MP3(yol.replace("//", "/") + secim.replace("   ", ".mp3")).info.length))
                    geritus.config(state=NORMAL)
                    ileritus.config(state=NORMAL)
                    oynattus.config(state=NORMAL, command=durdur, image=durdurtuspng)
                    karisiktus.config(state=NORMAL, image=karistirtuspng)
                    looptus.config(state=NORMAL)
                    ilerleme.config(state=NORMAL, to=MP3(yol.replace("//", "/") + secim.replace("   ", ".mp3")).info.length, value=0)
                    albumkapakuygula()
                    zamn = int(datetime.datetime.now().timestamp())
                    try:
                        RPC.update(details="Şarkı Dinliyor", state=secim.rstrip(), start=zamn, large_image="acemtubedc", small_image="kulaklik", small_text="Spotify Liste/Albüm/Parçalarını .mp3 Halinde İndirebilirsiniz!", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                    except:
                        print("dc yürümüyor.")


                elif secim == ">Geri":
                    sarkisecimi.delete(0, tk.END)
                    suan = oynatici["gecerlipath"]
                    #if suan.endswith("/"):
                    #    suan = list(suan)[:1]
                    gecerlipath = suan.replace(oynatici["gecerlipath"].split("/")[-1], "").replace("//", "/")
                    print(gecerlipath)
                    print(get_yol())
                    olasidirisimler = customklasor().keys()
                    olasidirler = []
                    for olsdir in olasidirisimler:
                        olasidirler.append(customklasor()[olsdir].replace(oynatici["gecerlipath"].split("/")[-1], "").replace("//", "/"))

                    if gecerlipath != get_yol() and gecerlipath != get_yol() + "/" and gecerlipath  + "/" != get_yol() and gecerlipath not in olasidirler:
                        if gecerlipath.endswith("/"):
                            gecerlipath = "".join(list(gecerlipath)[:-1])

                        oynatici["gecerlipath"] = gecerlipath
                        try:
                            klasörler = os.listdir(gecerlipath)
                        except:
                            klasörler = []

                        sarkisecimi.delete(0, tk.END)
                        siralamadict = {}
                        olmayanlar = []
                        for dosya in klasörler:
                            if dosya.endswith(".mp3"):
                                dosnum = eyed3.load(oynatici["gecerlipath"] + "/" + dosya).tag.track_num[0]
                                #print(dosnum)
                                if not str(dosnum) in siralamadict and not dosnum == None and not dosnum == "None":
                                    siralamadict[str(eyed3.load(oynatici["gecerlipath"] + "/" + dosya).tag.track_num[0])] = dosya
                                else:
                                    olmayanlar.append(dosya)
                            else:
                                olmayanlar.append(dosya)
                        
                        
                        #print(siralamadict)
                        #print(olmayanlar)
                        intglist = []

                        for key in siralamadict.keys():
                            intglist.append(int(key))

                        try:
                            sınır = max(intglist)
                        except:
                            sınır = 0
                        
                        print(sınır)
                        metalı = []
                        
                        dongsayi = 1
                        while True:
                            if not sınır == 0:
                                try:
                                    dosy = siralamadict[str(dongsayi)]
                                except:
                                    if not dongsayi == sınır:
                                        dongsayi += 1
                                        continue
                                    else:
                                        break
                                #print(dosy)
                                metalı.append(dosy)
                                if not dongsayi == sınır:
                                    dongsayi += 1
                                else:
                                    break
                            else:
                                break

                        eklenecek = metalı + olmayanlar
                        for olmayan in eklenecek:
                            if not olmayan.endswith(".part") and not olmayan.endswith(".m4a"):
                                sarkisecimi.insert(tk.END, olmayan.replace(".mp3", "   "))
                        sarkisecimi.insert(tk.END, ">Klasörde Göster")
                        sarkisecimi.insert(tk.END, ">Geri")
                    else:
                        sarkisecimi.delete(0, tk.END)
                        sarkisecimi.insert(tk.END, "Spotify")
                        sarkisecimi.insert(tk.END, "YouTube")
                        ozelklasorisimleri = customklasor().keys()
                        for klasorisim in ozelklasorisimleri:
                            sarkisecimi.insert(tk.END, klasorisim)
                        sarkisecimi.insert(tk.END, ">Özel Klasörleri Düzenle")
                else:
                    eskigecerlipath = oynatici["gecerlipath"]
                    oynatici["gecerlipath"] = oynatici["gecerlipath"] + "/" + secim
                    gecerlipath = oynatici["gecerlipath"]
                    dirdegil = False
                    try:
                        klasörler = os.listdir(gecerlipath)
                    except NotADirectoryError:
                        dirdegil = True
                    if not dirdegil:
                        sarkisecimi.delete(0, tk.END)
                        siralamadict = {}
                        olmayanlar = []
                        for dosya in klasörler:
                            if dosya.endswith(".mp3"):
                                dosnum = eyed3.load(oynatici["gecerlipath"] + "/" + dosya).tag.track_num[0]
                                #print(dosnum)
                                if not str(dosnum) in siralamadict and not dosnum == None and not dosnum == "None":
                                    siralamadict[str(eyed3.load(oynatici["gecerlipath"] + "/" + dosya).tag.track_num[0])] = dosya
                                else:
                                    olmayanlar.append(dosya)
                            else:
                                olmayanlar.append(dosya)
                        
                        
                        #print(siralamadict)
                        #print(olmayanlar)
                        intglist = []

                        for key in siralamadict.keys():
                            intglist.append(int(key))

                        try:
                            sınır = max(intglist)
                        except:
                            sınır = 0
                        
                        print(sınır)
                        metalı = []
                        
                        dongsayi = 1
                        while True:
                            if not sınır == 0:
                                try:
                                    dosy = siralamadict[str(dongsayi)]
                                except:
                                    if not dongsayi == sınır:
                                        dongsayi += 1
                                        continue
                                    else:
                                        break
                                #print(dosy)
                                metalı.append(dosy)
                                if not dongsayi == sınır:
                                    dongsayi += 1
                                else:
                                    break
                            else:
                                break

                        eklenecek = metalı + olmayanlar
                        for olmayan in eklenecek:
                            if not olmayan.endswith(".part") and not olmayan.endswith(".m4a"):
                                sarkisecimi.insert(tk.END, olmayan.replace(".mp3", "   "))
                        sarkisecimi.insert(tk.END, ">Klasörde Göster")
                        sarkisecimi.insert(tk.END, ">Geri")
                    else:
                        print("Bu bir klasör değil!")
                        oynatici["gecerlipath"] = eskigecerlipath
            def karistir():
                pygame.mixer.Sound.play(click)
                if oynatici["karistir"] == 0:
                    print("Sıra Karıştırılıyor...")
                    şuankişarkı = oynatici["sira"][oynatici["konum"]]
                    print(şuankişarkı)
                    normalkonum = oynatici["konum"]
                    normalsira = oynatici["sira"]
                    print(normalsira)
                    print("Konum: "+ str(normalkonum))

                    oynatici["normsira"] = normalsira
                    oynatici["normkonum"] = normalkonum
                    karisik = []
                    karistirilan = random.sample(normalsira, len(normalsira))
                    karisik.append(şuankişarkı)
                    karistirilan.remove(şuankişarkı)
                    #print(karisik_sira)
                    print("_______________________")
                    oynatici["sira"] = karisik + karistirilan
                    print(oynatici["sira"]) 

                    oynatici["konum"] = 0
                    oynatici["karistir"] = 1
                    karisiktus.config(image=karisiktuspng)
                else:
                    normallestirilecek = oynatici["normsira"]
                    karisik_olan = oynatici["sira"]
                    gecerliolankonum = oynatici["konum"]
                    gecerliolan = karisik_olan[gecerliolankonum]
                    print(gecerliolan)
                    yeni = []
                    eskiolmayan = []
                    sayi = -1
                    for sark in normallestirilecek:
                        sayi += 1
                        if sark == gecerliolan:
                            oynatici["konum"] = sayi
                            print("Geçerli şarkının konumu: " + str(sayi))
                            break
                        
                    oynatici["sira"] = normallestirilecek
                    oynatici["karistir"] = 0
                    
                    karisiktus.config(image=karistirtuspng)

            def loopayr():
                pygame.mixer.Sound.play(click)
                if oynatici["loop"] == "sira":
                    looptus.config(image=loop1png)
                    oynatici["loop"] = "gecerli"
                elif oynatici["loop"] == "gecerli":
                    looptus.config(image=looptuspng)
                    oynatici["loop"] = "kapali"
                elif oynatici["loop"] == "kapali":
                    looptus.config(image=loopgpng)
                    oynatici["loop"] = "sira"

            geritus = tk.Button(tuscercevesi, image=gerituspng, borderwidth=0, bg=arkaplan, command=geri, activebackground=arkaplan)
            geritus.image = gerituspng
            oynattus = tk.Button(tuscercevesi, image=oynattuspng, borderwidth=0, bg=arkaplan, command=oynat, activebackground=arkaplan)
            oynattus.image = oynattuspng
            ileritus = tk.Button(tuscercevesi, image=ilerituspng, borderwidth=0, bg=arkaplan, command=ileri, activebackground=arkaplan)
            ileritus.image = ilerituspng
            karisiktus = tk.Button(tuscercevesi, image=karistirtuspng, borderwidth=0, bg=arkaplan, command=karistir, activebackground=arkaplan)
            karisiktus.image = karistirtuspng
            looptus = tk.Button(tuscercevesi, image=loopgpng, borderwidth=0, bg=arkaplan, command=loopayr, activebackground=arkaplan)
            looptus.image = looptuspng
            mutetus = tk.Button(baslikutu1, image=unmutepng, borderwidth=0, bg=arkaplan, command=mutefunc, activebackground=arkaplan)
            mutetus.image = unmutepng
            albumkapak = tk.Label(baslikutu1, image=albumkapakpng, bg=arkaplan ,fg=acikgri2)
            albumkapak.image = albumkapakpng

            def oynatabas(bob=None):
                oynattus.invoke()

            def ileritusabas(bob=None):
                ileritus.invoke()
            def geritusabas(bob=None):
                geritus.invoke()
            def sonusec(bob):
                sec(">Geri", fnc=True)
            def tuss(tus):
                print(tus)

            sarkisecimi.bind('<Double-Button>', sec)
            sarkisecimi.bind('<Return>', sec)
            sarkisecimi.bind('<space>', oynatabas)
            sarkisecimi.bind('<BackSpace>', sonusec)
            sarkisecimi.bind('<Escape>', sonusec)
            sarkisecimi.bind('<XF86AudioPlay>', oynatabas)
            sarkisecimi.bind('<XF86AudioNext>', ileritusabas)
            sarkisecimi.bind('<XF86AudioPrev>', geritusabas)

            #ilerleme.grid(row=0, column=2, pady=10)

            karisiktus.grid(row=0, column=0, padx = 2)
            geritus.grid(row=0, column=1, padx = 10)
            oynattus.grid(row=0, column=2, padx=10)
            ileritus.grid(row=0, column=3, padx=10)
            looptus.grid(row=0, column=4, padx=2)

            mutetus.place(relx=0.387, rely=0.936)
            sesyzd.place(relwidth=0.05, relheight=0.05, rely=0.926, relx=0.58)
            albumkapak.place(relx=0.56, rely=0.085)
            geritus.config(state=DISABLED)
            ileritus.config(state=DISABLED)
            oynattus.config(state=DISABLED)
            karisiktus.config(state=DISABLED)
            looptus.config(state=DISABLED)
            ilerleme.config(state=DISABLED)

            #geritus.pack(pady= 4)

            def cikis():

                pygame.mixer.Sound.play(click)
                pygame.mixer.Sound.play(hata)
                root.attributes('-disabled', True)

                def anan():
                    print("anan")
                print("kapatıldım aq")
                kpw = tk.Tk()
                kpw.title("Emin Misiniz?")
                kpw.resizable(False, False)
                kpw.iconbitmap("acemtubered.ico")
                kpw.protocol("WM_DELETE_WINDOW", anan)
                yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
                yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
                kpw.geometry(f"400x150+{yer2}+{yer3}")
                kpw.attributes("-alpha", seffaflik)
                canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
                canvas.pack()
                emnk = tk.Frame(kpw, bg=arkaplan)
                emnk1 = tk.Frame(kpw, bg=arkaplan)
                emnk.place(relwidth=1, relheight=0.7, rely=0.3)
                emnk1.place(relwidth=1, relheight=0.3)
                emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
                emnb.config(font=("Montserrat ExtraBold", "30", "italic"))

                emnb.place(relwidth=1, relheight=0.9)

                ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=arkaplan, fg=yazirengi)
                ckyazi.config(font=("Montserrat Medium", "9"))
                ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
                def cikiss():
                    pygame.mixer.Sound.play(click)
                    pygame.mixer.music.fadeout(1000)
                    try:
                       RPC.close()
                    except:
                        print("discord yürütülmeimş")
                    
                    subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                    root.destroy()
                    kpw.destroy()
                    exit(0)
                def gri():
                    pygame.mixer.Sound.play(click)
                    root.attributes('-disabled', False)
                    kpw.destroy()

                cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
                cikıss.place(rely=0.5, relx= 0.25)
                anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
                anamenuu.place(rely=0.5, relx= 0.57)

                kpw.mainloop()

            def anamenu():
                pygame.mixer.Sound.play(click)

                print("anamenu basıldı")
                baslikutu.destroy()
                baslikutu1.destroy()
                ilkbaslangic(anamenu=1)
            def sessizilerif():
                ileri(klik=False)
            cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
            cikıs.place(rely=0.87, relx= 0.89)
            anamenu = tk.Button(baslikutu1, text=" Ana Menü ", padx=0, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=anamenu)
            anamenu.place(rely=0.8, relx= 0.89)
            sessizileri = tk.Button(baslikutu1, text="", padx=0, pady=0, foreground=arkaplan, bg=arkaplan, activebackground=arkaplan, activeforeground=arkaplan, highlightbackground=arkaplan, borderwidth=0, relief=tk.RAISED, command=sessizilerif)
            sessizileri.place(rely=1, relx= 1)

            
            def sarkison():
                print("Şarkı Sonu Eventi İzleniyor..")
                SONG_END = pygame.USEREVENT + 1
                pygame.mixer.music.set_endevent(SONG_END)
                def medialis():
                    def klvyebuton(key):
                        if key == keyboard.Key.media_play_pause:
                            oynattus.invoke()
                        elif key == keyboard.Key.media_next:
                            ileritus.invoke()
                        elif key == keyboard.Key.media_previous:
                            geritus.invoke()
                    with keyboard.Listener(on_press=klvyebuton) as listener:
                        listener.join()

                keythread = threading.Thread(target=medialis)
                keythread.start()

                while True:                    
                    time.sleep(0.01)
                    if sessizileri.winfo_exists() == 1:
                        try:
                            for event in pygame.event.get():
                                if event.type == SONG_END:
                                    #print("Şarkı Bitti!")
                                    sessizileri.invoke()
                        except Exception as e:
                            print(e)
                            break
                    else:
                        print("Oynatıcı Kapatıldı.")
                        break
                    

            sth = threading.Thread(target=sarkison)
            sth.start()
            
        else:
            anamenures.invoke()
  


    def dce():
        pygame.mixer.Sound.play(click)
        webbrowser.open(dclink)

    def dceb():
        pygame.mixer.Sound.play(click)
        webbrowser.open("https://acemtube.glitch.me/")

    def yout():
        pygame.mixer.Sound.play(click)
        webbrowser.open("https://youtube.com/c/acem8887")

    def eng():
        pygame.mixer.Sound.play(click)
        print("english basıldı")
        engils.destroy()
        webbrowser.open(dclink)
        disc.place(rely=0.5, relx= 0.1)
        discb.place(rely=0.5, relx= 0.4)
        engil.place(rely=0.5, relx= 0.7)
        baslik.destroy()
        likbaslik = tk.Label(baslikutu, text=f"English", bg=acikyesil, fg=yazirengi)
        likbaslik.config(font=("Montserrat Medium", "24"))
        likbaslik.place(relwidth=1, relheight=1)
        yakyazi = tk.Label(baslikutu1, text=f"Bu özellik yakında eklenecek. Gelişmeleri takip etmek için sunucumuza gelebilirsin!", bg=acikgri2, fg=yazirengi)
        yakyazi.config(font=("Montserrat Medium", "12"))
        yakyazi.place(relwidth=1, relheight=0.1, rely=0.2)
        ses.destroy()
        video.destroy()
        spotify.destroy()
        ayarlar.destroy()
        hkd.destroy()
        def cikis():
            pygame.mixer.Sound.play(click)
            pygame.mixer.Sound.play(hata)
            root.attributes('-disabled', True)
            
            def anan():
                print("anan")
            print("kapatıldım aq")
            kpw = tk.Tk()
            kpw.title("Emin Misiniz?")
            kpw.resizable(False, False)
            kpw.iconbitmap("acemtubered.ico")
            kpw.protocol("WM_DELETE_WINDOW", anan)
            yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
            yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
            kpw.geometry(f"400x150+{yer2}+{yer3}")
            kpw.attributes("-alpha", seffaflik)
            canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
            canvas.pack()
            emnk = tk.Frame(kpw, bg=acikgri2)
            emnk1 = tk.Frame(kpw, bg=acikgri2)
            emnk.place(relwidth=1, relheight=0.7, rely=0.3)
            emnk1.place(relwidth=1, relheight=0.3)
            emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=yazirengi)
            emnb.config(font=("Montserrat ExtraBold", "30", "italic"))
    
            emnb.place(relwidth=1, relheight=0.9)
            
            ckyazi = tk.Label(emnk, text=f"AcemTube Uygulamasından Çıkmak\nİstediğinizden Emin Misiniz?", bg=acikgri2, fg=yazirengi)
            ckyazi.config(font=("Montserrat Medium", "9"))
            ckyazi.place(relwidth=1, relheight=0.32, rely=0.08)
            def cikiss():
                pygame.mixer.Sound.play(click)
                try:
                   RPC.close()
                except:
                    print("discord yürütülmeimş")
                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                root.destroy()
                kpw.destroy()
                exit(0)
            def gri():
                pygame.mixer.Sound.play(click)
                root.attributes('-disabled', False)
                kpw.destroy()
    
            cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, command=cikiss)
            cikıss.place(rely=0.5, relx= 0.25)
            anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, command=gri)
            anamenuu.place(rely=0.5, relx= 0.57)
            kpw.mainloop()

        def anamenu():
            pygame.mixer.Sound.play(click)
            print("anamenu basıldı")
            baslikutu.destroy()
            baslikutu1.destroy()
            ilkbaslangic(anamenu=1)
        
        cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, command=cikis)
        cikıs.place(rely=0.87, relx= 0.89)
        anamenu = tk.Button(baslikutu1, text=" Ana Menü ", padx=0, pady=1, foreground=yazirengi, bg=koyugri, command=anamenu)
        anamenu.place(rely=0.8, relx= 0.89)

        cıkıs.destroy()

    
    global canvas
    canvas = tk.Canvas(root, height=510, width=740, background=acikgri2)
    canvas.pack()
    
    baslikutu = tk.Frame(root, bg=acikmavi)
    baslikutu.place(relwidth=1, relheight=0.1)
    
    baslikutu1 = tk.Frame(root, bg=arkaplan)
    baslikutu1.place(relwidth=1, relheight=0.9, rely=0.1)

    def programk():
        root.attributes('-disabled', True)
        pygame.mixer.Sound.play(click)
        pygame.mixer.Sound.play(hata)
        def anan():
            print("anan")
            
        print("kapatıldım aq")
        kpw = tk.Tk()
        kpw.title("Emin Misiniz?")
        kpw.resizable(False, False)
        kpw.iconbitmap("acemtubered.ico")
        kpw.protocol("WM_DELETE_WINDOW", anan)
        yer2 = str(kpw.winfo_screenwidth()/2 - 400/2).split(".")[0]
        yer3 = str(kpw.winfo_screenheight()/2 - 150/2).split(".")[0]
        kpw.geometry(f"400x150+{yer2}+{yer3}")
        kpw.attributes("-alpha", seffaflik)
        canvas = tk.Canvas(kpw, height=150, width=400, background=acikgri2)
        canvas.pack()
        emnk = tk.Frame(kpw, bg=arkaplan)
        emnk1 = tk.Frame(kpw, bg=arkaplan)
        emnk.place(relwidth=1, relheight=0.7, rely=0.3)
        emnk1.place(relwidth=1, relheight=0.3)
        emnb = tk.Label(emnk1, text=f"Emin Misiniz?", bg=kirmizi, fg=baslikyazirengi)
        emnb.config(font=("Montserrat ExtraBold", "30", "italic"))

        emnb.place(relwidth=1, relheight=0.9)
        
        ckyazi = tk.Label(emnk, text=f"Herhangi Bir Devam Eden İşlem İptal Edilecektir.", bg=arkaplan, fg=yazirengi)
        ckyazi.config(font=("Montserrat Medium", "9"))
        ckyazi.place(relwidth=1, relheight=0.15, rely=0.2)
        def cikis():
            pygame.mixer.Sound.play(click)
            try:
               RPC.close()
            except:
                print("discord yürütülmeimş")
            subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
            root.destroy()
            kpw.destroy()
            exit(0)
        def gri():
            pygame.mixer.Sound.play(click)
            root.attributes('-disabled', False)
            kpw.destroy()

        cikıss = tk.Button(emnk, text=" Çıkış ", padx=15, pady=1, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
        cikıss.place(rely=0.5, relx= 0.25)
        anamenuu = tk.Button(emnk, text=" Vazgeç ", padx=11, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=gri)
        anamenuu.place(rely=0.5, relx= 0.57)
        kpw.mainloop()
        
    root.protocol("WM_DELETE_WINDOW", programk)

    baslik = tk.Label(baslikutu, text=f"AcemTube", bg=acikmavi, fg=baslikyazirengi)
    baslik.config(font=("Montserrat ExtraBold", "30", "italic"))
    baslik.place(relwidth=1, relheight=0.9)
    if not offline_modu: 
        if cevap == "7" or "[7]-" in cevap:
            baslik.config(text="AcemTube Free")
    else:
        baslik.config(text="AcemTube Offline")
        

    upd = tk.Label(baslikutu1, text=altyazi, bg=arkaplan, fg=yazirengi)
    upd.config(font=("Arial", "8"))
    upd.place(relwidth=0.13, relheight=0.05, rely=0.95)
    altlik = tk.Label(baslikutu1, text=f"      Versiyon : {version} By Acem", bg=arkaplan, fg=yazirengi)
    altlik.config(font=("Arial", "7"))
    altlik.place(relwidth=0.2, relheight=0.05, rely=0.95, relx=0.8)

    def uyarı():
        spotify.config(state=DISABLED)
        uyrkutu = tk.Frame(root, bg=turuncu)
        uyrkutu.place(relwidth=1, relheight=0.1, rely=0.9)
        uyaru = tk.Label(uyrkutu, text=f"UYARI: SPOTIFY İNDİRME ÖZELLİĞİ KISA SÜRELİĞİNE DEVRE DIŞI BIRAKILMIŞTIR. EN YAKIN ZAMANDA YENİ GÜNCELLEME İLE DÜZELTİLECEKTİR.", bg="#ff7b00", fg=baslikyazirengi)
        uyaru.config(font=("Montserrat Medium", "6", "bold"))
        uyaru.place(relwidth=1, relheight=1)
        pygame.mixer.Sound.play(hata)
        ses.place(rely=0.12, relx= 0.107)
        video.place(rely=0.12, relx= 0.407)
        spotify.place(rely=0.12, relx= 0.707)
        ayarlar.place(rely=0.52, relx= 0.407)
        hkd.place(rely=0.52, relx= 0.107)
        cıkıs.place(rely=0.52, relx= 0.707)
    
    #anamenü butonları
    ses = tk.Button(baslikutu1, text=" Ses ", padx=60, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=ses).start)
    ses.place(rely=0.15, relx= 0.107)

    video = tk.Button(baslikutu1, text=" Video ", padx=50, pady=50, foreground=yazirengi, bg=koyugri,activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=video).start)
    video.place(rely=0.15, relx= 0.407)

    #threading.Thread(target=spotify).start

    spotify = tk.Button(baslikutu1, text=" Spotify ", padx=45, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=spotify)
    spotify.place(rely=0.15, relx= 0.707)
    #spotify kapat

    #spotify.config(state=DISABLED)
    
    def get_yolst():
        with open('data.json', 'r') as f:
            yol = json.load(f)
        if "kayit_yolu" in yol:
            if not yol["kayit_yolu"] == "":
                return yol["kayit_yolu"]
            else:
                return "Yok"
        else:
            return "Yok"

    ayarlar = tk.Button(baslikutu1, text=" Ayarlar ", padx=46, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=ayarlar).start)
    ayarlar.place(rely=0.55, relx= 0.407)

    hkd = tk.Button(baslikutu1, text=" Oynatıcı ", padx=44, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=mp3oynatici).start)
    hkd.place(rely=0.55, relx= 0.107)

    cıkıs = tk.Button(baslikutu1, text=" Çıkış ", padx=51, pady=50, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cıkıs)
    cıkıs.place(rely=0.55, relx= 0.707)

    disc = tk.Button(baslikutu1, text=" Discord Sunucumuz ", padx=16, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dce)
    #disc.place(rely=0.83, relx= 0.107)

    discb = tk.Button(baslikutu1, text="AcemTube Websitesi", padx=17.8, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dceb)
    #discb.place(rely=0.83, relx= 0.407)

    engil = tk.Button(baslikutu1, text=" Youtube Kanalımız ", padx=14, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=yout)
    #engil.place(rely=0.83, relx= 0.707)

    engils = tk.Button(baslikutu1, text=" English (Soon) ", padx=252, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=eng)
    #engils.place(rely=0.83, relx= 0.107)

    if offline_modu:
        ses.config(state=DISABLED)
        video.config(state=DISABLED)
        spotify.config(state=DISABLED)

    try:
        if verakt == "2":
            global verkutu
            verkutu = tk.Frame(root, bg=turuncu)
            verkutu.place(relwidth=1, relheight=0.1, rely=0.9)
            ses.place(rely=0.12, relx= 0.107)
            video.place(rely=0.12, relx= 0.407)
            spotify.place(rely=0.12, relx= 0.707)
            ayarlar.place(rely=0.52, relx= 0.407)
            hkd.place(rely=0.52, relx= 0.107)
            cıkıs.place(rely=0.52, relx= 0.707)
            sescik = tk.Label(verkutu, text=f"Yeni Güncelleme Mevcut! ({guncelsurumadi}) Güncellemeleri Al Ekranından Hemen İndirebilirsiniz! Geçerli Sürüm: ({version})", bg="#ff7b00", fg=baslikyazirengi)
            sescik.config(font=("Montserrat Medium", "8", "bold"))
            sescik.place(relwidth=1, relheight=1)
            pygame.mixer.Sound.play(hata)
    except:
        print("bruh")
   
    if get_yolst() == "Yok":
        ayarlar.invoke()
        
    if anamenu == 3:
        hkd.invoke()
    root.mainloop()
def hebe():
    def hbbasla():
        def kld_get():
            with open('data.json', 'r') as f:
                klad = json.load(f)
            if "kullanici_adi" in klad:
                return klad["kullanici_adi"]
            else:
                return "yok"

        def sif_get():
            with open('data.json', 'r') as f:
                klad = json.load(f)
            if "kullanici_parola" in klad:
                return klad["kullanici_parola"]
            else:
                return "yok"

        def get_krlm():
            with open('data.json', 'r') as f:
                yol = json.load(f)
            if "krlm_chk" in yol:
                return yol["krlm_chk"]
            else:
                return 0

        def kurulumchk():
            with open('data.json', 'r') as f:
                yzd = json.load(f)
            yzd[str(f"yuzde")] += 7.142857142857143
            with open('data.json', 'w') as f:
                json.dump(yzd, f, indent=4)
            if get_krlm() == 0 and not offline_modu:
                try:
                    RPC.update(details="Kurulum Yapıyor", start=zmn, state="İlk Aşamada",large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("discord yürümüyor.")
                actsupdater.acts_guncelle(bitir=True)

                lisans2 = tk.Tk()
                lisans2.title(f"AcemTube Kurulum")
                lisans2.iconbitmap("acemtubesetup.ico")
                yer = str(lisans2.winfo_screenwidth()/2 - 750/2).split(".")[0]
                yer1 = str(lisans2.winfo_screenheight()/2 - 510/2).split(".")[0]
                lisans2.geometry(f"750x510+{yer}+{yer1}")
                lisans2.attributes("-alpha", seffaflik)
                licanvas2 = tk.Canvas(lisans2, height=510, width=750, background=acikgri2)
                licanvas2.pack()
                lisans2.resizable(False, False)

                baslikutu2 = tk.Frame(lisans2, bg=acikmavi)
                baslikutu2.place(relwidth=1, relheight=0.1)
                baslikutu3 = tk.Frame(lisans2, bg=arkaplan)
                baslikutu3.place(relwidth=1, relheight=0.9, rely=0.1)

                basarili = tk.Label(baslikutu2, text=f"İlk Kurulum", bg=acikmavi, fg=yazirengi)
                basarili.config(font=("Montserrat ExtraBold", "30", "italic"))
                basarili.place(relwidth=1, relheight=0.9)
                def kuraq():
                    pygame.mixer.Sound.play(click)
                    print("ok kuruom")
                    sism.destroy()
                    sism1.destroy()
                    deq.destroy()
                    basarili.destroy()
                    progyaz = tk.Label(baslikutu2, text=f"İndiriliyor...", bg=acikmavi, fg=yazirengi)
                    progyaz.config(font=("Montserrat ExtraBold", "30", "italic"))
                    progyaz.place(relwidth=1, relheight=1)
                    progyazi = tk.Label(baslikutu3, text=f"Gereken Bileşenler İndiriliyor", bg=arkaplan, fg=yazirengi)
                    progyazi.config(font=("Montserrat Medium", "12"))
                    progyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                    s = ttk.Style()
                    s.theme_use("clam")
                    s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
                    prgs1 = ttk.Progressbar(baslikutu3, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
                    prgs1.place(relx=0.265, rely=0.2)
                    time.sleep(1)
                    prgs1['value'] += 10
                    subprocess.run("powershell.exe -ExecutionPolicy RemoteSigned \"Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')\"", shell=True)
                    prgs1['value'] += 80
                    subprocess.call("scoop update", shell=True)
                    prgs1['value'] += 100
                    time.sleep(2)
                    progyaz.destroy()
                    progyazi.destroy()
                    pygame.mixer.Sound.play(tik)
                    prgs1.destroy()
                    basbaslik = tk.Label(baslikutu2, text=f"Tamamlandı!", bg=acikyesil, fg=yazirengi)
                    basbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    basbaslik.place(relwidth=1, relheight=1)
                    basyazi = tk.Label(baslikutu3, text=f"Kurulum Başarıyla Tamamlandı!", bg=arkaplan, fg=yazirengi)
                    basyazi.config(font=("Montserrat Medium", "12"))
                    basyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                    with open('data.json', 'r') as f:
                        key = json.load(f)
                    key[str(f"krlm_chk")] = 1
                    with open('data.json', 'w') as f:
                        json.dump(key, f, indent=4)
                    def cikis():
                        pygame.mixer.Sound.play(click)
                        print("cıkıs basıldı")
                        try:
                           RPC.close()
                        except:
                            print("discord yürütülmeimş")
                        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                        lisans2.destroy()
                        exit(0)
                    cikıs = tk.Button(baslikutu3, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
                    cikıs.place(rely=0.87, relx= 0.89)
                    def ybb():
                        pygame.mixer.Sound.play(click)
                        os.system("shutdown /r /t 0")
                        lisans2.destroy()
                        exit(0)
                    yb = tk.Button(baslikutu3, text=" Yeniden Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybb)
                    yb.place(rely=0.24, relx= 0.42)

                sism = tk.Label(baslikutu3, text=f"Tebrikler! Lisansınız Başarıyla Etkinleştirildi. Fakat Programı İlk Defa Yürüttüğünüzü Farkettik. ", bg=arkaplan, fg=yazirengi)
                sism.config(font=("Montserrat Medium", "10"))
                sism1 = tk.Label(baslikutu3, text=f"Programın Çalışması İçin Ufak Bir Kurulum Yapması Gerekli. Bu işlem Sadece Bir Kere Yapılacaktır. ", bg=arkaplan, fg=yazirengi)
                sism1.config(font=("Montserrat Medium", "10"))
                sism.place(relwidth=1, relheight=0.1, rely=0.01)
                sism1.place(relwidth=1, relheight=0.1, rely=0.1)
                deq = tk.Button(baslikutu3, text=" Kur! ", padx=15, pady=15, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=kuraq).start)
                deq.place(rely=0.25, relx= 0.45)
                lisans2.mainloop()
            elif get_krlm() == 1 and not offline_modu:
                try:
                    RPC.update(details="Kurulum Yapıyor", start=zmn, state="İkinci Aşamada",large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                except:
                    print("discord yürümüyor.")
                actsupdater.acts_guncelle(bitir=True)
                pygame.mixer.Sound.play(dikkat)
                lisans2 = tk.Tk()
                lisans2.title(f"AcemTube Kurulum")
                lisans2.iconbitmap("acemtubesetup.ico")
                licanvas2 = tk.Canvas(lisans2, height=510, width=750, background=acikgri2)
                licanvas2.pack()
                yer = str(lisans2.winfo_screenwidth()/2 - 750/2).split(".")[0]
                yer1 = str(lisans2.winfo_screenheight()/2 - 510/2).split(".")[0]
                lisans2.geometry(f"750x510+{yer}+{yer1}")
                lisans2.attributes("-alpha", seffaflik)
                lisans2.resizable(False, False)
                baslikutu2 = tk.Frame(lisans2, bg=acikmavi)
                baslikutu2.place(relwidth=1, relheight=0.1)
                baslikutu3 = tk.Frame(lisans2, bg=arkaplan)
                baslikutu3.place(relwidth=1, relheight=0.9, rely=0.1)

                basarili = tk.Label(baslikutu2, text=f"İkinci Kurulum", bg=acikmavi, fg=yazirengi)
                basarili.config(font=("Montserrat ExtraBold", "30", "italic"))
                basarili.place(relwidth=1, relheight=0.9)
                def kuraq():
                    pygame.mixer.Sound.play(click)
                    print("ok kuruom")
                    sism.destroy()
                    deq.destroy()
                    basarili.destroy()
                    progyaz = tk.Label(baslikutu2, text=f"İndiriliyor...", bg=acikmavi, fg=yazirengi)
                    progyaz.config(font=("Montserrat ExtraBold", "30", "italic"))
                    progyaz.place(relwidth=1, relheight=1)

                    progyazi = tk.Label(baslikutu3, text=f"Gereken Bileşenler İndiriliyor", bg=arkaplan, fg=yazirengi)
                    progyazi.config(font=("Montserrat Medium", "12"))
                    s = ttk.Style()
                    s.theme_use("clam")
                    s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
                    prgs1 = ttk.Progressbar(baslikutu3, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
                    prgs1.place(relx=0.265, rely=0.2)
                    progyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                    #subprocess.call("scoop install git", shell=True)
                    time.sleep(1)
                    prgs1['value'] += 5
                    subprocess.call("scoop update", shell=True)
                    prgs1['value'] += 30
                    subprocess.call("scoop uninstall ffmpeg", shell=True)
                    prgs1['value'] += 40
                    prgs1.config(mode="indeterminate")
                    prgs1.start(25)
                    subprocess.call("scoop install ffmpeg", shell=True)
                    prgs1.config(mode="determinate")
                    time.sleep(0.5)
                    prgs1.stop()
                    prgs1['value'] = 85

                    ffmpeg_chck2 = subprocess.run("ffmpeg", capture_output=True, shell=True)
                    if "'ffmpeg' is not recognized as an internal or external command" in str(ffmpeg_chck2):
                        print("FFMPEG KURULU DEĞİL!")
                        with open('data.json', 'r') as f:
                            clc = json.load(f)
                        clc[str(f"krlm_chk")] = 1
                        with open('data.json', 'w') as f:
                            json.dump(clc, f, indent=4)
                        subprocess.call("scoop uninstall ffmpeg", shell=True)
                        subprocess.call("scoop cache rm ffmpeg", shell=True)

                        lisans2.attributes("-alpha", 0)
                        lisans2.title(f"AcemTube")

                        lisans2.geometry(f"{lisans2.winfo_screenwidth()}x{lisans2.winfo_screenheight()}+0+0")
                        lisans2.bell()
                        pygame.mixer.Sound.play(hata1)
                        messagebox.showerror("Hata!", "Kurulum Yaparken Bir Hata Oluştu. 1. Kurulumdan Sonra Bilgisayarınızı Yeniden Başlattığınızdan Emin Olun.")
                        pygame.mixer.Sound.play(click)
                        pygame.mixer.Sound.play(hata)
                        yeniden_dene = messagebox.askretrycancel("Kurulum", "Kurulumu Yeniden Denemek İster Misiniz?")
                        pygame.mixer.Sound.play(click)
                        if yeniden_dene:
                            try:
                                os.startfile("acemtube.exe")
                            except:
                                os.startfile("acemtube.py")
                        try:
                            RPC.close()
                        except:
                            print("discord yürütülmeimş")
                        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                        lisans2.destroy()
                        exit(0)
                    else:
                        with open('data.json', 'r') as f:
                            clc = json.load(f)
                        clc[str(f"krlm_chk")] = 2
                        with open('data.json', 'w') as f:
                            json.dump(clc, f, indent=4)

                    time.sleep(1)
                    prgs1['value'] += 100
                    time.sleep(1)
                    progyaz.destroy()
                    progyazi.destroy()
                    prgs1.destroy()
                    pygame.mixer.Sound.play(dikkat)
                    try:
                        RPC.update(details="Kurulum Yapıyor", start=zmn, state="Kayıt Yolu ayarlıyor",large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
                    except:
                        print("discord yürümüyor.")
                    print("kayıtyol basıldı")


                    def get_yol():
                        with open('data.json', 'r') as f:
                            yol = json.load(f)
                        if "kayit_yolu" in yol:
                            if not yol["kayit_yolu"] == "":
                                return yol["kayit_yolu"]
                            else:
                                return "Yok"
                        else:
                            return "Yok"

                    def kayyaz():
                        pygame.mixer.Sound.play(tik)
                        print(dosyaadi)
                        devamk.destroy()
                        sec.destroy()
                        kurulbaslik.destroy()
                        basyazi.destroy()
                        secilyazi.destroy()
                        with open('data.json', 'r') as f:
                            yol = json.load(f)
                        yol[str(f"kayit_yolu")] = dosyaadi
                        with open('data.json', 'w') as f:
                            json.dump(yol, f, indent=4)
                        pygame.mixer.Sound.play(tik)
                        basbaslik = tk.Label(baslikutu2, text=f"Tamamlandı!", bg=acikyesil, fg=yazirengi)
                        basbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                        basbaslik.place(relwidth=1, relheight=1)
                        basyazi1 = tk.Label(baslikutu3, text=f"Kurulum Başarıyla Tamamlandı!", bg=arkaplan, fg=yazirengi)
                        basyazi1.config(font=("Montserrat Medium", "12"))
                        basyazi1.place(relwidth=1, relheight=0.1, rely=0.1)

                        def cikis():
                            pygame.mixer.Sound.play(click)
                            print("cıkıs basıldı")
                            try:
                                RPC.close()
                            except:
                                print("discord yürütülmeimş")
                            lisans2.destroy()
                            exit(0)
                        cikıs = tk.Button(baslikutu3, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
                        cikıs.place(rely=0.87, relx= 0.89)
                        def ybb():
                            pygame.mixer.Sound.play(click)
                            lisans2.destroy()
                            ilkbaslangic()

                        yb = tk.Button(baslikutu3, text=" Programı Başlat ", padx=15, pady=20, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=ybb)
                        yb.place(rely=0.24, relx= 0.42)


                    def kaybasla():
                        pygame.mixer.Sound.play(click)
                        global dosyaadi
                        dosyaadi = tk.filedialog.askdirectory(initialdir="/", title="Kayıt Klasörü Seçiniz.")
                        pygame.mixer.Sound.play(click)
                        print('"' + dosyaadi + '"')
                        if not dosyaadi == "":
                            devamk.config(state=NORMAL)
                            secilyazi.config(text=f"Seçilen Yol: {dosyaadi}", bg=arkaplan, fg=yazirengi)
                        else:
                            devamk.config(state=DISABLED)
                            secilyazi.config(text=f"Seçilen Yol: Yok", bg=arkaplan, fg=yazirengi)

                    sec = tk.Button(baslikutu3, text=" Seç ", padx=22, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kaybasla)
                    sec.place(rely=0.31, relx= 0.45)
                    kurulbaslik = tk.Label(baslikutu2, text=f"Kaydetme Yolu Ayarla", bg=acikmavi, fg=yazirengi)
                    kurulbaslik.config(font=("Montserrat ExtraBold", "30", "italic"))
                    kurulbaslik.place(relwidth=1, relheight=0.9)
                    global basyazi
                    basyazi = tk.Label(baslikutu3, text=f"Lütfen Aşağıdaki Tuşa Basıp İndirilen Ses Ve Videoların Gideceği Yolu Belirtin.", bg=arkaplan, fg=yazirengi)
                    basyazi.config(font=("Montserrat Medium", "12"))
                    basyazi.place(relwidth=1, relheight=0.1, rely=0.1)
                    devamk = tk.Button(baslikutu3, text=" Uygula ", padx=17, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, state=DISABLED, command=kayyaz)
                    devamk.place(rely=0.41, relx= 0.444)
                    if get_yol() != "Yok" and get_yol() != "":
                        devamk.config(state=NORMAL)
                    global secilyazi
                    secilyazi = tk.Label(baslikutu3, text=f"Seçili Yol: {get_yol()}", bg=arkaplan, fg=yazirengi)
                    secilyazi.config(font=("Montserrat Medium", "10"))
                    secilyazi.place(relwidth=1, relheight=0.1, rely=0.2)

                sism = tk.Label(baslikutu3, text=f"Tebrikler! Kurulumun İlk Bölümünü Tamamladınız! İkinci Bölümü De Tamamladıktan Sonra Programı Yürütebileceksiniz!", bg=arkaplan, fg=yazirengi)
                sism.config(font=("Montserrat Medium", "9"))

                sism.place(relwidth=1, relheight=0.1, rely=0.05)
                bruh = tk.IntVar()
                def sesyrt():
                    pygame.mixer.Sound.play(click)
                deq = tk.Button(baslikutu3, text=" Kur! ", padx=15, pady=15, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=kuraq).start)
                deq.place(rely=0.2, relx= 0.45)
                lisans2.mainloop()
            else:
                ilkbaslangic()

        if kld_get() == "yok" or sif_get() == "yok":
            def aktbasla():
                pygame.mixer.Sound.play(click)    
                try:
                    hwidstr = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                    async def hello():
                        uri = server
                        async with websockets.connect(uri) as websocket:
                            rawistek = f"{giris.get()}<///>{giris1.get()}<///>{hwidstr}".encode("ascii")
                            istek = base64.b64encode(rawistek)
                            print(f"{istek} İsteği Gönderiliyor")
                            await websocket.send(istek)
                            print(f"{istek} İsteği Gönderildi. Cevap Bekleniyor...")

                            sifcevap = await websocket.recv()
                            global cevap
                            cevap = sifcevap
                            print(f"Cevap: {cevap}")
                            
                    asyncio.get_event_loop().run_until_complete(hello())

                    if cevap == "1":
                        with open('data.json', 'r') as f:
                            jayson = json.load(f)
                        jayson[str(f"kullanici_adi")] = giris.get()
                        with open('data.json', 'w') as f:
                            json.dump(jayson, f, indent=4)
                        with open('data.json', 'r') as f:
                            jayson1 = json.load(f)
                        jayson1[str(f"kullanici_parola")] = giris1.get()
                        with open('data.json', 'w') as f:
                            json.dump(jayson1, f, indent=4)

                        #anahtar yarat
                        hwid = giris.get() + str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                        #print(hwid)
                        if len(hwid) == 32:
                            antstr = hwid
                        elif len(hwid) < 32:
                            antstr = hwid + ("a"*(32 - len(hwid)))
                            #print("int: " + str(antstr))
                        else:
                            antstr = hwid[:32]
                            #print("ints: " + str(antstr))

                        anahtar = base64.urlsafe_b64encode(antstr.encode("ascii"))
                        #yaz
                        #tarih falan şifrele
                        grs = str(datetime.datetime.utcnow())
                        print("Giriş şifreleniyor...")
                        anlanahtar = Fernet(anahtar)
                        sifrelenen = anlanahtar.encrypt(grs.encode())
                        #print(sifrelenen)

                        #yaz
                        with open('data.json', 'r') as f:
                            jayson1 = json.load(f)
                        jayson1[str(f"ofd")] = str(sifrelenen).replace("b'", "").strip("'")
                        with open('data.json', 'w') as f:
                            json.dump(jayson1, f, indent=4)

                        pygame.mixer.Sound.play(tik)
                        lisans.destroy()
                        kurulumchk()
                    elif cevap == "7":
                        with open('data.json', 'r') as f:
                            jayson = json.load(f)
                        jayson[str(f"kullanici_adi")] = giris.get()
                        with open('data.json', 'w') as f:
                            json.dump(jayson, f, indent=4)
                        with open('data.json', 'r') as f:
                            jayson1 = json.load(f)
                        jayson1[str(f"kullanici_parola")] = giris1.get()
                        with open('data.json', 'w') as f:
                            json.dump(jayson1, f, indent=4)
                        pygame.mixer.Sound.play(tik)
                        lisans.destroy()
                        kurulumchk()
                    elif cevap == "2":
                        pygame.mixer.Sound.play(hata1)
                        htayazi.config(text=f"Hesabınızın Lisansı Feshedilmiş!")
                        htayazi1.config(text=f"https://acemtube.glitch.me/ Websitesinden Yeniden Aktif Edebilirsiniz!")

                        giris.delete(0, 'end')
                        giris1.delete(0, 'end')
                    elif cevap == "0":
                        pygame.mixer.Sound.play(hata1)
                        htayazi.config(text=f"Hesabınızın Bu Programda Lisans Yetkisi Yok!")
                        htayazi1.config(text=f"https://acemtube.glitch.me/ Sitesinden Elde Edebilirsiniz!")
                        giris.delete(0, 'end')
                        giris1.delete(0, 'end')
                    elif cevap == "4":
                        pygame.mixer.Sound.play(hata1)
                        htayazi.config(text=f"Kullanıcı Adı Bulunamadı!")
                        htayazi1.config(text=f"Eğer Hesabınız Yoksa https://acemtube.glitch.me/ Websitesinden Oluşturabilirsiniz!")
                        giris.delete(0, 'end')
                        giris1.delete(0, 'end')
                    elif cevap == "5":
                        pygame.mixer.Sound.play(hata1)
                        htayazi.config(text=f"Parolanız Yanlış!")
                        htayazi1.config(text=f"{dclink} Discord Sunucusundan Yardım Alabilirsiniz!")
                        giris.delete(0, 'end')
                        giris1.delete(0, 'end')
                    elif cevap == "3":
                        pygame.mixer.Sound.play(hata1)
                        htayazi.config(text=f"Bu Hesabın Maksimum Makine Sayısına Ulaşıldı!")
                        htayazi1.config(text=f"Makine Sildirmek İçin Discord Sunucumuzdan Yardım Alabilirsiniz!")
                        giris.delete(0, 'end')
                        giris1.delete(0, 'end')
                    elif "[6]-" in cevap or "[7]-" in cevap:
                        pygame.mixer.Sound.play(hata)
                        kod = cevap.split("]-")[-1]
                        kpw = tk.Tk()
                        kpw.title("E-Posta Doğrulama")
                        kpw.resizable(False, False)
                        kpw.iconbitmap("acemtubel.ico")
                        yer2 = str(kpw.winfo_screenwidth()/2 - 450/2).split(".")[0]
                        yer3 = str(kpw.winfo_screenheight()/2 - 300/2).split(".")[0]

                        def kapa():
                            pygame.mixer.Sound.play(click)
                            kpw.destroy()
                            lisans.attributes('-disabled', False)
                            lisans.wm_state('iconic')
                            lisans.wm_state('normal')

                        kpw.protocol("WM_DELETE_WINDOW", kapa)
                        kpw.geometry(f"450x300+{yer2}+{yer3}")
                        kpw.attributes("-alpha", seffaflik)
                        lisans.attributes('-disabled', True)
                        canvas = tk.Canvas(kpw, height=300, width=450, background=acikgri2)
                        canvas.pack()
                        emnk = tk.Frame(kpw, bg=arkaplan)
                        emnk1 = tk.Frame(kpw, bg=arkaplan)
                        emnk.place(relwidth=1, relheight=0.8, rely=0.2)
                        emnk1.place(relwidth=1, relheight=0.2)
                        emnb = tk.Label(emnk1, text=f"E-Posta Doğrulama", bg=acikyesil, fg=baslikyazirengi)
                        emnb.config(font=("Montserrat ExtraBold", "30", "italic"))

                        emnb.place(relwidth=1, relheight=0.9)

                        ckyazi = tk.Label(emnk, text=f"Yeni Bir Cihazdan Bağlanmış Gibi Görünüyorsunuz.\n \n Lütfen E-Postanıza Gönderilen Kodu Giriniz.", bg=arkaplan, fg=yazirengi)
                        ckyazi.config(font=("Arial", "9"))
                        ckyazi.place(relwidth=1, relheight=0.2, rely=0.1)

                        ckyazi1 = tk.Label(emnk, text=f"", bg=arkaplan, fg=kirmiziyazi)
                        ckyazi1.config(font=("Arial", "14"))
                        ckyazi1.place(relwidth=1, relheight=0.15, rely=0.7)

                        giris3 = tk.Entry(emnk, width=7, bg=aramarengi, borderwidth=kenargenisligi, relief=stil, font=("Montserrat Medium", 20) , justify='center', fg=yazirengi)
                        giris3.pack(pady=80)

                        def epostabasla():
                            pygame.mixer.Sound.play(click)
                            temizkod = "".join(str(giris3.get()).split("-")).strip()
                            if kod == temizkod:
                                with open('data.json', 'r') as f:
                                    jayson = json.load(f)
                                jayson[str(f"kullanici_adi")] = giris.get()
                                with open('data.json', 'w') as f:
                                    json.dump(jayson, f, indent=4)
                                with open('data.json', 'r') as f:
                                    jayson1 = json.load(f)
                                jayson1[str(f"kullanici_parola")] = giris1.get()
                                with open('data.json', 'w') as f:
                                    json.dump(jayson1, f, indent=4)
                                async def hello():
                                    uri = server
                                    async with websockets.connect(uri) as websocket:
                                        hwidstr = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                                        istek = f"makinekle-{giris.get()}|{hwidstr}"
                                        print(f"{istek} İsteği Gönderiliyor")
                                        await websocket.send(istek)
                                asyncio.get_event_loop().run_until_complete(hello())
                                pygame.mixer.Sound.play(tik)
                                lisans.destroy()
                                kpw.destroy()
                                kurulumchk()
                            else:
                                print(kod)
                                print(giris3.get())
                                ckyazi1.config(text="Geçersiz Kod.")
                                pygame.mixer.Sound.play(hata1)
                                emnb.config(bg=kirmizi)

                        devamke = tk.Button(emnk, text=" Giriş Yap! ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=epostabasla)
                        devamke.place(rely=0.55, relx=0.41)

                    else:
                        pygame.mixer.Sound.play(hata1)
                        htayazi.config(text=f"Hata!")
                        htayazi1.config(text=f"Sunucu Bağlantıyı Reddetti.")
                        giris.delete(0, 'end')
                        giris1.delete(0, 'end') 
                except Exception as e:
                    pygame.mixer.Sound.play(hata1)
                    htayazi.config(text=f"Hata!")
                    htayazi1.config(text=f"{e}")
                    giris.delete(0, 'end')
                    giris1.delete(0, 'end') 
            try:
                    RPC.update(details="Giriş Yapıyor", start=zmn, large_image="acemtubeldc", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
            except:
                print("discord yürümüyor.")

            lisans = tk.Tk()
            lisans.title(f"AcemTube Lisans")
            lisans.iconbitmap("acemtubel.ico")
            lisans.resizable(False, False)
            yer = str(lisans.winfo_screenwidth()/2 - 750/2).split(".")[0]
            yer1 = str(lisans.winfo_screenheight()/2 - 510/2).split(".")[0]
            lisans.geometry(f"750x510+{yer}+{yer1}")
            lisans.attributes("-alpha", seffaflik)
            licanvas = tk.Canvas(lisans, height=510, width=750, background=acikgri2)
            licanvas.pack()

            def cikis():
                pygame.mixer.Sound.play(click)
                print("cıkıs basıldı")
                try:
                   RPC.close()
                except:
                    print("discord yürütülmeimş")
                subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
                lisans.destroy()
                exit(0)

            baslikutu = tk.Frame(lisans, bg=acikmavi)
            baslikutu.place(relwidth=1, relheight=0.1)
            baslikutu1 = tk.Frame(lisans, bg=arkaplan)
            baslikutu1.place(relwidth=1, relheight=0.9, rely=0.1)
            htayazi = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=kirmizi)
            htayazi.config(font=("Montserrat Medium", "14"))
            htayazi.place(relwidth=1, relheight=0.1, rely=0.45)
            htayazi1 = tk.Label(baslikutu1, text=f"", bg=arkaplan, fg=yazirengi)
            htayazi1.config(font=("Montserrat Medium", "10"))
            htayazi1.place(relwidth=1, relheight=0.1, rely=0.55)
            def get_hata():
                with open('data.json', 'r') as f:
                    yol = json.load(f)
                if "giris_hata" in yol:
                    return yol["giris_hata"]
                else:
                    return "1"

            if get_hata() == "0":
                with open('data.json', 'r') as f:
                    jayson = json.load(f)
                jayson[str(f"giris_hata")] = "1"
                with open('data.json', 'w') as f:
                    json.dump(jayson, f, indent=4)
                pygame.mixer.Sound.play(dikkat)
                htayazi.config(text="Hata!")
                htayazi1.config(text="Hesabınızın Lisans Erişimi Yok! acemtube.glitch.me Sitemizden Satın Alabilirsiniz!")
            elif get_hata() == "2":
                with open('data.json', 'r') as f:
                    jayson = json.load(f)
                jayson[str(f"giris_hata")] = "1"
                with open('data.json', 'w') as f:
                    json.dump(jayson, f, indent=4)
                pygame.mixer.Sound.play(dikkat)
                htayazi.config(text="Hata!")
                htayazi1.config(text="Hesabınız Fesh Edilmiş! Programa Olan Erişiminiz Engellenmiştir.")
            elif get_hata() == "3":
                with open('data.json', 'r') as f:
                    jayson = json.load(f)
                jayson[str(f"giris_hata")] = "1"
                with open('data.json', 'w') as f:
                    json.dump(jayson, f, indent=4)
                pygame.mixer.Sound.play(dikkat)
                htayazi.config(text="Hata!")
                htayazi1.config(text="Hesabınızın Maksimum Makine Sayısı Aşıldı! Giriş Yapabilmek İçin Lütfen Diğer Makinelerden Çıkış Yapınız.")
            elif get_hata() == "4":
                with open('data.json', 'r') as f:
                    jayson = json.load(f)
                jayson[str(f"giris_hata")] = "1"
                with open('data.json', 'w') as f:
                    json.dump(jayson, f, indent=4)
                pygame.mixer.Sound.play(dikkat)
                htayazi.config(text="Hata!")
                htayazi1.config(text="Kullanıcı Adı Bulunamadı!")
            elif get_hata() == "5":
                with open('data.json', 'r') as f:
                    jayson = json.load(f)
                jayson[str(f"giris_hata")] = "1"
                with open('data.json', 'w') as f:
                    json.dump(jayson, f, indent=4)
                pygame.mixer.Sound.play(dikkat)
                htayazi.config(text="Hata!")
                htayazi1.config(text="Parolanız Hatalı!")
            
            baslik = tk.Label(baslikutu, text=f"AcemTube Lisans", bg=acikmavi, fg=baslikyazirengi)
            baslik.config(font=("Montserrat ExtraBold", "30", "italic"))
            baslik.place(relwidth=1, relheight=0.9)
            actsupdater.acts_guncelle(bitir=True)
            altlik = tk.Label(baslikutu1, text=f"      Versiyon : {version} By Acem", bg=arkaplan, fg=yazirengi)
            altlik.config(font=("Montserrat Medium", "7"))
            altlik.place(relwidth=0.21, relheight=0.05, rely=0.95, relx=0.78)
            sescik1 = tk.Label(baslikutu1, text=f"Lütfen Giriş Yapınız.", bg=arkaplan, fg=yazirengi)
            sescik1.config(font=("Montserrat Medium", "11"))
            sescik1.place(relwidth=1, relheight=0.1, rely=0.01)
            global giris
            giris = tk.Entry(baslikutu1, width=30, bg=aramarengi, borderwidth=kenargenisligi, relief=stil, fg=yazirengi)
            giris.place(rely=0.1, relx=0.38)

            giris1 = tk.Entry(baslikutu1, width=30, bg=aramarengi, borderwidth=kenargenisligi, relief=stil, show="*", fg=yazirengi)
            giris1.place(rely=0.15, relx=0.38)
            parolatxt = tk.Label(baslikutu1, text=f"Parola", bg=arkaplan, fg=yazirengi)
            parolatxt.config(font=("Montserrat Medium", "9"))
            parolatxt.place(relwidth=0.09, relheight=0.03, rely=0.15, relx=0.29)
            kladtxt = tk.Label(baslikutu1, text=f"Kullanıcı Adı", bg=arkaplan, fg=yazirengi)
            kladtxt.config(font=("Montserrat Medium", "9"))
            kladtxt.place(relwidth=0.1, relheight=0.03, rely=0.1, relx=0.26)
            devamke = tk.Button(baslikutu1, text=" Giriş Yap! ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=aktbasla)
            devamke.place(rely=0.25, relx= 0.444)
            print(giris.keys())
            def dce():
                pygame.mixer.Sound.play(click)
                webbrowser.open(dclink)

            def dceb():
                pygame.mixer.Sound.play(click)
                webbrowser.open("https://acemtube.glitch.me/")

            def yout():
                pygame.mixer.Sound.play(click)
                webbrowser.open("https://youtube.com/c/acem8887")

            def lisanssoz():

                pygame.mixer.Sound.play(click)
                print("lisanssöz basıldı")
                #os.startfile(".\BeniOku\lisans.txt")
                lisans.attributes('-disabled', True)
                kpw = tk.Tk()
                kpw.title("AcemTube Lisans Sözleşmesi")
                kpw.resizable(False, False)
                kpw.iconbitmap("acemtubesetup.ico")
                def kapa():
                    pygame.mixer.Sound.play(click)
                    kpw.destroy()
                    lisans.attributes('-disabled', False)
                    lisans.wm_state('iconic')
                    lisans.wm_state('normal')

                kpw.protocol("WM_DELETE_WINDOW", kapa)
                yer2 = str(kpw.winfo_screenwidth()/2 - 740/2).split(".")[0]
                yer3 = str(kpw.winfo_screenheight()/2 - 510/2).split(".")[0]
                kpw.geometry(f"740x510+{yer2}+{yer3}")
                kpw.attributes("-alpha", seffaflik)
                canvas = tk.Canvas(kpw, height=510, width=740, background=arkaplan)
                canvas.pack()

                baslikutu8 = tk.Frame(kpw, bg=acikyesil)
                baslikutu8.place(relwidth=1, relheight=0.1)

                baslikutu9 = tk.Frame(kpw, bg=acarka)
                baslikutu9.place(relwidth=0.85, relheight=0.75, rely=0.1, relx=0.08)
                yanl = tk.Frame(kpw, bg=arkaplan)
                yanl.place(relwidth=0.08, relheight=0.75, rely=0.1)
                yanr = tk.Frame(kpw, bg=arkaplan)
                yanr.place(relwidth=0.07, relheight=0.75, rely=0.1, relx=0.93)
                baslikutu7 = tk.Frame(kpw, bg=arkaplan)
                baslikutu7.place(relwidth=1, relheight=0.15, rely=0.85)
                hatabaslik = tk.Label(baslikutu8, text=f"AcemTube {version} Lisans Sözleşmesi", bg=acikyesil, fg=yazirengi)
                hatabaslik.config(font=("Montserrat ExtraBold", "27", "italic"))
                hatabaslik.place(relwidth=1, relheight=1)
                text_scroll = tk.Scrollbar(baslikutu9)
                text_scroll.pack(side=RIGHT, fill=Y)

                lisanstxt = tk.Text(baslikutu9, width=740, height=480, font=("Montserrat Medium", 10), bg=acarka, fg=yazirengi, borderwidth=kenargenisligi, relief=stil, selectbackground=acikyesil, yscrollcommand=text_scroll.set)
                lisanstxt.pack()

                text_scroll.config(command=lisanstxt.yview)
                yb = tk.Button(baslikutu7, text=" Kapat ", padx=15, pady=10, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kapa)
                yb.place(rely=0.2, relx=0.45)
                lisanstxt.insert(0.0, soz)

                lisanstxt.config(state=DISABLED)

                kpw.mainloop()

            devamkeslka = tk.Button(baslikutu1, text=" Lisans Sözleşmesi ", padx=10, pady=5, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=lisanssoz)
            devamkeslka.place(rely=0.35, relx= 0.416)

            cikıs = tk.Button(baslikutu1, text=" Çıkış ", padx=15, pady=1, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikis)
            cikıs.place(rely=0.87, relx= 0.89)
            disc = tk.Button(baslikutu1, text=" Discord Sunucumuz ", padx=16, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dce)
            disc.place(rely=0.75, relx= 0.1)

            discb = tk.Button(baslikutu1, text=" AcemTube Websitesi ", padx=17.8, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=dceb)
            discb.place(rely=0.75, relx= 0.4)

            engil = tk.Button(baslikutu1, text=" Youtube Kanalımız ", padx=14, pady=4, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=yout)
            engil.place(rely=0.75, relx= 0.7)
            pygame.mixer.Sound.play(dikkat)
            lisans.mainloop()
        else:
            try:
                def kld1_get():
                    with open('data.json', 'r') as f:
                        klad = json.load(f)
                    if "kullanici_adi" in klad:
                        return klad["kullanici_adi"]
                    else:
                        return None
                def sif1_get():
                    with open('data.json', 'r') as f:
                        klad = json.load(f)
                    if "kullanici_parola" in klad:
                        return klad["kullanici_parola"]
                    else:
                        return None
    
                async def hello():
                    uri = server
                    async with websockets.connect(uri) as websocket:
                        hwidstr = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                        rawistek = f"{kld1_get()}<///>{sif1_get()}<///>{hwidstr}".encode("ascii")
                        istek = base64.b64encode(rawistek)
                        print(f"{istek} İsteği Gönderiliyor")
                        await websocket.send(istek)
                        actsupdater.acts_guncelle(7.142857142857143)
                        print(f"{istek} İsteği Gönderildi. Cevap Bekleniyor...")
                        sifcevap = await websocket.recv()
                        print(f"Şifreli Cevap: {sifcevap}")
                        global cevap
                        cevap = sifcevap
                        print(f"Cevap: {cevap}")
                        
                asyncio.get_event_loop().run_until_complete(hello())

                if cevap == "1":
                    hwid = kld1_get() + str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
                    #print(hwid)
                    if len(hwid) == 32:
                        antstr = hwid
                    elif len(hwid) < 32:
                        antstr = hwid + ("a"*(32 - len(hwid)))
                        #print("int: " + str(antstr))
                    else:
                        antstr = hwid[:32]
                        #print("ints: " + str(antstr))

                    anahtar = base64.urlsafe_b64encode(antstr.encode("ascii"))
                    #yaz
                    #tarih falan şifrele
                    grs = str(datetime.datetime.utcnow())
                    print("Giriş şifreleniyor...")
                    anlanahtar = Fernet(anahtar)
                    sifrelenen = anlanahtar.encrypt(grs.encode())
                    #print(sifrelenen)

                    #yaz
                    with open('data.json', 'r') as f:
                        jayson1 = json.load(f)
                    jayson1[str(f"ofd")] = str(sifrelenen).replace("b'", "").strip("'")
                    with open('data.json', 'w') as f:
                        json.dump(jayson1, f, indent=4)
                    actsupdater.acts_guncelle(8)
                    #jsonlogin
                    kurulumchk()
                elif cevap == "7":
                    actsupdater.acts_guncelle(8)
                    kurulumchk()
                else:
                    try:
                        with open('data.json', 'r') as f:
                            key = json.load(f)
                        key.pop("kullanici_adi")
                        with open('data.json', 'w') as f:
                            json.dump(key, f, indent=4)
                        with open('data.json', 'r') as f:
                            key1 = json.load(f)
                        key1.pop("kullanici_parola")
                        with open('data.json', 'w') as f:
                            json.dump(key1, f, indent=4)
                    except:
                        print("Jsona Yazamadım aq")
                    print("Bir Şey Yanlış.")
                    hebe()
            except Exception as e:
                if not offline_modu:
                    print(e)
                    print("İlk Eventte Sorun Var")
                    print(f"Deneme: {len(deneme)}, {deneme}")
                    if len(deneme) > 2:
                        rut = tk.Tk()
                        rut.attributes("-alpha", 0)
                        rut.title(f"AcemTube")
                        rut.iconbitmap("acemtubered.ico")
                        deneme.append(str(e))
                        rut.geometry(f"{rut.winfo_screenwidth()}x{rut.winfo_screenheight()}+0+0")
                        rut.bell()
                        messagebox.showerror("Hata!", f"AcemTube Sunucularına Şu An Erişemiyoruz. Lütfen İnternet Bağlantınızı Kontrol Edin Veya Programı Güncelleyin. \n\nHata Kodu: {e} \n\nDiscord Sunucumuzdan Yardım Alabilirsiniz: {dclink}")
                    else:
                        deneme.append(str(e))

                        hebe()
                else:
                    kurulumchk()
    hbbasla()

def get_sozlesme():
    with open('data.json', 'r') as f:
        soz = json.load(f)
    if "lisans_sozlesmesi" in soz:
        return soz["lisans_sozlesmesi"]
    else:
        return 0
    
def surumbitiyor():
    actsupdater.acts_guncelle(bitir=True)
    pygame.mixer.Sound.play(hata)
    try:
        RPC.update(details="AcemTube Güncelleyici", start=zmn, state="Güncelleme Mevcut", large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
    except:
        print("discord yürümüyor.")
    kpw = tk.Tk()
    kpw.title(f"AcemTube Güncelleyici")
    kpw.resizable(False, False)
    kpw.iconbitmap("acemtubesetup.ico")
    yer2 = str(kpw.winfo_screenwidth()/2 - 700/2).split(".")[0]
    yer3 = str(kpw.winfo_screenheight()/2 - 400/2).split(".")[0]
    kpw.geometry(f"700x400+{yer2}+{yer3}")
    kpw.attributes("-alpha", seffaflik)
    canvas = tk.Canvas(kpw, height=400, width=700, background=acikgri2)
    canvas.pack()
    emnk = tk.Frame(kpw, bg=arkaplan)
    emnk1 = tk.Frame(kpw, bg=arkaplan)
    emnk.place(relwidth=1, relheight=0.8, rely=0.2)
    emnk1.place(relwidth=1, relheight=0.2)
    emnb = tk.Label(emnk1, text=f"Güncelleme Mevcut.", bg="#ff7b00", fg=yazirengi)
    emnb.config(font=("Montserrat ExtraBold", "30", "italic"))    
    emnb.place(relwidth=1, relheight=0.9)
    
    ckyazi = tk.Label(emnk, text=f"Şu Anki Sürümün ({version}) Kullanım Süresi Dolmuştur Ve Yeni Bir Sürüm ({guncelsurumadi}) Mevcuttur. Lütfen Güncelleyiniz.", bg=arkaplan, fg=yazirengi)
    ckyazi.config(font=("Montserrat Medium", "9"))
    ckyazi.place(relwidth=1, relheight=0.15, rely=0.2)
    def cikiss():
        pygame.mixer.Sound.play(click)
        try:
           RPC.close()
        except:
            print("discord yürütülmeimş")
        kpw.destroy()
        exit(0)
    def gri():
        pygame.mixer.Sound.play(click)
        try:
            RPC.update(details="AcemTube Güncelleyici", start=zmn, state="İndiriliyor...", large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
        except:
            print("discord yürümüyor.")
        canvas.destroy()
        emnk.destroy()
        emnk1.destroy()
        emnb.destroy()
        cikıss.destroy()
        anamenuu.destroy()
        yer = str(kpw.winfo_screenwidth()/2 - 350/2).split(".")[0]
        yer1 = str(kpw.winfo_screenheight()/2 - 100/2).split(".")[0]
        kpw.geometry(f"350x90+{yer}+{yer1}")
        kpw.overrideredirect(1)
        canvas1 = tk.Canvas(kpw, height=100, width=350, background=arkaplan)
        canvas1.pack()
        #baslikutu = tk.Frame(kpw, bg=acikmavi)
        #baslikutu.place(relwidth=1, relheight=0.1)
        #008000
        #313542
        baslikutu1 = tk.Frame(kpw, bg=arkaplan)
        baslikutu1.place(relwidth=1, relheight=1)
        baslik = tk.Label(baslikutu1, text=f"AcemTube", bg=arkaplan, fg=yazirengi)
        baslik.config(font=("Montserrat ExtraBold", "29", "bold italic"))
        baslik1 = tk.Label(baslikutu1, text=f"Güncelleniyor...", bg=arkaplan, fg=yazirengi)
        baslik1.config(font=("Montserrat ExtraBold", "12", "bold italic"))
        baslik.place(relwidth=0.67, relheight=0.6, relx=0.285)
        baslik1.place(relwidth=0.65, relheight=0.22, relx=0.3, rely=0.5)
        frm = tk.Frame()
        
        logo = ImageTk.PhotoImage(Image.open("acemtubesetups.png"))
        rlbl = tk.Label(baslikutu1, image=logo, bg=arkaplan ,fg=acikgri2)
        rlbl.place(relwidth=0.3, relheight=0.83)
        muzikres["muzikres"] = 1
        s = ttk.Style()
        s.theme_use("clam")

        s.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)
        prgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="indeterminate")
        prgs.place(rely=0.791)
        prgs.start(24)
        try:
            os.mkdir("gunccache")
        except:
            print("dizin zaten var")
        dosyaadi = updlink.split("/")[-1]
        try:
            os.remove(dosyaadi)
            print("dosya var")
        except:
            pass
        time.sleep(3)
        baslik1.config(text="İndiriliyor...")
        updget = requests.get(updlink)
        print(dosyaadi)
        
        baslik1.config(text="Yazılıyor...")
        time.sleep(1)
        with open(dosyaadi, "wb") as f:
            for chunk in updget.iter_content(chunk_size=chunkboyut):
                if chunk:
                    f.write(chunk)
        shutil.move(dosyaadi, r"./gunccache")
        baslik1.config(text="Temizleniyor...")
        sayi = 0
        for dosya in os.listdir(r"./"):
            if "AcemTube" in dosya and "setup.exe" in dosya:
                os.remove(dosya)
                print(dosya + " silindi")
                sayi += 1
                baslik1.config(text=f"Temizleniyor: ({sayi})...")
                time.sleep(0.5)
        
        baslik1.config(text="Yürütülüyor...")
        time.sleep(1)
        shutil.move( r"./gunccache/" + dosyaadi, r"./")
        try:
            shutil.rmtree("gunccache")
        except:
            print("dizin yok")

        baslik1.config(text="Tamamlandı!   ")
        time.sleep(0.5)
        os.startfile(f"{dosyaadi}")
        subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)

    cikıss = tk.Button(emnk, text= "       Çıkış       ", padx=30, pady=10, foreground=kirmiziyazi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=cikiss)
    cikıss.place(rely=0.5, relx= 0.25)
    anamenuu = tk.Button(emnk, text=" Güncellemeleri Al ", padx=20, pady=10, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=threading.Thread(target=gri).start)
    anamenuu.place(rely=0.5, relx= 0.55)
    kpw.mainloop()
    

def sozlesme():
    if get_sozlesme() != 1:
        actsupdater.acts_guncelle(bitir=True)
        try:
            RPC.update(details="Lisans Sözleşmesi Okuyor", start=zmn,large_image="acemtubesetup", large_text="Youtube Ses Video Ve Spotify İndirici. By: Acem#8887")
        except:
            print("discord yürümüyor.")
        pygame.mixer.Sound.play(dikkat)
        print("lisanssöz basıldı")
        #os.startfile(".\BeniOku\lisans.txt")

        kpw = tk.Tk()
        kpw.title("AcemTube Lisans Sözleşmesi")
        kpw.resizable(False, False)
        kpw.iconbitmap("acemtubesetup.ico")
        def kapa():
            pygame.mixer.Sound.play(click)
            try:
               RPC.close()
            except:
                print("discord yürütülmeimş")
            subprocess.call("TASKKILL /F /IM acemtube.exe", shell=True)
            kpw.destroy()
            exit(0)

        def kabul():
            with open('data.json', 'r') as f:
                jayson = json.load(f)
            jayson[str(f"lisans_sozlesmesi")] = 1
            with open('data.json', 'w') as f:
                json.dump(jayson, f, indent=4)
            kpw.destroy()
            pygame.mixer.Sound.play(tik)
            try:
                
                if verakt == "1" or verakt == "2":
                    hebe()
                elif verakt == "0":
                    surumbitiyor()
            except Exception as e:
                print(e)
                print("Verakt Problemi Var")
                print(f"Deneme: {len(deneme)}, {deneme}")
                if len(deneme) > 2:
                    rut = tk.Tk()
                    rut.attributes("-alpha", 0)
                    rut.title(f"AcemTube")
                    rut.iconbitmap("acemtubered.ico")
                    deneme.append(str(e))
                    rut.geometry(f"{rut.winfo_screenwidth()}x{rut.winfo_screenheight()}+0+0")
                    rut.bell()
                    messagebox.showerror("Hata!", f"AcemTube Sunucularına Şu An Erişemiyoruz. Lütfen İnternet Bağlantınızı Kontrol Edin Veya Programı Güncelleyin. \n\nHata Kodu: {e} \n\nDiscord Sunucumuzdan Yardım Alabilirsiniz: {dclink}")
                else:
                    deneme.append(str(e))

                    kabul()

        kpw.protocol("WM_DELETE_WINDOW", kapa)
        yer2 = str(kpw.winfo_screenwidth()/2 - 740/2).split(".")[0]
        yer3 = str(kpw.winfo_screenheight()/2 - 510/2).split(".")[0]
        kpw.geometry(f"740x510+{yer2}+{yer3}")
        kpw.attributes("-alpha", seffaflik)
        canvas = tk.Canvas(kpw, height=510, width=740, background=arkaplan)
        canvas.pack()

        baslikutu8 = tk.Frame(kpw, bg=acikyesil)
        baslikutu8.place(relwidth=1, relheight=0.1)
        baslikutu9 = tk.Frame(kpw, bg=acarka)
        baslikutu9.place(relwidth=0.85, relheight=0.75, rely=0.1, relx=0.08)
        yanl = tk.Frame(kpw, bg=arkaplan)
        yanl.place(relwidth=0.08, relheight=0.75, rely=0.1)
        yanr = tk.Frame(kpw, bg=arkaplan)
        yanr.place(relwidth=0.07, relheight=0.75, rely=0.1, relx=0.93)
        baslikutu7 = tk.Frame(kpw, bg=arkaplan)
        baslikutu7.place(relwidth=1, relheight=0.15, rely=0.85)
        hatabaslik = tk.Label(baslikutu8, text=f"AcemTube {version} Lisans Sözleşmesi", bg=acikyesil, fg=yazirengi)
        hatabaslik.config(font=("Montserrat ExtraBold", "27", "italic"))
        hatabaslik.place(relwidth=1, relheight=1)
        text_scroll = tk.Scrollbar(baslikutu9)
        text_scroll.pack(side=RIGHT, fill=Y)

        lisanstxt = tk.Text(baslikutu9, width=740, height=480, font=("Montserrat Medium", 10), bg=acarka, fg=yazirengi, borderwidth=kenargenisligi, relief=stil, selectbackground=acikyesil, yscrollcommand=text_scroll.set)
        lisanstxt.pack()

        text_scroll.config(command=lisanstxt.yview)
        kbl = tk.Button(baslikutu7, text=" Kabul Et ", padx=15, pady=10, foreground=yazirengi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kabul)
        kbl.place(rely=0.2, relx=0.52)
        red = tk.Button(baslikutu7, text="  Reddet  ", padx=15, pady=10, foreground=kirmizi, bg=koyugri, activebackground=acikgri, activeforeground=yazirengi, highlightbackground=acikgri, borderwidth=kenargenisligi, relief=stil, command=kapa)
        red.place(rely=0.2, relx=0.37)
        lisanstxt.insert(0.0, soz)

        lisanstxt.config(state=DISABLED)
        kpw.mainloop()
    else:
        try:
            if verakt == "1" or verakt == "2":
                with open('data.json', 'r') as f:
                    yzd = json.load(f)
                yzd[str(f"yuzde")] += 8
                with open('data.json', 'w') as f:
                    json.dump(yzd, f, indent=4)
                hebe()
            elif verakt == "0":
                surumbitiyor()
            else:
                raise Exception("Versiyon bilgisi yanlış")
        except Exception as e:
            print(e)
            print("Verakt 0 Problem")
            print(f"Deneme: {len(deneme)}, {deneme}")
            if len(deneme) > 2:
                rut = tk.Tk()
                rut.attributes("-alpha", 0)
                rut.title(f"AcemTube")
                rut.iconbitmap("acemtubered.ico")
                deneme.append(str(e))
                rut.geometry(f"{rut.winfo_screenwidth()}x{rut.winfo_screenheight()}+0+0")
                rut.bell()
                
                messagebox.showerror("Hata!", f"AcemTube Sunucularına Şu An Erişemiyoruz. Lütfen İnternet Bağlantınızı Kontrol Edin Veya Programı Güncelleyin. \n\nHata Kodu: {e} \n\nDiscord Sunucumuzdan Yardım Alabilirsiniz: {dclink}")
            else:
                deneme.append(str(e))

                sozlesme()

sozlesme()