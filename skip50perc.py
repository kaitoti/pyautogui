"""this file is for 50 percent on chrome in the h5-sao domain"""

from labyrinthloop import click
import pyautogui
import time 
import os

PATH = os.path.dirname(__file__) + '\\images\\'
IMAGEFILE = 'skipQuest.PNG'
IMAGEFILE2 = 'close_50.PNG'
IMAGEFILE2_2 = 'close_50_2.PNG'
IMAGEBATTLE = 'battle_50.PNG'
image = PATH + IMAGEFILE
image2 = PATH + IMAGEFILE2
image2_2 = PATH + IMAGEFILE2_2
image3 = PATH + IMAGEBATTLE

enter_x , enter_y =  pyautogui.position()
count = 0

try:
    while True:
        if pyautogui.locateOnScreen(image):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image)
                click(x,y)
                # time.sleep(0.2)
                pyautogui.moveTo(enter_x,enter_y)
            except: continue
        elif pyautogui.locateOnScreen(image2):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image2)
                click(x,y)
                # time.sleep(0.2)
                pyautogui.moveTo(enter_x,enter_y)
            except: continue
        elif pyautogui.locateCenterOnScreen(image3):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image3)
                click(x,y)
                # time.sleep(0.2)
                pyautogui.moveTo(enter_x,enter_y)
            except: continue
        elif pyautogui.locateCenterOnScreen(image2_2):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image2_2)
                click(x,y)
                # time.sleep(0.2)
                pyautogui.moveTo(enter_x,enter_y)
            except: continue
        else:
            print(count)
            count += 1
            enter_x , enter_y =  pyautogui.position()
except KeyboardInterrupt:
    print('\nDone')
            
