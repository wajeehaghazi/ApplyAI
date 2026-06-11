from backend.services.apify_service import fetch_linkedin_jobs

from backend.services.jsearch_service import fetch_jsearch_jobs

from backend.utils.dedup import deduplicate_by_url

from backend.utils.domain_utils import normalize_domain

from backend.utils.logger import  get_logger

logger = get_logger( "job_discovery")


def discover_jobs(
    preference: str) -> list[dict]:

    """
    Discover jobs from multiple sources,
    normalize them,
    remove duplicates,
    and return the final list.
    """

    logger.info(f"Discovering jobs for: {preference}")

    linkedin_jobs = fetch_linkedin_jobs(preference)

    jsearch_jobs = fetch_jsearch_jobs(preference)

    all_jobs = (
        linkedin_jobs
        + jsearch_jobs
    )

    logger.info(f"Collected {len(all_jobs)} jobs before deduplication")

    unique_jobs = deduplicate_by_url(all_jobs)

    logger.info(f"{len(unique_jobs)} jobs after deduplication")

    for job in unique_jobs:

        job["domain"] = normalize_domain(
            company_name=job.get(
                "company_name",
                ""
            ),
            job_url=job.get(
                "job_url",
                ""
            )
        )

    logger.info(f"Returning {len(unique_jobs)} normalized jobs")

    return unique_jobs