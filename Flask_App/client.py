import requests

URL = "http://127.0.0.1:5408/record_and_store"
TEST_AUDIO_FILE_PATH = "Flask_App/AudioFiles/Genesis 1_1.wav"

if __name__ == "__main__":
    
    audio_file = open(TEST_AUDIO_FILE_PATH, "rb")
    values = {"file": (TEST_AUDIO_FILE_PATH, audio_file, "audio/wav")}
    response = requests.post(URL, files=values)
    data = response.json()
    
    print("Your request is:", data)