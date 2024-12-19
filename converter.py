import os
from os.path import splitext
from pypdf import PdfReader
import whisper
import dummy
import pymupdf4llm
import custom_whisper
from typing import Callable

model: whisper.Whisper | None = None

def transcribe(path, language='id', verbose=False, progress_callback: Callable[[int, int], None] = lambda a,b: None):
    # Convert audio to WAV
    if not path.endswith(".wav"):
        input_path, _ = splitext(path)
        input_path += ".wav"
        status = os.system(f"ffmpeg -i '{path}' -ar 16000 -ac 1 -c:a pcm_s16le '{input_path}'")
        assert status == 0, "Fail to convert audio to WAV"
    else:
        input_path = path

    global model

    # Lazy loading to improve startup performance.
    if not model:
        model = whisper.load_model('turbo')

    print("Transcribing...")
    transcript = custom_whisper.transcribe(model, audio=input_path, language=language, verbose=verbose, progress_callback=progress_callback)
    return transcript["text"]


def pdf2text(path, splitter="\n\n"):
    return pymupdf4llm.to_markdown(path)