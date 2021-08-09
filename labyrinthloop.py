import time
import sys, os
import pyautogui
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

def mouse_click():
    x,y = pyautogui.position()
    click(x,y)

def start_browser(ans='n'):
    if ans == 'y':
        os.system('start "" "chrome.exe" --new-window --app=https://saogamesource.heatgames.me/sao2/beta/play_pc.html & exit')


count = 0
enter_x , enter_y =  pyautogui.position()
delay = 5
# 1243,701
# while keyboard.is_pressed('q') == False:

def loop():
    global count
    global answer
    while True:
        click(1341,692)
        if answer == 'n' or answer == '':
            pyautogui.moveTo(enter_x,enter_y)
        elif answer == 'c':
            click(enter_x,enter_y)
        pause(delay) #delaytime in seconds
        count += 1
        click(1243,701)
        time.sleep(0.2)

def pause(delaytime):
    global enter_x , enter_y
    # while delaytime > 0 :
    for delay in range(delaytime,0,-1) :
        print(f"{delay}")
        time.sleep(1)
        # delaytime -= 1
        enter_x , enter_y =  pyautogui.position()
        

if __name__ == '__main__':
    try:
        answer2 = input("Open SAO?: (y)")
        # if answer2 == 'y':
        #     os.system('start "" "chrome.exe" --new-window --app=https://saogamesource.heatgames.me/sao2/beta/play_pc.html & exit')
        start_browser(answer2)
        answer = input("(C)lick or (N)ot: \n").lower()
        loop()
    except KeyboardInterrupt:
        print(f"{((count * delay)/60):.2f} minutes are done")
        sys.exit()
