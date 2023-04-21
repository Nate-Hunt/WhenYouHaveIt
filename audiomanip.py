import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

#Start recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    
#Stop recording
stream.stop_stream()
stream.close()
audio.terminate()

wavFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wavFile.setnchannels(CHANNELS)
wavFile.setsampwidth(audio.get_sample_size(FORMAT))
wavFile.setframerate(RATE)
wavFile.writeframes(b''.join(frames))
wavFile.close()

print("Your audio file was saved as '", WAVE_OUTPUT_FILENAME, "'")