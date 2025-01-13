import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input and return it as text."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        talk("There seems to be a connection issue. Please try again later.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

def tell_time():
    """Tell the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    talk(f"The current time is {current_time}")

def tell_date():
    """Tell today's date."""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    talk(f"Today's date is {current_date}")

def search_web(query):
    """Perform a web search."""
    talk(f"Searching the web for {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def voice_assistant():
    """Main function to handle voice commands."""
    talk("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        
        if not command:
            continue  # Skip empty commands
        
        if "hello" in command:
            talk("Hello! How can I assist you today?")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search" in command:
            talk("What would you like to search for?")
            query = listen()
            if query:
                search_web(query)
        elif "exit" in command or "quit" in command:
            talk("Goodbye! Have a great day!")
            break
        else:
            talk("I didn't understand that. Could you please repeat?")

# Run the assistant
if __name__ == "__main__":
    voice_assistant()
