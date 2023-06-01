import pyaudio
import wave

# set up audio input parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

# create audio object
audio = pyaudio.PyAudio()

# start recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, input_device_index=0, frames_per_buffer=CHUNK)
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
stream.stop_stream()
stream.close()
audio.terminate()

# save audio to file
filename = 'test.wav'
wf = wave.open(filename, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# play back audio
wf = wave.open(filename, 'rb')
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
data = wf.readframes(CHUNK)
while data:
    stream.write(data)
    data = wf.readframes(CHUNK)
stream.stop_stream()
stream.close()
audio.terminate()
