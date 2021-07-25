from labyrinthloop import click, pause
import pyautogui
import os
import time

PATH = os.getcwd() + '\\images\\'
IMAGEFILE = 'image4.png'
image = PATH + IMAGEFILE

enter_x , enter_y =  pyautogui.position()
count = 0
master = 0
print('Starting')
try:
    while True:
        if pyautogui.locateOnScreen(image):
            count = 0
            x, y = pyautogui.locateCenterOnScreen(image)
            click(x,y)
            time.sleep(0.2)
            click(x+95,y)
            pyautogui.moveTo(enter_x,enter_y)
            master+=1
        else:
            # message = 'Not found'
            # print(count, end='')
            # print('\b' * len(str(count)), end='', flush=True)
            print(count)
            count += 1
            enter_x , enter_y =  pyautogui.position()
           
except KeyboardInterrupt:
    print('\n\nDone {}'.format(master))
