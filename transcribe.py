import whisper
from whisper.utils import get_writer
from custom_whisper import transcribe
from typing import Callable

model: whisper.Whisper | None = None

def get_transcribe(audio: str, language: str = 'en', progress_callback: Callable[[int, int], None] = lambda a,b: None):
    global model

    # Lazy loading to improve startup performance.
    if not model:
        model = whisper.load_model('turbo')

    # return transcribe(model, audio=audio, language=language, verbose=True)
    return transcribe(model, audio=audio, language=language, progress_callback=progress_callback)


def save_file(results, format='tsv'):
    writer = get_writer(format, './output/')
    writer(results, f'transcribe.{format}')


if __name__ == "__main__":
    def pg(total, current):
        print(f"Processed {current} out of {total} sections")

    result = get_transcribe(audio='./samples/Lecture04/DS-Lct04-Communication.mp3', language='id', progress_callback=pg)
    print('-'*50)
    print(result.get('text', ''))
    save_file(result)
    save_file(result, 'txt')
    save_file(result, 'srt')