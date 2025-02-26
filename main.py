#packages required for the project are speech_recognition, pyttsx3, webbrowser is in build package,setuptools, pyaudio,
import speech_recognition as sr 
import pyttsx3 
import webbrowser 
import os
import musicLibrary
# Initialize speech recognizer and text-to-speech engine
recgnizer = sr.Recognizer()
engine = pyttsx3.init()

def speek(text):
    # Function to make the assistant speak
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    # Function to process user commands
    if "open google" in c.lower():
        speek("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speek("Opening Youtube")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        speek("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "Radhe Radhe" in c.lower():
        speek("Radhe Radhe Boss")
    elif c.lower().startswith("play"):
        # Extract the song name from the command
        song= c.lower().split(" ")[1]
        link = musicLibrary.music(song) # Fetch the music link from library
        webbrowser.open(link)
    
if __name__ =="__main__":
    speek("Initializing Jarvis.....!!!!")
    #listen for the wake word "Jarvis"
    while True:
        r = sr.Recognizer()
        print("recognizer...")
        try:
            with sr.Microphone() as source:
                print("Listening....") 
                audio = r.listen(source, timeout = 2) # Capture audio from the microphone
            word = r.recognize_google(audio) # Convert speech to text
            if(word.lower() == "jarvis"): # If the wake word is detected
                speek("Jarvis active")
                speek("How can I help you sir")
                with sr.Microphone() as source:
                    print("jarvis active....") 
                    audio = r.listen(source)
                    command = r.recognize_google(audio) # Capture user command

                    processcommand(command) # Process the command
        except Exception as e:
            print("Error; {0}".format(e)) # Print any errors that occur