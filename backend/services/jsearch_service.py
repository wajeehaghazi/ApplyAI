import requests

from backend.config.settings import settings
from backend.utils.logger import get_logger


logger = get_logger("jsearch_service")

BASE_URL = ("https://jsearch.p.rapidapi.com/search")


def fetch_jsearch_jobs(
    preference: str) -> list[dict]:

    """
    Fetch jobs from JSearch API and normalize
    them into the project's standard format.
    """

    logger.info(f"Fetching JSearch jobs for: {preference}")

    try:

        headers = {
            "X-RapidAPI-Key": (
                settings.RAPIDAPI_KEY
            ),
            "X-RapidAPI-Host": (
                "jsearch.p.rapidapi.com"
            )
        }

        params = {
            "query": preference,
            "page": 1,
            "num_pages": 1,
            "country": "us",
            "date_posted": "month"
        }

        response = requests.get(
            BASE_URL,
            headers=headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data.get(
            "data",
            []
        ):

            jobs.append(
                {
                    "job_title": item.get("job_title",""),

                    "company_name": item.get("employer_name",""),

                    "domain": "",

                    "description": item.get("job_description", ""),

                    "job_url": item.get("job_apply_link",""),

                    "posted_date": item.get("job_posted_at_datetime_utc",""),
                    
                    "source": "jsearch"
                }
            )

        logger.info(f"Fetched {len(jobs)} jobs from JSearch")

        return jobs

    except Exception as e:

        logger.warning(
            f"JSearch failed: {e}"
        )

        return []