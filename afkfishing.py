from pynput.mouse import Button, Controller
from pynput import keyboard
import pyautogui
import time

mouse = Controller()
    
def on_press(key):
    try:
        if key == keyboard.Key.alt_l:
            y = pyautogui.pixel(1722*1.33,841*1.9)
            print("Fishing Rod found. Starting to fish.")
            while True:
                x = pyautogui.pixelMatchesColor(1722*1.33, 841*1.9, y,tolerance=40)
                if x == True:
                    mouse.click(Button.right)
                    time.sleep(2)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

print("Hey! This is an afk fishing program.")
print("To start the program, press run and then open up minecraft.\n After opening the world and standing at the fishing spot ( look at the video ) Simply press the left alt key to start the program.")
print("To close the program, simply kill the code.")
#display=input("Enter the display resolution seperated by x: ").split('x')
while True:
    pyautogui.position


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
