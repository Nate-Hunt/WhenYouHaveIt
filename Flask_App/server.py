import os
import random
import speech_recognition as sr
from flask import Flask, request, render_template

app = Flask(__name__)

"""
    This application handles the microphone audio recording 
    and storing for the database application.
"""

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/record_and_store", methods=["POST"])

def transcribe():
    result = record_and_store()
    return result

def record_and_store():
    #record, create audio file, and save it
    audio_file = request.files["file"]
    file_name = "temp_file" + str(random.randint(0, 10))
    audio_file.save(file_name)
    
    #transcribe into usable request for extraction
    r = sr.Recognizer()
    file = sr.AudioFile(file_name)
    
    with file as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        
    result = r.recognize_google(audio, language = 'en')
    os.remove(file_name)
    try:
        text = r.recognize_google(audio, language = 'en')
    except sr.UnknownValueError:
        return "Unable to recognize speech"
    except sr.RequestError as e:
        return f"Error: {str(e)}"
      
    return render_template("index.html", transcript=text)
    #extract data and send sql query
    
    #return data
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5409,debug=True)