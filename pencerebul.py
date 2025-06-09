import win32.lib.win32con as win32con, win32gui, win32process
import wmi

c = wmi.WMI()

def get_app_name(hwnd):
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
            exe = p.Name
            break
    except:
        return None
    else:
        return exe

pencereler = []
gizlenenler = []

def get_konsol_name():
    return gizlenenler
    
def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        pencereler.append(hwnd)

win32gui.EnumWindows(winEnumHandler, None)

#print(pencereler)

for pencere in pencereler:
    pencere_isim = win32gui.GetWindowText(pencere)
    if "acemtube.exe" in pencere_isim or "AcemTube" in pencere_isim or "acemtube" in pencere_isim or pencere_isim == "AcemTube" and not pencere_isim == "AcemTube ":
        #print(win32gui.GetWindowText(pencere) + "p")
        #print(get_app_name(pencere))
        uygad = get_app_name(pencere)
        pead = win32gui.GetWindowText(pencere)
        kontrol = False
        if get_app_name(pencere) == "acemtube.exe":
            kontrol = True
        if "acemtube.exe" in str(pead):
            kontrol = True
        if uygad == "WindowsTerminal.exe":
            kontrol = True
        if pencere_isim == "AcemTube ":
            kontrol = False
        if kontrol:
            win32gui.ShowWindow(pencere, win32con.SW_HIDE)
            gizlenenler.append(pencere)