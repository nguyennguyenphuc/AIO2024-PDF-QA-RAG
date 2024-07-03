from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chainlit.types import AskFileResponse

from config import Config


# hàm create_vector_db để test vector db thôi
def create_vector_db(file_path='./test/YOLOv10_Tutorials.pdf'):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )
    docs = text_splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings()
    vector_db = Chroma.from_documents(documents=docs, embedding=embedding)

    return vector_db


def process_file(file: AskFileResponse):
    if file.type == "text/plain":
        loader_inf = TextLoader
    elif file.type == "application/pdf":
        loader_inf = PyPDFLoader
    else:
        raise ValueError(f"Unsupported file type: {file.type}")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )
    loader = loader_inf(file.path)
    documents = loader.load()
    docs = text_splitter.split_documents(documents)

    for i, doc in enumerate(docs):
        doc.metadata["source"] = f"source_{i}"

    return docs
