from whispercpp import Whisper


w = Whisper.from_pretrained("/home/jupyter-c14220202@john.pet-104c4/petranesian-pintar/src/samples/ggml-large-v3.bin")

result = w.transcribe_from_file("./DS Lect04 Communication.mp3")
with open("transcript.txt", "w") as f:
    f.write(result)
