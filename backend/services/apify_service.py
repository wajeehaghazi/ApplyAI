from apify_client import ApifyClient

from backend.config.settings import settings
from backend.utils.logger import get_logger


logger = get_logger("apify_service")

client = ApifyClient(settings.APIFY_API_TOKEN)

def fetch_linkedin_jobs(
    preference: str) -> list[dict]:

    """
    Fetch jobs from Apify LinkedIn Jobs Scraper
    and normalize them to the standard format.
    """

    logger.info(f"Fetching LinkedIn jobs for: {preference}")

    try:

        actor_input = {
            "keywords": preference,
            "maxItems": 30
        }

        run = client.actor(
            "hMvNSpz3JnHgl5jkh"
        ).call(
            run_input=actor_input
        )

        jobs = []

        for item in client.dataset(
            run["defaultDatasetId"]
        ).iterate_items():

            jobs.append(
                {
                    "job_title": item.get("title",""),

                    "company_name": item.get("companyName",""),

                    "domain": "","description": item.get("description",""),

                    "job_url": item.get("jobUrl",""),

                    "posted_date": item.get("postedAt",""),

                    "source": "linkedin"
                }
            )

        logger.info(f"Fetched {len(jobs)} jobs from Apify")

        return jobs

    except Exception as e:

        logger.warning( f"Apify failed: {e}")

        return []