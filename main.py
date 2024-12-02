import streamlit as st
from os.path import splitext
import uuid
from llama_index.core import Document
from converter import transcribe, pdf2text
from sl import summarise, derive_questions
from llama_index.core.node_parser import SentenceSplitter
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.chat_engine import ContextChatEngine
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, Document
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import get_response_synthesizer
from llama_index.core.prompts import ChatMessage
import dummy
import asyncio
import time

# Make sure user is specified
if not "user" in st.session_state:
    st.rerun()

loop = asyncio.get_event_loop()


def get_ms():
    return time.time_ns() // 1_000_000


UPLOADS_DIR = "./storage/uploads"
splitter = SentenceSplitter(chunk_size=512, chunk_overlap=128)

def generate_filename(ext):
    key = uuid.uuid4()
    filename = str(key) + ext
    return filename


def prepare_retriever(documents: list[Document]):
    with st.spinner(text="Preparing data..."):
        nodes = splitter.get_nodes_from_documents(documents, show_progress=True)
        index = VectorStoreIndex.from_documents(
            documents, show_progress=True, text_splitter=splitter
        )
        index_retriever = index.as_retriever(similarity_top_k=2)
        bm25_retriever = BM25Retriever.from_defaults(
            nodes=nodes,
            similarity_top_k=2,
        )

        return QueryFusionRetriever(
            [index_retriever, bm25_retriever],
            num_queries=1,
            similarity_top_k=4,
            use_async=True,
            verbose=True,
        )


def chat(role, content):
    st.session_state.messages.append(dict(role=role, content=content))
    st.chat_message(role).write(content)


def chat_stream(role, generator, content_getter):
    st.chat_message(role).write_stream(generator)
    st.session_state.messages.append(dict(role=role, content=content_getter()))



def save_file(file):
    """Save file with a random name and return the path"""
    filename = file.name
    _, ext = splitext(filename)
    filename = generate_filename(ext)
    full_path = UPLOADS_DIR + "/" + filename
    with open(full_path, "wb") as f:
        f.write(file.getvalue())
    return full_path


