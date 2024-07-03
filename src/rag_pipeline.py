import torch
from transformers import BitsAndBytesConfig, AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain_huggingface.llms import HuggingFacePipeline

from config import Config
from vector_database import create_vector_db
from language_model import get_language_model


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def initialize_rag_system(file_path='./test/YOLOv10_Tutorials.pdf'):

    llm = get_language_model()

    # Create vector database
    vector_db = create_vector_db(file_path)

    retriever = vector_db.as_retriever()
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | hub.pull("rlm/rag-prompt")
        | llm | StrOutputParser())

    return rag_chain
