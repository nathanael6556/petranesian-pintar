import os
from os.path import splitext
from pypdf import PdfReader
import whisper
import dummy


model = whisper.load_model('turbo')


def transcribe(path, language='id', verbose=True):
    if dummy.USE_DUMMY:
        return dummy.DUMMY_TRANSCRIPT

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

    print("Transcribing...")
    transcript = model.transcribe(audio=input_path, language=language, verbose=verbose)
    return transcript["text"]


def pdf2text(path, splitter="\n\n"):
    if dummy.USE_DUMMY:
        return dummy.DUMMY_MATERIAL

    reader = PdfReader(path)
    texts = [page.extract_text() for page in reader.pages]
    return splitter.join(texts)