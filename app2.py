import os
import google.generativeai as genai

API_KEY= "AIzaSyADUxbPyDR8uDvdcG-NiDbyg01HfRvkTBE"
genai.configure(api_key=API_KEY)

myfile = genai.upload_file("audio.mp3")
#print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content([ myfile,"Que dice este audio?"])
print(f"{result.text}")