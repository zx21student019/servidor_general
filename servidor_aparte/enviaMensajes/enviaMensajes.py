#!C:\Users\mores\AppData\Local\Microsoft\WindowsApps\python
 
#@python.coder_
import pyautogui as pg
import time
from random import *
 
time.sleep(3)

mensaje = ["mensaje1","mensaje2","mensaje3","mensaje4"]
for i in range(10):
    numeroRandom = randint(0,3)
    
    pg.write(mensaje[numeroRandom])
    pg.press('enter')