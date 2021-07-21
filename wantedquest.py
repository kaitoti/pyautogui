import time
import sys
import pyautogui
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

# 146,251
# 146,279
# 673,622
# 672,553
""" if not fullscreen """
enter_x , enter_y =  pyautogui.position()

current_pos = pyautogui.position()

def loop():
    global count
    
    while True:
        click(146,251)
        # click(enter_x,enter_y)
        pause(delaytime=10) #delaytime in seconds
        count += 1
        click(673,622)
        time.sleep(0.2)
        click(672,553)
        time.sleep(0.2)
        
        

def pause(delaytime):
    global enter_x , enter_y
    while delaytime > 0 :
        print(f"{delaytime}")
        time.sleep(1)
        delaytime -= 1
        # enter_x , enter_y =  pyautogui.position()
        
count = 0
    

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print(f"{((count *10)/60):.2f} minutes are done")
        sys.exit()