import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import googlesearch
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'poornima' in command:
                command = command.replace('poornima','')
                print(command)

    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'heck' in command:
        person = command.replace('heck','')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'on a date' in command:
        talk('sorry, I have a headache today, will plan this later')
    elif 'are you single' in command:
        talk('No, I am in a relationship with wifi')
    elif 'i love you' in command:
        talk('Sorry, I have a boyfriend, and you deserve someone better')
    elif 'date' in command:
        dt = datetime.datetime.now().strftime('%d/%m/%Y')
        print(dt)
        talk('Current Date is ' + dt)
    elif 'joke' in command:
        #print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'know' in command:
        talk(googlesearch.search())
    elif 'good night' in command:
        talk('Good Night Baby... Sweet Dreams And take Care, I think its the right time to go on the bed')
    elif 'bhai' in command:
        i=1
        if i==1:
            talk('Byyeeee baby')
            pass
    else:
        talk('Please say the command again.')

while True:

    run_alexa()

