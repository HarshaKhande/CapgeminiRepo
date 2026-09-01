import os

from dotenv import load_dotenv
from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint
)

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN not found. Check your .env file.")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3.8-2.4T-A95B",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_new_tokens=2000,
    temperature=0.2,
)

chat_model = ChatHuggingFace(
    llm=llm
)