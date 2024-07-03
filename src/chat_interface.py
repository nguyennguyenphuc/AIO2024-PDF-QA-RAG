import chainlit as cl
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from chainlit.types import AskFileResponse
from langchain_community . chat_message_histories import ChatMessageHistory
from vector_database import process_file
from language_model import get_language_model
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def get_vector_db(file: AskFileResponse):
    docs = process_file(file)
    cl.user_session.set("docs", docs)
    embedding = HuggingFaceEmbeddings()
    vector_db = Chroma.from_documents(documents=docs, embedding=embedding)
    return vector_db


@cl.on_chat_start
async def on_chat_start():
    welcome_message = """ Welcome to the PDF QA! To get started :
                        1. Upload a PDF or text file
                        2. Ask a question about the file
                    """
    files = None
    while files is None:
        files = await cl.AskFileMessage(
            content=welcome_message,
            accept=["application/pdf"],
            max_size_mb=20,
            timeout=180,
        ).send()

    file = files[0]

    msg = cl.Message(content="Processing file...", disable_feedback=True)
    await msg.send()

    vector_db = await cl.make_async(get_vector_db)(file)

    message_history = ChatMessageHistory()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=message_history,
        return_messages=True,
    )

    retriever = vector_db.as_retriever(
        search_type="mmr", search_kwargs={'k': 3})

    chain = ConversationalRetrievalChain.from_llm(
        llm=get_language_model(),
        chain_type="stuff",
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

    msg.content = f"'{file.name}' processed . You can now ask questions !"
    await msg.update()
    cl.user_session.set("chain", chain)


@cl.on_message
async def on_message(message: cl.Message):
    chain = cl.user_session.get("chain")
    cb = cl.AsyncLangchainCallbackHandler()
    result = await chain.ainvoke(message.content)
    answer = result["answer"]
    source_documents = result["source_documents"]
    text_elements = []
    if source_documents:
        for source_idx, source_doc in enumerate(source_documents, callbacks=[cb]):
            source_name = f"source_{source_idx}"
            text_elements.append(
                cl.Text(content=source_doc.page_content, name=source_name))

    source_names = [text_el.name for text_el in text_elements]

    if source_names:
        answer += f"\nSources: {', '.join(source_names)}"
    else:
        answer += "\nNo sources found"

    await cl.Message(content=answer, elements=text_elements).send()
