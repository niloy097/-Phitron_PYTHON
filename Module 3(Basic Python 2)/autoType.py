import pyautogui
from time import sleep
sleep(10)
for i in range(1, 10):
    pyautogui.write("Sending Message Automatically", interval=0.25)
    pyautogui.press('enter')
