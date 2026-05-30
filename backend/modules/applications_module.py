from services.supabase_service import (get_applications)
from utils.logger import get_logger


logger = get_logger("applications_module")

def get_user_applications(
    user_id: str):

    """
    Get applications for a user.
    """

    logger.info(f"Fetching applications for {user_id}")

    return get_applications(
        user_id
    )