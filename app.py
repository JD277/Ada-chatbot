import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY="API_KEY"
client = OpenAI(api_key=OPENAI_API_KEY)

audio_file = open("audio.mp3","rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)
