from pynput.mouse import Button, Controller
from pynput import keyboard
import pyautogui
import time

mouse = Controller()
    
def on_press(key):
    try:
        if key == keyboard.Key.alt_l:
            y = pyautogui.pixel(1722,841)
            #print(y)
            print("Fishing Rod found. Starting to fish.")
            while True:
                #print("color got: " + str(y)w da )
                x = pyautogui.pixelMatchesColor(1722, 841, y,tolerance=40)
                '''z = pyautogui.pixel(1722,841)
                print("color need: " + str(z))
                print(x)'''
                if x == True:
                    #y = pyautogui.pixel(1722,841) 
                    mouse.click(Button.right)
                    time.sleep(2)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()


