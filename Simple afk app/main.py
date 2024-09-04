import time
import random
import pyautogui as pag
import readchar 
import sys


while True:
    x = random.randint(600,800)
    y = random.randint(600,800)
    pag.moveTo(x,y,0.5)
    key = readchar.readkey()
    if key == "x":
        print("you pressed ", key)
        print("Ending program")
        sys.exit()
    else:
        print("Wrong key, program continuing")
        
    time.sleep(2)
    

