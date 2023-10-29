pip install pyaudio


import os
import pyaudio
import wave

# Parameters for audio recording
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1              # Mono recording
RATE = 44100              # Sample rate
CHUNK = 1024              # Chunk size (frames per buffer)
RECORD_SECONDS = 5       # Duration of recording (in seconds)

# Directory to save recordings
SAVE_DIR = "recordings"

# Create the recordings directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

def record_audio(filename):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    wf = wave.open(os.path.join(SAVE_DIR, filename), 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    filename = input("Enter a filename for the recording: ")
    record_audio(filename + ".wav")
