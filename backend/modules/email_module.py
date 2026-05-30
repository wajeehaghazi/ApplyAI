from schema.email_schema import (EmailDraftResponse)
from utils.logger import get_logger

logger = get_logger("email_module")


def regenerate_draft(
    job_match_id: str,
    user_id: str):

    logger.info(
        f"Regenerating email draft for {job_match_id}"
    )

    return EmailDraftResponse(
        subject="Placeholder Subject",
        body="Placeholder email body."
    )