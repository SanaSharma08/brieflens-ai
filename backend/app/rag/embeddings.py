from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv("../.env")


def get_embedding_model():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    return embeddings