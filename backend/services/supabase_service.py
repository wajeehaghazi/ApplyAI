from uuid import uuid4
from supabase import Client, create_client
from config.settings import settings
from utils.logger import get_logger

logger = get_logger("supabase_service")


# Singleton Supabase Client
supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_KEY
)

def get_user(user_id: str):
    """
    Fetch a user by ID.
    """

    logger.info(f"Fetching user: {user_id}")

    response = (
        supabase
        .table("users")
        .select("*")
        .eq("id", user_id)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


def upsert_user(
    user_id: str,
    email: str,
    cv_text: str,
    cv_embedding: list[float]
):
    """
    Insert or update user.
    """

    logger.info(f"Upserting user: {user_id}")

    data = {
        "id": user_id,
        "email": email,
        "cv_text": cv_text,
        "cv_embedding": cv_embedding
    }

    return (
        supabase
        .table("users")
        .upsert(data)
        .execute()
    )


def update_user_preference(
    user_id: str,
    preference: str
):
    """
    Update user's job preference.
    """

    logger.info(
        f"Updating preference for user: {user_id}"
    )

    return (
        supabase
        .table("users")
        .update(
            {
                "job_preference": preference
            }
        )
        .eq("id", user_id)
        .execute()
    )

def create_pipeline_run(
    user_id: str) -> str:

    """
    Create pipeline run record.
    """

    run_id = str(uuid4())

    logger.info(
        f"Creating pipeline run: {run_id}"
    )

    data = {
        "id": run_id,
        "user_id": user_id,
        "status": "queued"
    }

    (
        supabase
        .table("pipeline_runs")
        .insert(data)
        .execute()
    )

    return run_id


def update_pipeline_run(
    run_id: str,
    status: str,
    **kwargs
):
    """
    Update pipeline run.
    """

    logger.info(
        f"Updating pipeline run: {run_id}"
    )

    data = {
        "status": status,
        **kwargs
    }

    return (
        supabase
        .table("pipeline_runs")
        .update(data)
        .eq("id", run_id)
        .execute()
    )

def get_job_matches(
    run_id: str):

    """
    Get all jobs for a run.
    """

    logger.info(f"Fetching jobs for run: {run_id}")

    response = (
        supabase
        .table("job_matches")
        .select("*")
        .eq("run_id", run_id)
        .execute()
    )

    return response.data


def get_job_detail(
    job_match_id: str
):
    """
    Get job detail.
    """

    logger.info(
        f"Fetching job: {job_match_id}"
    )

    response = (
        supabase
        .table("job_matches")
        .select("*")
        .eq("id", job_match_id)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None


def update_job_status(
    job_match_id: str,
    status: str
):
    """
    Update job status.
    """

    logger.info(
        f"Updating job status: {job_match_id}"
    )

    return (
        supabase
        .table("job_matches")
        .update(
            {
                "user_status": status
            }
        )
        .eq("id", job_match_id)
        .execute()
    )

def get_applications(
    user_id: str):

    """
    Get applied jobs.
    """

    logger.info(f"Fetching applications for: {user_id}")

    response = (
        supabase
        .table("job_matches")
        .select("*")
        .eq("user_id", user_id)
        .eq("user_status", "applied")
        .execute()
    )

    return response.data