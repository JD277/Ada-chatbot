import os
import google.generativeai as genai

API_KEY= ""
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel("gemini-1.5-flash")
def answer():
    myfile = genai.upload_file("graba.wav")
    result = model.generate_content([ myfile,"Que dice este audio ?"])
    result2 = model.generate_content(result.text)
    print(result2.text)