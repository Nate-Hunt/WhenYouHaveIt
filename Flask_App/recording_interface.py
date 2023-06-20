"""This Flask app controls the audio recording in the index file."""
import pyaudio
import wave
import os
from flask import Flask, render_template, request

app = Flask(__name__)

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

app = Flask(__name__, template_folder='Templates')
@app.route('/')
def index():
    """Renders the template html document"""
    return render_template('index.html')

@app.route('/record', methods=['POST'])
def record():
    """A uses the created variables to record a 5-second chunk of audio"""
    frames = []

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save audio to file
    filename = 'recording.wav'
    filepath = os.path.join(app.static_folder, filename)
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return filename

@app.route('/playback')
def playback():
    filename = 'recording.wav'
    filepath = os.path.join(app.static_folder, filename)
    return render_template('playback.html', audio_file=filename)

if __name__ == '__main__':
    app.run()