def main():
    st.set_page_config(page_title="Petranesian Pintar", page_icon="🎓")
    st.title("Petranesian Pintar")
    st.info("Review materi pembelajaran dengan kuis!", icon="🎓")

    if "chat_mode" not in st.session_state:
        st.session_state.chat_mode = False
    languages = {"English": "en", "Indonesia": "id"}

    if ("language" not in st.session_state):
        selected_language = st.radio(
            "Language",
            options=languages,
            horizontal=True,
        )
        confirm_language = st.button("Confirm language")
        if (confirm_language):
            st.session_state.language = selected_language
            st.rerun()
        return

    transcript = None
    material = None
    c1, c2 = st.columns(2)
    audio_file = c1.file_uploader("Audio")
    pdf_file = c2.file_uploader("PDF")

    if audio_file is not None and "transcript" not in st.session_state:
        with st.spinner("Transcribing audio..."):
            progress_bar = st.progress(0., "Transcoding audio...")
            audio_path = save_file(audio_file)
            total_progress = 0
            start_time = get_ms()

            def update_progress(total, current_rate):
                nonlocal total_progress
                total_progress += current_rate
                percent_complete = total_progress / total
                frames_per_second = total_progress / ((get_ms() - start_time) / 1000)
                estimated_done_seconds = int((total - total_progress) // frames_per_second)
                progress_bar.progress(percent_complete, text=f"Transcribing Audio ({total_progress}/{total} frames, {frames_per_second:.2f} frames/s, around {estimated_done_seconds} seconds left.)")

            transcript = transcribe(audio_path, progress_callback=update_progress)
            st.session_state.transcript = transcript

            progress_bar.empty()

    if pdf_file is not None and "material" not in st.session_state:
        with st.spinner("Extracting text from PDF..."):
            pdf_path = save_file(pdf_file)
            material = pdf2text(pdf_path)
            st.session_state.material = material

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "transcript" in st.session_state:
        with st.expander("Transcript"):
            st.download_button("Download transcript", st.session_state.transcript, "transcript.txt", "text/plain ")
            st.write(st.session_state.transcript)

    if (
        "transcript" in st.session_state
        and "material" in st.session_state
        and "summary" not in st.session_state
        and "questions" not in st.session_state
    ):
        documents = [
            Document(
                text=st.session_state.transcript, extra_info={"type": "raw transcription"}
            ),
            Document(text=st.session_state.material, extra_info={"type": "raw material"}),
        ]

        with st.spinner("Summarizing..."):
            summaries = []
            progress_bar = st.progress(0., f"Summarizing: (Document 1/{len(documents)}, 0/? chunks)...")

            for idx, document in enumerate(documents):

                def progress_callback(total_processed, total_chunks):
                    progress_bar.progress(total_processed / total_chunks, f"Summarizing: (Document {idx+1}/{len(documents)}, {total_processed}/{total_chunks} chunks)...")

                summary = loop.run_until_complete(summarise(document, progress_callback))
                summaries.append(summary)

            summary = "\n\n".join(summaries)
            progress_bar = progress_bar.progress(1., f"Creating a merged summary...")
            summary = loop.run_until_complete(summarise(Document(text=summary, extra_info={"type": "summary of transcription and material"})))
            st.session_state.summary = summary
            st.session_state.documents = documents + [
                Document(text=summary, extra_info={"type": "summary"})
            ]

            progress_bar.empty()

        with st.spinner("Creating questions..."):
            questions = derive_questions(summary)
            st.session_state.questions = questions

        st.session_state.questions = questions
        st.session_state.answers = []
        st.session_state.question_index = 0
        st.session_state.next_question = True

    if "summary" in st.session_state:
        with st.expander("Summary"):
            st.download_button("Download summary", st.session_state.summary, "summary.md", "text/markdown ")
            st.write(st.session_state.summary)

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if st.session_state.chat_mode:
        if "chat_engine" not in st.session_state:
            documents = st.session_state.documents
            index = VectorStoreIndex.from_documents(documents, show_progress=True)
            chat_history = [ChatMessage(**message) for message in st.session_state.messages]
            memory = ChatMemoryBuffer.from_defaults(chat_history=chat_history, token_limit=16384)
            chat_engine = ContextChatEngine.from_defaults(
                retriever=st.session_state.retriever,
                chat_history=chat_history,
                memory=memory,
                context_template=(
                    "You are a teacher guiding a student."
                    "Give the student constructive criticism with the given context."
                    "Here are the relevant documents for the context:\n"
                    "{context_str}"
                    "\nInstruction: Use the previous chat history, or the context above, to interact and help the student."
                )
            )
            st.session_state.chat_engine = chat_engine
        answer = st.chat_input("Ask me anything!")
        if answer is not None:
            chat("user", answer)
            with st.spinner("Thinking..."):
                response_stream = st.session_state.chat_engine.stream_chat(answer)
                chat_stream("assistant", response_stream.response_gen, lambda : response_stream.response)

    if "questions" in st.session_state and st.session_state.question_index < len(
        st.session_state.questions
    ) and not st.session_state.chat_mode:
        answer = st.chat_input("Your answer")
        if answer is not None:
            st.session_state.answers.append(answer)
            chat("user", answer)
            st.session_state.question_index += 1
            st.session_state.next_question = True

        if st.session_state.next_question:
            text = None
            if st.session_state.question_index >= len(st.session_state.questions):
                text = "Nice work! Let's evaluate them."
                chat("assistant", text)

                st.session_state.retriever = prepare_retriever(st.session_state.documents)

                response_synthesizer = get_response_synthesizer(
                    streaming=True,
                    verbose=True,
                )
                qe = RetrieverQueryEngine(
                    retriever=st.session_state.retriever,
                    response_synthesizer=response_synthesizer,
                )

                with st.chat_message("assistant"):
                    content = ""
                    for question, answer in zip(st.session_state.questions, st.session_state.answers):
                        qa = f"You are a teacher evaluating a student's answer. Give the student constructive criticism with the given context.\nQuestion: {question}\nUser's Answer: {answer}\n\nEvaluation of the answer:"
                        st.write(f"Question: {question}")
                        content += f"Question: {question}\n\n"
                        st.write(f"Your Answer: {answer}")
                        content += f"Your Answer: {answer}\n\n"
                        st.write(f"Evaluation:")
                        content += f"Evaluation:\n\n"
                        response_stream = qe.query(qa)
                        full_str = st.write_stream(response_stream.response_gen)
                        content += str(full_str)
                        st.write("\n\n")
                        content += "\n\n"
                st.session_state.messages.append(dict(
                    role="assistant",
                    content=content
                ))

                st.session_state.chat_mode = True
                chat("assistant", "Feel free to ask for further explanation!")
                del answer
                st.rerun()
            else:
                question = st.session_state.questions[st.session_state.question_index]
                chat("assistant", question)
            st.session_state.next_question = False



main()