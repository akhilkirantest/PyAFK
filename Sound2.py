import pyttsx3
MyText = 'hi Ayush, you are a genius. We are going out today. The lake seems to be a great place. are you coming ?'
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
SpeakText(MyText)