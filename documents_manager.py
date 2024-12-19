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
    
    # for each audio file, check if it has a _text.md file
    unprocessed_audio_files = []
    for audio_file in original_audio_files:
        text_file = audio_file + "_text.md"
        if not os.path.exists(os.path.join(topic_path, text_file)):
            unprocessed_audio_files.append(audio_file)
            
    return unprocessed_audio_files

def get_file_content(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()

def get_processed_files_content(topic_path: str) -> tuple[list[str], list[str]]:
    # Processed files are those with _text.md
    documents = get_documents(topic_path)
    processed_documents = [f for f in documents if f.endswith("_text.md")]
    processed_documents_contents = [get_file_content(os.path.join(topic_path, f)) for f in processed_documents]
    
    audio_files = get_audio_files(topic_path)
    processed_audio_files = [f for f in audio_files if f.endswith("_text.md")]
    processed_audio_file_contents = [get_file_content(os.path.join(topic_path, f)) for f in processed_audio_files]
    
    return processed_documents_contents, processed_audio_file_contents

def get_sections(user: User) -> list[str]:
    base_path = user.get_base_path()
    
    # Get all directories in base_path/topics, if does not exist, create it
    if not os.path.exists(os.path.join(base_path, "topics")):
        os.mkdir(os.path.join(base_path, "topics"))
    sections = [d.name for d in os.scandir(os.path.join(base_path, "topics")) if d.is_dir()]
    return sections