import pyaudio
import wave
import threading

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
archivo = "graba.wav"

# Initialize PyAudio and open stream
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

frames = []
recording = True

def record_audio():
    """Continuously record audio until 'recording' is set to False."""
    print("Recording... Press Enter to stop.")
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

def wait_for_enter():
    """Wait for user to press Enter to stop recording."""
    global recording
    input()  # Wait for Enter key
    recording = False  # Stop recording

# Start recording in a separate thread
recording_thread = threading.Thread(target=record_audio)
recording_thread.start()

# Wait for Enter key press to stop recording
wait_for_enter()

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()
print("Recording finished.")

# Save the recorded audio to a file
waveFile = wave.open(archivo, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()