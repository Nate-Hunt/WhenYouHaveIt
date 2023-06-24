import sys
import extraction
from creds import cred2
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_audio_input.html')

@app.route('/process', methods=['GET', 'POST'])
def process_transcript():
    if request.method == 'POST':
        transcript = request.form.get('transcript')
        if transcript:
            processed_result = process_transcript_function(cred2, transcript)
            return render_template('result.html', result=processed_result)
        else:
            return "Error: Transcript not found"
    else:
        # Handle GET request for /process route
        return render_template('result.html')

def process_transcript_function(inFile, transcript):
    # Your transcript processing logic goes here
    # ...

        result = extraction.extract(inFile, transcript)
        # Return the processed result
        print(result)
        return result

if __name__ == '__main__':
    app.run(debug=True)
