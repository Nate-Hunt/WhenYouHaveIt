import requests

URL = "http://127.0.0.1:5000/record_and_store"
TEST_AUDIO_FILE_PATH = "AudioFiles/Exodus 16_4.m4a"

if __name__ == "__main__":
    
    audio_file = open(TEST_AUDIO_FILE_PATH, "rb")
    values = {"file": (TEST_AUDIO_FILE_PATH, audio_file, "audio/m4a")}
    response = requests.post(URL, files=values)
    data = response.json()
    
    print("Your request is:", data)