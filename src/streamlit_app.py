import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from config import Config
from vector_database import create_vector_db
from language_model import get_language_model

# Khởi tạo vector database và mô hình ngôn ngữ
vector_db = create_vector_db('./AIO-2024-All-Materials.pdf')
retriever = vector_db.as_retriever(search_type="mmr", search_kwargs={'k': 3})

message_history = ChatMessageHistory()
memory = ConversationBufferMemory(
    memory_key="chat_history",
    output_key="answer",
    chat_memory=message_history,
    return_messages=True,
)

chain = ConversationalRetrievalChain.from_llm(
    llm=get_language_model(),
    chain_type="stuff",
    retriever=retriever,
    memory=memory,
    return_source_documents=True
)

st.title("RAG PDF Question-Answering")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    file_details = {"FileName": uploaded_file.name,
                    "FileType": uploaded_file.type}
    st.write(file_details)

    if st.button("Process"):
        docs = create_vector_db(uploaded_file)
        st.success("File processed successfully!")

        question = st.text_input("Ask a question about the document:")
        if st.button("Get Answer"):
            result = chain({"question": question})
            answer = result["answer"]
            source_documents = result["source_documents"]

            st.write("Answer:", answer)
            st.write("Source documents:")
            for i, doc in enumerate(source_documents):
                st.write(f"Source {i+1}:", doc.page_content)
