from services.supabase_service import (
    get_job_matches,
    get_job_detail,
    update_job_status
)

from utils.logger import get_logger
logger = get_logger("jobs_module")


def get_run_results(run_id: str):

    """
    Get all jobs for a pipeline run.
    """

    logger.info(f"Fetching jobs for run: {run_id}")

    return get_job_matches(run_id)


def get_single_job(job_match_id: str):

    """
    Get detailed job information.
    """

    logger.info(f"Fetching job: {job_match_id}")

    return get_job_detail(job_match_id)


def update_status(
    job_match_id: str,
    status: str):

    """
    Update job status.
    """

    logger.info(f"Updating job {job_match_id} to {status}")

    return update_job_status(
        job_match_id,
        status
    )