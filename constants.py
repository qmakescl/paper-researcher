import os

from dotenv import load_dotenv
from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModelType
from llama_index.llms.openai import OpenAI


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

embed_model = OpenAIEmbedding(
    model=OpenAIEmbeddingModelType.TEXT_EMBED_3_LARGE,
    api_key = openai_api_key
)

