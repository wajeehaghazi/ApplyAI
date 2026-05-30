from celery import Celery
import time

from backend.config.settings import settings
from backend.utils.logger import get_logger
from backend.services.redis_service import (
    set_pipeline_status
)

logger = get_logger("celery_service")

celery_app = Celery(
    "applyai",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)


@celery_app.task
def run_pipeline_task(
    user_id: str,
    run_id: str
):
    """
    Temporary pipeline task.
    """

    logger.info(
        f"Pipeline started: {run_id}"
    )

    set_pipeline_status(
        run_id,
        "running"
    )

    time.sleep(5)

    set_pipeline_status(
        run_id,
        "done"
    )

    logger.info(
        f"Pipeline completed: {run_id}"
    )