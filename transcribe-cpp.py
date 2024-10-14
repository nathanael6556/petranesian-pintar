import os
from os.path import splitext, abspath
from whisper_cpp_python import Whisper
from whisper_cpp_python.whisper_cpp import whisper_progress_callback


INPUT_PATH = abspath("./samples/Lecture04/DS-Lct04-Communication.mp3")
MODEL_PATH = "../ggml-small.bin"


# Convert audio to WAV
if not INPUT_PATH.endswith(".wav"):
    output_path, _ = splitext(INPUT_PATH)
    output_path += ".wav"
    status = os.system(f"ffmpeg -i '{INPUT_PATH}' -ar 16000 -ac 1 -c:a pcm_s16le {output_path}")
else:
    output_path = INPUT_PATH


def callback(ctx, state, i, p):
    print(i)

model = Whisper(MODEL_PATH)
model.params.progress_callback = whisper_progress_callback(callback)

print(model.transcribe(output_path))
