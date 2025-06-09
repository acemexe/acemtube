import json
import subprocess

def acts_guncelle(deger=None, bitir = False, ekle = True):
    print("Yüzde Güncelleniyor: " + f"{deger}, {bitir}, {ekle}")
    if bitir:
        subprocess.call("TASKKILL /F /IM acts.exe", shell=True)
    elif ekle:
        with open('data.json', 'r') as f:
            acts_yuzde = json.load(f)
        acts_yuzde["yuzde"] += deger
        with open('data.json', 'w') as f:
            json.dump(acts_yuzde, f, indent=4)
    else:
        with open('data.json', 'r') as f:
            acts_yuzde = json.load(f)
        acts_yuzde["yuzde"] = deger
        with open('data.json', 'w') as f:
            json.dump(acts_yuzde, f, indent=4)
