import os
import re

from users import User

# Special documents end in _text.md or is "summary.md"

def clear_all_special_files(topic_path: str):
    for file in os.listdir(topic_path):
        if file.endswith("_text.md") or file == "summary.md":
            os.remove(os.path.join(topic_path, file))
            
def clear_summary_file(topic_path: str):
    summary_file = os.path.join(topic_path, "summary.md")
    if os.path.exists(summary_file):
        os.remove(summary_file)
            
def get_audio_files(topic_path: str) -> list[str]:
    audio_files = [f for f in os.listdir(topic_path) if f.endswith(".mp3") or f.endswith(".m4a") or f.endswith(".wav")]
    return audio_files

def get_documents(topic_path: str) -> list[str]:
    documents = [f for f in os.listdir(topic_path) if f.endswith(".pdf")]
    return documents

def get_unprocessed_documents(topic_path: str) -> list[str]:
    # Unprocessed documents are those without _text.md
    documents = get_documents(topic_path)
    original_documents = [f for f in documents if not f.endswith("_text.md")]
    
    # for each document, check if it has a _text.md file
    unprocessed_documents = []
    for document in original_documents:
        text_file = document + "_text.md"
        if not os.path.exists(os.path.join(topic_path, text_file)):
            unprocessed_documents.append(document)
            
    return unprocessed_documents
    
def get_unprocessed_audio_files(topic_path: str) -> list[str]:
    audio_files = get_audio_files(topic_path)
    original_audio_files = [f for f in audio_files if not f.endswith("_text.md")]
    
    # make sure the audio file does not have a .wav equivalent of the same name
    for audio_file in original_audio_files:
        base_name, ext = os.path.splitext(audio_file)
        wav_file = base_name + ".wav"
        if os.path.exists(os.path.join(topic_path, wav_file)):
            original_audio_files.remove(audio_file)
    
    # for each audio file, check if it has a .wav file and a _text.md file under it
    unprocessed_audio_files = []
    for audio_file in original_audio_files:
        # split extension
        base_name, ext = os.path.splitext(audio_file)
        wav_file = base_name + ".wav"
        
        text_file = base_name + "_text.md"
        
        if not os.path.exists(os.path.join(topic_path, wav_file)):
            unprocessed_audio_files.append(audio_file)
        elif not os.path.exists(os.path.join(topic_path, text_file)):
            unprocessed_audio_files.append(audio_file)
        
            
    return unprocessed_audio_files

def get_file_content(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

def get_processed_files_content(topic_path: str) -> tuple[list[str], list[str]]:
    # Processed files are those with _text.md
    documents = get_documents(topic_path)
    documents_text_files = [f + ".md" for f in documents]
    print("documents_text_files: ", documents_text_files)
    # filter exists
    documents_text_files = [f for f in documents_text_files if os.path.exists(os.path.join(topic_path, f))]
    processed_documents_contents = [get_file_content(os.path.join(topic_path, f)) for f in documents_text_files]
    
    audio_files = get_audio_files(topic_path)
    print("audio_files: ", audio_files)
    processed_audio_files = [os.path.splitext(f)[0] + "_text.md" for f in audio_files]
    print("processed_audio_files: ", processed_audio_files)
    # filter exists
    processed_audio_files = [f for f in processed_audio_files if os.path.exists(os.path.join(topic_path, f))]
    processed_audio_file_contents = [get_file_content(os.path.join(topic_path, f)) for f in processed_audio_files]
    
    return processed_documents_contents, processed_audio_file_contents

def get_sections(user: User) -> list[str]:
    base_path = user.get_base_path()
    
    # Get all directories in base_path/topics, if does not exist, create it
    if not os.path.exists(os.path.join(base_path, "topics")):
        os.mkdir(os.path.join(base_path, "topics"))
    sections = [d.name for d in os.scandir(os.path.join(base_path, "topics")) if d.is_dir()]
    return sections