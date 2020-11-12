from ctypes import windll, Structure, c_long, byref
import pyautogui as pp
pp.FAILSAFE = False
print("Move your mouse to top left corner to refresh the page its that simple lmfao")

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return f'{pt.x}{pt.y}'

def refresher():
    pp.press("f5")
    print("refreshed")
    
while True:
    pos = int(queryMousePosition())
    if pos < 100:
        refresher()
