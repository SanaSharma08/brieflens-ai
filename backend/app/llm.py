import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
# This module provides functions to create and return the LLM used by BriefLens. It uses the `langchain` library to create a ChatOpenAI instance, which is a wrapper around the OpenAI API for generating text completions.

load_dotenv()


def get_llm():
    """
    Create and return the LLM used by BriefLens.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set in the .env file."
        )

    llm = ChatOpenAI(
        model="gpt-5-mini",
        temperature=0,
    )

    return llm