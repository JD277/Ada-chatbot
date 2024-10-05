import pyaudio
import speech_recognition as sr
from grabar_audio2 import record_prompt
from app2 import answer
# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
archivo = "prompt.wav"

recognizer = sr.Recognizer()
microphone = sr.Microphone()
def listen_for_wake_word():
    
    """Continuously listens for the wake word 'Hey ADA'."""
    with microphone as source:
        print("Listening for wake word 'Hey Eva'...")
        while True:
            audio_data = recognizer.listen(source,timeout=10, phrase_time_limit=10)
            try:
                # Recognize the speech using Google Speech Recognition
                text = recognizer.recognize_google(audio_data)
                print(f"Heard: {text.lower()}")
                if "hey eva" in text.lower():  # If wake word is detected
                    print("Wake word detected!")
                    record_prompt()
                    answer()
                    break
            except sr.WaitTimeoutError:
                print("Listening timeout... continuing")
            except sr.UnknownValueError:
                pass  # Ignore unrecognized speech
            except sr.RequestError as e:
                print(f"Error with recognition service: {e}")

listen_for_wake_word()


