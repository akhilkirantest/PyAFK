import pyautogui
import time
Pos1=(370,824)
Pos2=(554,825)

time.sleep(5)
for x in range(1,10):
    time.sleep(2)
    pyautogui.moveTo(Pos1, duration = 1)
    pyautogui.click(Pos1)
    time.sleep(2)
    pyautogui.moveTo(Pos2, duration = 1)
    pyautogui.click(Pos2)