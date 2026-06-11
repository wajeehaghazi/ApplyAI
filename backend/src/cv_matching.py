from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from backend.config.settings import settings
from backend.utils.logger import get_logger

logger = get_logger("cv_matching")

client = OpenAI( api_key=settings.OPENAI_API_KEY)


def get_embedding(
    text: str) -> list[float]:

    """
    Generate embedding for text.
    """

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


def calculate_similarity(
    cv_embedding: list[float],
    job_embedding: list[float]) -> float:

    """
    Calculate cosine similarity.
    """

    similarity = cosine_similarity(
        [cv_embedding],
        [job_embedding]
    )[0][0]

    return float(
        round(
            similarity * 100,
            1
        )
    )


def match_jobs_to_cv(
    cv_text: str,
    jobs: list[dict],
    threshold: float = 70.0) -> list[dict]:

    """
    Match jobs against CV using embeddings.
    """

    logger.info(f"Matching {len(jobs)} jobs")

    cv_embedding = get_embedding(cv_text)

    matched_jobs = []

    for job in jobs:

        try:

            description = job.get(
                "description",
                ""
            )

            if not description:
                continue

            job_embedding = get_embedding(
                description
            )

            score = calculate_similarity(
                cv_embedding,
                job_embedding
            )

            if score >= threshold:

                matched_job = {
                    **job,
                    "match_score": score,
                    "job_match_id": None
                }

                matched_jobs.append(matched_job)

        except Exception as e:

            logger.warning( f"Failed matching job: {e}")

    matched_jobs.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    logger.info(f"Found {len(matched_jobs)} matching jobs")

    return matched_jobs