import os
from os.path import splitext
from pypdf import PdfReader
from whisper_cpp_python import Whisper
from whisper_cpp_python.whisper_cpp import whisper_progress_callback


MODEL_PATH = "ggml-small.bin"


def transcribe(path):
    # Convert audio to WAV
    if not path.endswith(".wav"):
        input_path, _ = splitext(path)
        input_path += ".wav"
        status = os.system(f"ffmpeg -i '{path}' -ar 16000 -ac 1 -c:a pcm_s16le {input_path}")
        assert status == 0, "Fail to convert audio to WAV"
    else:
        input_path = path

    def callback(ctx, state, i, p):
        print(i, "%", sep="")

    model = Whisper(MODEL_PATH)
    model.params.progress_callback = whisper_progress_callback(callback)

    print("Transcribing...")
    transcript = model.transcribe(input_path, response_format='text', language='id')
    return transcript


def pdf2text(path, splitter="\n\n"):
    reader = PdfReader(path)
    texts = [page.extract_text() for page in reader.pages]
    return splitter.join(texts)