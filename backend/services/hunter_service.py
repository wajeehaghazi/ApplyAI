from backend.schema.agent_schema import Contact
from backend.utils.logger import get_logger


logger = get_logger("hunter_service")


def find_contact(
    domain: str) -> Contact:

    """
    Mock Hunter service.

    Returns a fake contact for learning
    and development purposes.
    """

    logger.info(f"Finding contact for {domain}")

    return Contact(
        domain=domain,
        email=f"careers@{domain}",
        name="Hiring Team",
        title="Recruiter",
        confidence_score=95,
        source="mock",
        smtp_ok=True
    )