import os
import random
import ctypes
info = ctypes.windll.user32.MessageBoxW
liczba = random.randint(1,6)
if liczba == 1:
    info(None, 'Lul', 'DED', 0)
    os.system ("shutdown /s /t 1")
else:
    while(1):
        info(None, 'Lul', 'ZYJESZ', 0)