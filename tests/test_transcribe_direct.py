import requests

def test_transcribe_direct():
    url = "http://127.0.0.1:8000/transcribe"
    audio_path = "tests/test_file_converted.wav"

    with open(audio_path, "rb") as f:
        files = {"audio": ("test_file_converted.wav", f, "audio/wav")}
        response = requests.post(url, files=files)
        print("Status Code:", response.status_code)
        try:
            print("Response JSON:", response.json())
        except Exception as e:
            print("Failed to parse JSON response:", e)
            print("Response text:", response.text)

if __name__ == "__main__":
    test_transcribe_direct()
