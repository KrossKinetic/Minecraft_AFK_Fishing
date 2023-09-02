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
                if x == True:
                    #y = pyautogui.pixel(1722,841) 
                    mouse.click(Button.right)
                    time.sleep(2)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

print("Hey! This is an afk fishing program.")
print("To start the program, press run and then open up minecraft.\n After opening the world and standing at the fishing spot ( look at the video ) Simply press the left alt key to start the program.")
print("To close the program, simply kill the code.")


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()


