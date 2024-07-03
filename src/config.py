import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MODEL_NAME = os.getenv('MODEL_NAME', 'lmsys/vicuna-7b-v1.5')
    MAX_NEW_TOKENS = int(os.getenv('MAX_NEW_TOKENS', 512))
    CHUNK_SIZE = int(os.getenv('CHUNK_SIZE', 1000))
    CHUNK_OVERLAP = int(os.getenv('CHUNK_OVERLAP', 100))
