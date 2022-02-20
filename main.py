# Import libraries using pip
# TODO: Do not forget to include these in the requirements.txt file
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os

# End import

# Give BOT the ability to speak
engine = pyttsx3.init('sapi5')  # Use Microsoft's voice API
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 0 for David (male) and 1 for Zira (female)


# Complete the speaking ability


# Call the speak function. This is the heart of our little friend
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# End the speak function


# Greet the user with a proper salutation
def greet():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak('Good Morning!')
    elif 12 <= hour < 6:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('My name is Morpheus and I am your AI assistant')


# End the greeting section

# Add a path to file in case there is none
def addDir():
    ourDir = str(
        input('Please add the required directory to the path as shown by the format below:\nC:\\Users\\HP\\Music'))
    return ourDir


# Stop adding files


# Simple yes or no function
def answer(question):
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
# End yes or no function

# Take input commands via microphone of the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        '''Through the statement "r.pause_threshold", we continue to consider the phrase as a single command even with a pause time of 1 second in between
        You can check the definition of the function by navigating to init.py'''
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Working on it...')
        query = r.recognize_google(audio, language='en-in')
        # print(f"User said: {query}")
        # speak(query)
    except Exception as e:
        # print(e)  # This command prints out the error that occurred. Enable it for development purposes
        # print("Internal error occurred. Please try again")
        return "Error"
    return query


# Complete taking input commands


# Let the show begin :D
if __name__ == "__main__":
    # greet()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            print(f"According to wikipedia{results}")
            speak(f"According to wikipedia{results}")
        elif 'youtube' in query:
            query = query.replace("youtube", "").rstrip()
            if (query == "") or (query == "open"):
                webbrowser.open('youtube.com')
            else:
                query = query.replace(" ", "+").rstrip()
                webbrowser.open(f"www.youtube.com/results?search_query={query}")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Music'
            question = 'Do you wish to change the music path?'
            reply = answer(question)
            if reply:
                music_dir = addDir()
                pass
            elif not reply:
                pass
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'twitch' in query:
            speak('opening twitch')
            query = query.replace("twitch", "").rstrip()
            if (query == "") or (query == "open"):
                webbrowser.open('www.twitch.tv')
            else:
                query = query.replace(" ", "+").rstrip() and query.replace("open", "+")
                webbrowser.open(f"https://www.twitch.tv/search?term={query}")