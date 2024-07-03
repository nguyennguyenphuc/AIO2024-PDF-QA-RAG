from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
from langchain_huggingface.llms import HuggingFacePipeline
import torch

from config import Config


def get_language_model():
    nf4_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    model = AutoModelForCausalLM.from_pretrained(
        Config.MODEL_NAME,
        quantization_config=nf4_config,
        low_cpu_mem_usage=True
    )
    tokenizer = AutoTokenizer.from_pretrained(Config.MODEL_NAME)
    model_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=Config.MAX_NEW_TOKENS,
        pad_token_id=tokenizer.eos_token_id,
        device_map="auto"
    )
    llm = HuggingFacePipeline(pipeline=model_pipeline)
    return llm
