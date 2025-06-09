import asyncio
import websockets
import base64
import json
import random
import smtplib
import datetime
from email.message import EmailMessage
import threading
import time
print("==================/AcemTube Lisans Sunucusu\\==================")
#mail_adres = "acemtubedestek@gmail.com"
#mail_password = "agegsdgsrgsseg"
#domain = "smtp.gmail.com"
eport = 465
email_adres = "AcemTube@outlook.com"
edomain ="smtp.office365.com"
eport = 587
email_password = "drgrsrgesgswgwgl"

def loginlog(klad, sif, hwid, cvp="Yok"):
  logtxt = "\n" + str(datetime.datetime.utcnow() + datetime.timedelta(hours=3)) + ": " + str(klad) + " , " + str(sif) + " , " + str(hwid) + " , " + str(cvp)
  print(logtxt)
  oku = open("loginlog.loginlog","r")
  okunan = oku.read()
  oku.close()
  loginfile = open("loginlog.loginlog","w")
  loginfile.write(okunan + logtxt)
  loginfile.close()

def eposta_al(klad=None):
  with open('epostalar.json', 'r') as f:
      emdp = json.load(f)
  print(klad)
  eposta = emdp[klad]
  return eposta

def kodyolla(eposta=None, klad=None, kod=None):
  msg = EmailMessage()
  msg['Subject'] = 'AcemTube Doğrulama Kodun!'
  msg['From'] = "AcemTube Doğrulama"
  msg['Sender'] = email_adres
  msg['To'] = eposta
  kodr = str(kod)[0:3] + "-" + str(kod)[3:6]
  f = open("index.html", "r")
  epostacontent = f.read().replace("{kod}", str(kodr)).replace("{kadı}", klad)
  msg.add_alternative(epostacontent, subtype='html')
                          
  with smtplib.SMTP(edomain, eport) as smtp:
    smtp.starttls()
    smtp.login(email_adres, email_password)
    smtp.send_message(msg)

def hataemail(hatablg=None):
  bilgiler = hatablg.split("' '")
  klad = bilgiler[0].strip("'")
  print("klad " + klad)
  destekkod = bilgiler[2]
  tarih = bilgiler[1]
  ver = bilgiler[4]
  isl = bilgiler[3]
  mod = bilgiler[6]
  eposta = eposta_al(klad)
  msg = EmailMessage()
  msg['Subject'] = 'AcemTube Hata Destek Kodun!'
  msg['From'] = "AcemTube Destek"
  msg['To'] = eposta
  kodr = destekkod
  f = open("hata.html", "r")
  epostacontent = f.read().replace("{kod}", str(kodr)).replace("{kadı}", klad).replace("{islsis}", isl).replace("{zmn}", tarih).replace("{actmod}", mod).replace("{vers}", ver)
  msg.add_alternative(epostacontent, subtype='html')
                          
  with smtplib.SMTP_SSL(edomain, eport) as smtp:
    smtp.starttls()
    smtp.login(email_adres, email_password)
    smtp.send_message(msg)
  
