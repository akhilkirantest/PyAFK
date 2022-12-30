import pyautogui
import time
time.sleep(5)
Pos1=pyautogui.position()
print(pyautogui.position())
time.sleep(5)
Pos2=pyautogui.position()
print(pyautogui.position())

##############################################

time.sleep(5)
for x in range(1,10):
    time.sleep(2)
    pyautogui.moveTo(Pos1, duration = 1)
    pyautogui.click(Pos1)
    time.sleep(2)
    pyautogui.moveTo(Pos2, duration = 1)
    pyautogui.click(Pos2)