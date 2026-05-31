from groq import Groq
from openai import OpenAI

from backend.config.settings import settings
from backend.utils.logger import get_logger


logger = get_logger("groq_service")

groq_client = Groq(
    api_key=settings.GROQ_API_KEY
    )

openai_client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def call_llm(
system_prompt: str,
    user_prompt: str) -> str:

    """
    Call Groq first.
    If Groq fails, fall back to OpenAI.
    Returns generated text.
    """

    logger.info("Calling LLM")

    try:

        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        result = response.choices[0].message.content

        logger.info("Groq response received successfully")

        return result

    except Exception as e:

        logger.error(f"Groq failed: {e}")

        logger.info("Falling back to OpenAI")

        try:

            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )

            result = response.choices[0].message.content

            logger.info("OpenAI response received successfully")

            return result

        except Exception as e:

            logger.error(
                f"OpenAI failed: {e}"
            )

            raise Exception(
                "Both Groq and OpenAI failed."
            )