async def dogrula(websocket, path):
    
    print(str(websocket.remote_address) + " İle Bağlantı Kuruldu.")
    istekraw = await websocket.recv()
    
    if str(istekraw) != "ping":
      print(f"Gelen Şifreli Bilgiler: " + str(istekraw))
    if "makinesil-" in str(istekraw):
      klad = istekraw.split("-")[-1]
      
      with open('lisanslar.json', 'r') as f:
        hwdp = json.load(f)
        drm = hwdp[klad][-1]
        prl = hwdp[klad].split("//")[0]
        
      hwdp[klad] = prl + "//" + "//" + drm
      
      with open('lisanslar.json', 'w') as f:
        json.dump(hwdp, f, indent=4)
    elif "makinekle-" in str(istekraw):
      print("Hwid Eklenme İStendi")
      istekslpit = istekraw.split("makinekle-")[-1]
      klad = istekslpit.split("|")[0]
      hw = istekslpit.split("|")[1]
      pcname = hw = istekslpit.split("|")[-1]
      print(str(klad) + str(hw) + " Eklenior")
      with open('lisanslar.json', 'r') as f:
          kljson = json.load(f)
      
      kullanıcı = kljson[klad].split("//")
      
      hwidlist = kullanıcı[1].split("/")
      print(hwidlist) 
      
      print("hwid yazılıyor...")
      hwidlist.append(str(hw))
      dumphwlist = "/".join(hwidlist)
      with open('lisanslar.json', 'r') as f:
          hwdz = json.load(f)
      hwdz[klad] = kullanıcı[0] + "//" + dumphwlist + "//" + kullanıcı[2] 
      with open('lisanslar.json', 'w') as f:
          json.dump(hwdz, f, indent=4)
          print("hwid yazıldı")
    elif "hatabildir-" in str(istekraw):
      hatamsje = istekraw.strip("hatabildir-")
      hatamsj = hatamsje.replace("İ", "I").replace("ı", "i").replace("ğ", "g").replace("ü", "u").replace("ş", "s").replace("ö", "o").replace("ç", "c").encode('ascii', 'ignore').decode('ascii')
      bilgiler = hatamsj.split("' '")
      klad = bilgiler[0].strip("'")
      tarih = bilgiler[1]
      destekkod = bilgiler[2]
      mod = bilgiler[6]
      ver = bilgiler[4]
      isl = bilgiler[3]
      hwid = bilgiler[7].strip("'")
      hata = bilgiler[5]
      
      oku = open("hata-bildirme.hatalog","r")
      okunan = oku.read()
      oku.close()
      hatafile= open("hata-bildirme.hatalog","w")
      yazilcak = f"""\n'{destekkod}':<
          klad:'{klad}',
          tarih:'{tarih}',
          hata:'{hata}',
          mod:'{mod}',
          ver:'{ver}',
          os:'{isl}',
          hwid:'{hwid}'
>"""
      print("Bildirilen Hata Raporu:" + yazilcak)
      hatafile.write(okunan + yazilcak)
      hatafile.close()
      print("Bir hata bildirildi: " + hatamsje)
      print(f"{klad}'a Eposta Yollanıyor...'")
      hataemail(hatamsje)
      print(f"{klad}'a Eposta Yollandı.")
      
    elif str(istekraw) == "ping":
      await websocket.send(f"pong")
    else:
      istekf = str(istekraw).replace("b'", "").strip("'")
      istek = str(base64.b64decode(istekf)).replace("b'", "").strip("'")
      print(str(istek) + " deşifre edildi. giriş deneniyor.")
    
      blgler = istek.split("<///>")
      klad = blgler[0]
      prl = blgler[1]
      hwid = blgler[2]

      print(blgler)
      print(klad + " (" + str(websocket.remote_address[0]) + ")" + f" giriş yapmaya çalışıyor... ({prl})({hwid})")
      with open('lisanslar.json', 'r') as f:
          kljson = json.load(f)
      if klad in kljson:
          print(klad + " Kullanıcısı Bulundu " + prl + " parolası deneniyor...")
          kullanıcı = kljson[klad].split("//")
          if kullanıcı[0] == prl:
              hwidlist = kullanıcı[1].split("/")
              print(hwidlist)
              if kullanıcı[2] == "1" or kullanıcı[2] == "7":
                  if hwid in hwidlist:
                      if kullanıcı[2] == "1":
                        await websocket.send("1")
                      elif kullanıcı[2] == "7":
                        await websocket.send("7")
                        
                      print(klad + " Kullanıcısına izin verildi. Hwid listede zaten var.")
                      loginlog(klad, prl, hwid, kullanıcı[2])
                  else:
                      with open('hesaplimit.json', 'r') as f:
                          limitjson = json.load(f)
                      limit = limitjson[klad]
                      if '' in hwidlist and len(hwidlist) > 1:
                          hwidlist.pop(0)
                          print("hwid listesinden boşluk kesildi: " + str(hwidlist))
                      if limit > len(hwidlist):
                          with open('epostalar.json', 'r') as f:
                            emdp = json.load(f)
                          eposta = emdp[klad]
                          
                          
                          kod = random.randint(100000 , 999999)
                          alıcılar = []
                          if kullanıcı[2] == "1":
                            await websocket.send(f"[6]-{kod}")
                            gond = f"[6]-{kod}"
                          elif kullanıcı[2] == "7":
                            await websocket.send(f"[7]-{kod}")
                            gond = gond = f"[7]-{kod}"
                          print(f"{klad} Doğrulama Kodu İstemciye Gönderildi: {kod}")
                          kodyolla(eposta=eposta, klad=klad, kod=kod)
                          loginlog(klad, prl, hwid, gond)
                            
                      else:
                        if hwidlist == ['']:
                          with open('epostalar.json', 'r') as f:
                            emdp = json.load(f)
                            eposta = emdp[klad]


                          kod = random.randint(100000 , 999999)
                          alıcılar = []
                          if kullanıcı[2] == "1":
                            await websocket.send(f"[6]-{kod}")
                            gond = f"[6]-{kod}"
                          elif kullanıcı[2] == "7":
                            await websocket.send(f"[7]-{kod}")
                            gond = f"[7]-{kod}"
                            
                          print(f"{klad} Doğrulama Kodu İstemciye Gönderildi: {kod}")
                          kodyolla(eposta=eposta, klad=klad, kod=kod)
                          loginlog(klad, prl, hwid, gond)
                        else:
                          print("maksimum makine sayısı aşıldı.")
                          await websocket.send("3")
                          loginlog(klad, prl, hwid, "3")
              elif kullanıcı[2] == "0":
                  print("devre dışı")
                  await websocket.send("0")
                  loginlog(klad, prl, hwid, "0")
              elif kullanıcı[2] == "2":
                  print("fesh")
                  await websocket.send("2")
                  loginlog(klad, prl, hwid, "2")
          else:
              print(prl + " parolası yanlış")
              await websocket.send("5")
              loginlog(klad, prl, hwid, "5")
      else:
          await websocket.send("4")
          print(klad + " kullanıcı adı bulunamadı")
          loginlog(klad, prl, hwid, "4")
    
