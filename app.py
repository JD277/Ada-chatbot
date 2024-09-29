import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY="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"
client = OpenAI(api_key=OPENAI_API_KEY)

audio_file = open("audio.mp3","rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)
