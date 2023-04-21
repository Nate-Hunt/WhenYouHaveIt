from flask import Flask, render_template, request
import pyaudio
import wave

app = Flask(__name__)

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

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
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return 'Audio recording saved as {}'.format(WAVE_OUTPUT_FILENAME)

if __name__ == '__main__':
    app.run(debug=True)