def trial_thread():
  kontrol = 0
  while True:
      print("Trialler Kontrol Ediliyor.")   
      with open('trial.json', 'r') as f:
        trialjson = json.load(f)
      trialsayi = 0
      iptal = 0
      for klad in trialjson:
        fark = datetime.datetime.utcnow() - datetime.datetime.fromisoformat(str(trialjson[klad]))
        if fark > datetime.timedelta(14):
          iptl = False

          with open('lisanslar.json', 'r') as f:
                kljson = json.load(f)
          if not kljson[klad].endswith("0"):
            print(f"{klad} İptal Edildi. ({fark})")
            iptl = True
          kullanıcı = kljson[klad].split("//")

          hwidlist = kullanıcı[1].split("/")

          dumphwlist = "/".join(hwidlist)
          with open('lisanslar.json', 'r') as f:
              hwdz = json.load(f)
          hwdz[klad] = klad + "//" + dumphwlist + "//" + "0"
          with open('lisanslar.json', 'w') as f:
             json.dump(hwdz, f, indent=4) 
          if iptl:
            iptal += 1
        trialsayi += 1
      kontrol += 1
      print(f"Trialler {kontrol}. Kez Kontrol Edildi. ({trialsayi}/{iptal}) Sunucu {(kontrol - 1) * 5} Dakikadır Yürüyor.")

      time.sleep(300)
        
trial_loop = threading.Thread(target=trial_thread)
trial_loop.start()


start_server = websockets.serve(dogrula, "0.0.0.0", 1234)
time.sleep(0.1)
print("Sunucu Başarıyla Başlatıldı.")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()