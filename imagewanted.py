from labyrinthloop import click, pause
import pyautogui
import os
import time

PATH = os.getcwd() + '\\images\\'
IMAGEFILE = 'sawanted.png'
IMAGEFILE2 = 'quest_wanted.png'
image = PATH + IMAGEFILE
image2 = PATH 

enter_x , enter_y =  pyautogui.position()
count = 0
master = 0
data = []
print('Starting')
try:
    while True:
        if pyautogui.locateOnScreen(image):
            count = 0
            x, y = pyautogui.locateCenterOnScreen(image)
            print(x,y)
            click(x,y)
            time.sleep(2)
            print(x,y)
            click(x-512,y-287)
            print(x-512,y-287)
            pyautogui.moveTo(enter_x,enter_y)
            master+=1
            continue
            # if master == 10: break
        else:
            # message = 'Not found'
            # print(count, end='')
            # print('\b' * len(str(count)), end='', flush=True)
            print(count)
            count += 1
            enter_x , enter_y =  pyautogui.position()

except KeyboardInterrupt:
    print('\nDone {}'.format(master))
    try:
        print('Averaged {} in '.format(sum(data)/len(data),len(data)))
    except ZeroDivisionError: pass
