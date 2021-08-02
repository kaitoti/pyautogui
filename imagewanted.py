from labyrinthloop import click
import pyautogui
import os
import time

PATH = os.getcwd() + '\\images\\'
IMAGEFILE = 'sawanted.png'
IMAGEFILE2 = 'quest_wanted.png'
IMAGEFILE3 = 'claim_wanted.png'
IMAGEFILE4 = 'go_wanted.png'

image = PATH + IMAGEFILE
image2 = PATH + IMAGEFILE2
image3 = PATH + IMAGEFILE3
image4 = PATH + IMAGEFILE4

enter_x , enter_y =  pyautogui.position()
count = 0
master = 0
# data = []
print('Starting')

def check_quest():
    if pyautogui.locateOnScreen(image2):
        init_x,init_y = pyautogui.locateCenterOnScreen(image2)
        return init_x,init_y+30


try:
    
    while True:
        if check_quest():
            initial_x,initial_y = check_quest()
            print('In a wanted quest area\nSTARTING')
            break
        else:
            print('Not in a wanted quest area')
    click(initial_x,initial_y)
    while True:
        if pyautogui.locateOnScreen(image):
            print('\b' * len(str(count)), end='', flush=True)
            count = 0
            x, y = pyautogui.locateCenterOnScreen(image)
            click(x,y)
            time.sleep(0.5)
            click(initial_x,initial_y)
            pyautogui.moveTo(enter_x,enter_y)
            master+=1
            # continue
            # if master == 10: break
        elif pyautogui.locateOnScreen(image3):
            x, y = pyautogui.locateCenterOnScreen(image3)
            click(x,y)
            time.sleep(1.1)
            click(x,y)
            time.sleep(0.5) 
            click(x,y)
            # time.sleep(0.5) 
            # click(x,y)
            
            time.sleep(0.5)
            click(initial_x,initial_y)
            pyautogui.moveTo(enter_x,enter_y)

        else:
            # message = 'Not found'
            print(count, end='')
            print('\b' * len(str(count)), end='', flush=True)
            # print(count)
            count += 1
            enter_x , enter_y =  pyautogui.position()

except KeyboardInterrupt:
    print('\nDone {}'.format(master))
    # try:
    #     print('Averaged {} in '.format(sum(data)/len(data),len(data)))
    # # except ZeroDivisionError: pass
    # except: pass
