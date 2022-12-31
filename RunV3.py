import pyautogui
import time
import pyttsx3
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
SpeakText('Place the mouse pointer on application one')
time.sleep(2)
Pos1=pyautogui.position()
SpeakText('Registered application one')
print(pyautogui.position())
SpeakText('Place the mouse pointer on application two')
time.sleep(2)
Pos2=pyautogui.position()
SpeakText('Registered application two')
print(pyautogui.position())
SpeakText('registration complete,starting program')
##############################################




for x in range(1,10):
    time.sleep(1)
    pyautogui.moveTo(Pos1, duration = 1)
    pyautogui.click(Pos1)
    time.sleep(5)
    pyautogui.moveTo(Pos2, duration = 1)
    pyautogui.click(Pos2)
    time.sleep(4)