from labyrinthloop import click, pause
import pyautogui
import os
import time

PATH = os.getcwd() + '\\images\\'
IMAGEFILE = 'image4.png'
image = PATH + IMAGEFILE

def secondsToText(secs):
    days = secs//86400
    hours = (secs - days*86400)//3600
    minutes = (secs - days*86400 - hours*3600)//60
    seconds = secs - days*86400 - hours*3600 - minutes*60
    result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
    ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
    ("{0} minute{1}, ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
    ("{0:.2f} second{1}, ".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    return result

enter_x , enter_y =  pyautogui.position()
count = 0
master = 0
data = []
ans = input('Click(y) or not: ')
print('Starting')
start_time = time.perf_counter()
try:
    while True:
        if pyautogui.locateOnScreen(image):
            try:
                if count != 0: data.append(count)
                count = 0
                x, y = pyautogui.locateCenterOnScreen(image)
                click(x,y)
                time.sleep(0.2)
                click(x+95,y)
                if ans == 'y':
                    click(enter_x,enter_y)
                else:
                    pyautogui.moveTo(enter_x,enter_y)
                master+=1
                # if master == 10: break
            except: continue
        else:
            # message = 'Not found'
            # print(count, end='')
            # print('\b' * len(str(count)), end='', flush=True)
            print(count)
            count += 1
            enter_x , enter_y =  pyautogui.position()

except KeyboardInterrupt:
    end_time = time.perf_counter()
    print('\nDone {}'.format(master))
    try:
        print('Averaged {:.2f} in '.format(sum(data)/len(data),len(data)))
    except ZeroDivisionError:
        print('Did 0')
    
    print('Time elapsed\n{} '.format(secondsToText(end_time - start_time)))
