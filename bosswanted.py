from labyrinthloop import click
import pyautogui
import os
import time

PATH = os.path.dirname(__file__) + '\\images\\'
# print("DEBUG: " + PATH)
IMAGEFILE = 'bosswanted.png'
IMAGE_FULLSCREEN = 'boss_100.png'
image = PATH + IMAGEFILE
image_fs= PATH + IMAGE_FULLSCREEN

enter_x , enter_y =  pyautogui.position()
count = 0
ans = input('click(y) or no?, shutdown or no? ').lower().split(',') + [" ", " "]

print('Starting with shutdown at 200') if ans[1] == 'y' else print('Starting')

try:
    while True:
        if pyautogui.locateOnScreen(image):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image)
                click(x,y)
                time.sleep(0.2)
                click(x,y-45)
                # click(x-120,y-86)
                if ans[0] == 'y':
                    click(enter_x,enter_y)
                else:
                    pyautogui.moveTo(enter_x,enter_y)
            except: continue
        elif pyautogui.locateOnScreen(image_fs):
            try:
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image_fs)
                click(x,y)
                time.sleep(0.2)
                click(x,y-250)
                if ans[0] == 'y':
                    click(enter_x,enter_y)
                else:
                    pyautogui.moveTo(enter_x,enter_y)
               
            except: continue
        else:
            # message = 'Not found'
            # print(count, end='')
            # print('\b' * len(str(count)), end='', flush=True)
            print(count)
            count += 1
            enter_x , enter_y =  pyautogui.position()
            if ans[1] == 'y' and count > 200:
                os.system('shutdown.exe /s')
                break
except KeyboardInterrupt:
    print('\n\nDone')
