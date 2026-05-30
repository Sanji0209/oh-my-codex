import os
from openai import OpenAI


def get_model_name() -> str:
    return os.getenv("MODEL_NAME", "gpt-4o-2024-05-13")


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)
