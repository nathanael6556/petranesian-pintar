import streamlit as st
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.readers.file import CSVReader
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import Settings
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.node_parser import SentenceSplitter
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.chat_engine import CondensePlusContextChatEngine
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.core import Document
import sys
import logging
import nest_asyncio
from dotenv import load_dotenv
from ollama import Client
import re

# Prepare Environment
load_dotenv()
nest_asyncio.apply()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Base Settings
model = "llama3.1:8b-instruct-q4_0"
embed_model = "mxbai-embed-large:latest"
ollama_endpoint = "http://127.0.0.1:11434"


c = Client(ollama_endpoint, timeout=600)

Settings.llm = Ollama(model=model, base_url=ollama_endpoint)
Settings.embed_model = OllamaEmbedding(base_url=ollama_endpoint, model_name=embed_model)

# Summariser
summariser_splitter = SentenceSplitter(chunk_size=15 * 1024, chunk_overlap=512)


def summarise(d: Document) -> str:
    summaries = []
    for chunk in summariser_splitter.split_text(d.text):
        result = c.generate(
            model=model,
            prompt=(
                f"""Clean up the given document and restructure it using Markdown.
Clean up the document by structuring the information into points.
Fix and correct grammatical and language errors.
You must include all crucial information. You must not add any information that is not in the document.

<Document>
{chunk}

<Restructured Document>
    """
            ),
            options={
                "temperature": 0,
                "num_ctx": 16 * 1024,
                "num_predict": 2 * 1024,
            },
        )

        response = result["response"].strip()
        logging.info(f"""
[Summary]
{response}
""")
        summaries.append(response)
    return "\n\n".join(summaries)



# Create questions from summary
def derive_questions(summary: str) -> list[str]:
    questions = []
    question_re = re.compile(r"\d{1,2}\.\s(.*)")

    # Trim the first 2 lines
    chunk = summary

    result = c.generate(
        model=model,
        prompt=(
            f"""Create 5 questions that covers this summary.
The questions should ask reasoning and not ask for facts.
You must answer in the following format:
<Questions>
1. Question 1
2. Question 2

<Summary>
{chunk}

<Questions>
    """
        ),
        options={
            "temperature": 1,
            "num_predict": 1 * 1024,
        },
    )

    response = result["response"]
    logging.info(response)
    questions = question_re.findall(response)
    questions = [q.strip() for q in questions]

    return questions


# Create questions from materials
def derive_questions_from_materials(documents: list[Document]) -> tuple:
    # Get the summaries
    summaries = map(summarise, documents)

    # Create questions
    questions = derive_questions("\n".join(summaries))

    return (summaries, questions)
