from urllib.parse import urlparse

from backend.utils.logger import get_logger

logger = get_logger("domain_utils")

def normalize_domain(
    company_name: str,
    job_url: str) -> str:

    try:

        if job_url:

            parsed_url = urlparse(job_url)

            domain = parsed_url.netloc

            if domain.startswith("www."):
                domain = domain[4:]

            parts = domain.split(".")

            if len(parts) >= 2:

                return ".".join(
                    parts[-2:]
                )

        return (
            company_name
            .lower()
            .replace(" ", "")
            + ".com"
        )

    except Exception as e:

        logger.error(f"Error normalizing domain: {e}")

        return (
            company_name
            .lower()
            .replace(" ", "")
            + ".com"
        )