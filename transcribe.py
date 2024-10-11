import whisper
from whisper.utils import get_writer
model = whisper.load_model('large')


def get_transcribe(audio: str, language: str = 'en'):
    return model.transcribe(audio=audio, language=language, verbose=True)


def save_file(results, format='tsv'):
    writer = get_writer(format, './output/')
    writer(results, f'transcribe.{format}')


if __name__ == "__main__":
    result = get_transcribe(audio='./samples/DS Lect04 Communication.mp3', language='id')
    print('-'*50)
    print(result.get('text', ''))
    save_file(result)
    save_file(result, 'txt')
    save_file(result, 'srt')