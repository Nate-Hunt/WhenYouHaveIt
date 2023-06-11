import os
import random
import speech_recognition as sr
from flask import Flask, request, jsonify

app = Flask(__name__)

"""This application handles the microphone audio recording 
   and storing for the database application.
"""

@app.route("/record_and_store", methods=["POST"])

def record_and_store():
    #record, create audio file, and save it
    audio_file = request.files["file"]
    file_name = "temp_file" + str(random.randint(0, 10))
    audio_file.save(file_name)
    
    #transcribe into usable request for extraction
    r = sr.Recognizer()
    file = sr.AudioFile('file_name')
    
    with file as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        result = r.recognize_google(audio, language = 'en')
    os.remove(file_name)
    
    return jsonify(result)    
    
    #extract data and send sql query
    
    #return data
    
if __name__ == "__main__":
    app.run(debug=False)