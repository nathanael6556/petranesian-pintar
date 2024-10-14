import os
from os.path import splitext, abspath
from whisper_cpp_python import Whisper
from whisper_cpp_python.whisper_cpp import whisper_progress_callback


RAW_INPUT_PATH = abspath("./samples/Lecture04/DS-Lct04-Communication.mp3")
OUTPUT_PATH = "transcript.txt"
MODEL_PATH = "../ggml-small.bin"


# Convert audio to WAV
if not RAW_INPUT_PATH.endswith(".wav"):
    input_path, _ = splitext(RAW_INPUT_PATH)
    input_path += ".wav"
    status = os.system(f"ffmpeg -i '{RAW_INPUT_PATH}' -ar 16000 -ac 1 -c:a pcm_s16le {input_path}")
else:
    input_path = RAW_INPUT_PATH


def callback(ctx, state, i, p):
    print(i)


model = Whisper(MODEL_PATH)
model.params.progress_callback = whisper_progress_callback(callback)

transcript = model.transcribe(input_path, response_format='text', language='id')
print(transcript)
with open(OUTPUT_PATH, "w") as f:
    f.write(transcript)
