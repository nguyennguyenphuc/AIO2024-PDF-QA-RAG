from rag_pipeline import initialize_rag_system
from chat_interface import run_chat_interface

if __name__ == "__main__":
    rag_system = initialize_rag_system()
    run_chat_interface(rag_system)
