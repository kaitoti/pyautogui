"""Auto battle in World Boss 100% reso in chrome h5-sao domain"""
from labyrinthloop import click
import pyautogui
import os
import time

PATH = os.path.dirname(__file__) + '\\images\\'
IMAGEFILE = 'start_worldboss.PNG'
IMAGE_FULLSCREEN = 'boss_100.png'

image = PATH + IMAGEFILE
imagefs = PATH + IMAGE_FULLSCREEN

enter_x , enter_y =  pyautogui.position()
count = 0
print('Starting')

try:
    while True:
        if pyautogui.locateOnScreen(image):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image)
                click(x,y)
                time.sleep(0.2)
                # click(x-120,y-86)
                pyautogui.moveTo(enter_x,enter_y)
            except: continue
        elif pyautogui.locateOnScreen(imagefs):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(imagefs)
                click(x,y)
                time.sleep(0.2)
                # click(x-120,y-86)
                pyautogui.moveTo(enter_x,enter_y)
            except: continue
        else:
            # message = 'Not found'
            # print(count, end='')
            # print('\b' * len(str(count)), end='', flush=True)
            print(count)
            count += 1
            enter_x , enter_y =  pyautogui.position()
except KeyboardInterrupt:
    print('\n\nDone')
