from openai import OpenAI

from config.settings import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_embedding(
    text: str
) -> list[float]:
    """
    Generate embedding for text.
    """

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding