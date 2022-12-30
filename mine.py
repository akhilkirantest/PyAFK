import pyautogui
import time
time.sleep(15)
for x in range(1,3):
    pyautogui.moveRel(0, 500, duration = 1)
    pyautogui.leftClick(duration = 3)
    pyautogui.moveRel(0, -500, duration = 1)
    pyautogui.leftClick(duration = 3)
