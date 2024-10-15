from os.path import splitext
import uuid
from llama_index.core import Document
import streamlit as st
from converter import transcribe, pdf2text
from sl import summarise, derive_questions
import dummy


UPLOADS_DIR = "./storage/uploads"

st.set_page_config(page_title="Petranesian Pintar", page_icon="🎓")
st.title("Petranesian Pintar")
st.info("Review materi pembelajaran dengan kuis!", icon="🎓")


def generate_filename(ext):
    key = uuid.uuid4()
    filename = str(key) + ext
    return filename


def save_file(file):
    """Save file with a random name and return the path"""
    filename = file.name
    _, ext = splitext(filename)
    filename = generate_filename(ext)
    full_path = UPLOADS_DIR + "/" + filename
    with open(full_path, "wb") as f:
        f.write(file.getvalue())
    return full_path


transcript = None
material = None
c1, c2 = st.columns(2)
audio_file = c1.file_uploader("Audio")
pdf_file = c2.file_uploader("PDF")

if audio_file is not None and "transcript" not in st.session_state:
    audio_path = save_file(audio_file)
    transcript = transcribe(audio_path)
    st.session_state.transcript = transcript

if pdf_file is not None and "material" not in st.session_state:
    pdf_path = save_file(pdf_file)
    material = pdf2text(pdf_path)
    st.session_state.material = material

if "messages" not in st.session_state:
    st.session_state.messages = []


def chat(role, content):
    st.session_state.messages.append(dict(
        role=role,
        content=content
    ))
    st.chat_message(role).write(content)


if (
    "transcript" in st.session_state
    and "material" in st.session_state
    and "summary" not in st.session_state
    and "questions" not in st.session_state
):
    documents = [
        Document(
            text=st.session_state.transcript,
            extra_info={"type": "raw transcription"}
        ),
        Document(
            text=st.session_state.material,
            extra_info={"type": "raw material"}
        )
    ]
    print("Summarizing")
    if dummy.USE_DUMMY:
        summary = dummy.DUMMY_SUMMARY
    else:
        summary = "\n\n".join([summarise(document) for document in documents])
    print("Done")
    st.session_state.summary = summary

    if dummy.USE_DUMMY:
        questions = dummy.DUMMY_QUESTIONS
    else:
        questions = derive_questions(st.session_state.summary)
    st.session_state.questions = questions
    st.session_state.question_index = 0
    st.session_state.next_question = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if "questions" in st.session_state:
    answer = st.chat_input("Your answer")
    if answer is not None:
        chat("user", answer)
        st.session_state.question_index += 1
        st.session_state.next_question = True

    if st.session_state.next_question:
        text = None
        if st.session_state.question_index >= len(st.session_state.questions):
            text = (
                "Nice work! Take a look at this summary and check your answers\n\n"
                + st.session_state.summary
            )
        else:
            question = st.session_state.questions[st.session_state.question_index]
            text = question
        chat("assistant", text)
        st.session_state.next_question = False