import json
def get_yuzde():

    with open('data.json', 'r') as f:
        yol = json.load(f)
    return yol

def acts_start():
    import tkinter as tk
    from tkinter import filedialog, Text, DISABLED, NORMAL, ttk
    from PIL import ImageTk, Image
    import pyglet,tkinter
    import os
    import threading
    import time
    import asyncio
    import random

    pyglet.font.add_file('font.ttf')
    arkaplan = "#000000"
    koyugri = "#1c1c1c"
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
    jreeem = random.randint(0,100)
    jreem = jreeem == 0


    seffaflik = 0.9

    if os.path.isfile(r"./data.json"):
        if get_tema() == 0:
            print("Geçerli Tema Yok.")
        elif get_tema() != 0:
            print("Tema Yükleniyor.")
            try:
                with open(get_tema(), 'r') as f:
                    renk = json.load(f)
                if "arkaplan" in renk:
                    arkaplan = renk["arkaplan"]
                if "tusrengi" in renk:
                    koyugri = renk["tusrengi"]
                if "basmarengi" in renk:
                    acikgri = renk["basmarengi"]
                if "acikgri" in renk:
                    acikgri2 = renk["acikgri"]
                if "acikmavi" in renk:
                    acikmavi = renk["acikmavi"]
                if "acikyesil" in renk:
                    acikyesil = renk["acikyesil"]
                if "cubukrengi" in renk:
                    cubukrengi = renk["cubukrengi"]
                if "cubukrengi2" in renk:
                    cubukrengi2 = renk["cubukrengi2"]
                if "acikarka" in renk:
                    acarka = renk["acikarka"]
                if "yazirengi" in renk:
                    yazirengi = renk["yazirengi"]
                if "temaadi" in renk:
                    altyazi = renk["temaadi"]
                if "baslikyazirengi" in renk:
                    baslikyazirengi = renk["baslikyazirengi"]
                if "kirmizi" in renk:
                    kirmizi = renk["kirmizi"]
                if "kirmiziyazi" in renk:
                    kirmiziyazi = renk["kirmiziyazi"]
                if "aramarengi" in renk:
                    aramarengi = renk["aramarengi"]
                if "turuncu" in renk:
                    turuncu = renk["turuncu"]
                if "kenargenisligi" in renk:
                    kenargenisligi = renk["kenargenisligi"]
                if "acilisseffaflik" in renk:
                    seffaflik = renk["acilisseffaflik"]
            except:
                print("Tema Hatalı.")

    if jreem:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("jreem.mp3")
        pygame.mixer.music.play(loops=10)
        arkaplan = "#b5e51d"
        koyugri = "#1c1c1c"
        acikgri = "#313542"
        acikgri2 = "#23272a"
        acikmavi = "#ffffff"
        acikyesil = "#008000"
        koyugri2 = "#1d1f21"
        acarka = "#191414"
        yazirengi = "#000000"
        baslikyazirengi = "#000000"
        altyazi = "B L Λ C K O U T"
        kirmizi = "#FF0000"
        turuncu = "#FFA500"
        kenargenisligi = 0
        cubukrengi = acikmavi
        cubukrengi2 = acikyesil
        kirmiziyazi = kirmizi
        aramarengi = koyugri
        seffaflik = 1
    #191414
    #1d1f21
    def ekrbasla():
        root = tk.Tk()
        root.title(f"AcemTube Başlatılıyor...")
        root.resizable(False, False)
        yer = str(root.winfo_screenwidth()/2 - 350/2).split(".")[0]
        yer1 = str(root.winfo_screenheight()/2 - 90/2).split(".")[0]
        root.geometry(f"350x90+{yer}+{yer1}")
        root.attributes("-alpha", 0)
        root.overrideredirect(1)
        canvas = tk.Canvas(root, height=90, width=350, background=acikgri2)
        canvas.pack()
        #baslikutu = tk.Frame(root, bg="#2082b2")
        #baslikutu.place(relwidth=1, relheight=0.1)
        #008000
        #313542
        baslikutu1 = tk.Frame(root, bg=arkaplan)
        baslikutu1.place(relwidth=1, relheight=1)
        if jreem:
            baslik = "jreemTube"
        else:
            baslik = "AcemTube"
        baslik = tk.Label(baslikutu1, text=baslik, bg=arkaplan, fg=baslikyazirengi)
        baslik.config(font=("Montserrat ExtraBold", "28", "bold italic"))
        baslik.place(relwidth=0.65, relheight=0.75, relx=0.299)
        frm= tk.Frame()
        if jreem:
            logo = ImageTk.PhotoImage(Image.open("jreem.png"))
        else:
            logo = ImageTk.PhotoImage(Image.open("acemtubes.png"))
        rlbl = tk.Label(baslikutu1, image=logo, bg=arkaplan ,fg=acikgri2)
        rlbl.place(relwidth=0.31, relheight=0.78)
        s1 = ttk.Style()
        s1.theme_use("clam")
        s1.configure("red.Horizontal.TProgressbar", foreground=acikgri2, background=cubukrengi, troughcolor=koyugri, bordercolor=cubukrengi, darkcolor=cubukrengi, lightcolor=cubukrengi)

        acprgs = ttk.Progressbar(baslikutu1, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=350, mode="determinate")
        acprgs.place(rely=0.791)
        def ekr():
            ekran = True 
            while ekran:
                try:
                    soz = get_yuzde()
                    if "yuzde" in soz:
                        if soz["yuzde"] != acprgs['value']:
                            eski = acprgs['value']
                            acprgs['value'] = soz["yuzde"]
                            print(soz["yuzde"])
                            print("Yüzde Güncellendi: %" + str(eski) + "=> %" + str(soz["yuzde"]))
                        if soz["yuzde"] == 500:
                            acprgs.destroy()
                            root.destroy()

                            break
                    else:
                        print("yüzde bulunamadı")
                        time.sleep(0.5)
                    time.sleep(0.1)
                except Exception as e:
                    print("Hata Oluştu. İlk Açılış Olabilir. Hata: " + str(e))
                    time.sleep(0.5)

        def transparentles():
            root.attributes("-alpha", 0)
            time.sleep(0.07)
            root.attributes("-alpha", 0.1)
            time.sleep(0.07)
            root.attributes("-alpha", 0.2)
            time.sleep(0.07)
            root.attributes("-alpha", 0.3)
            time.sleep(0.07)
            root.attributes("-alpha", 0.4)
            time.sleep(0.07)
            root.attributes("-alpha", 0.5)
            time.sleep(0.07)
            root.attributes("-alpha", 0.6)
            time.sleep(0.07)
            root.attributes("-alpha", 0.7)
            time.sleep(0.07)
            root.attributes("-alpha", 0.8)
            time.sleep(0.07)
            root.attributes("-alpha", 0.9)
            time.sleep(0.07)
            root.attributes("-alpha", seffaflik)

        t1 = threading.Thread(target=ekr)
        t1.start()

        t2 = threading.Thread(target=transparentles)
        t2.start()
        root.mainloop()

    t0 = threading.Thread(target=ekrbasla)
    t0.start()

acts_start()

