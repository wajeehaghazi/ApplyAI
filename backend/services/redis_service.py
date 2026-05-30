import json
import redis
from backend.config.settings import settings
from backend.utils.logger import get_logger

logger = get_logger("redis_service")


# Redis client singleton
redis_client = redis.Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)


TTL_SECONDS = 24 * 60 * 60  # 24 hours

def set_pipeline_status(
    run_id: str,
    status: str) -> None:

    """
    Store pipeline status.
    """

    key = f"pipeline:{run_id}:status"

    redis_client.set(
        key,
        status,
        ex=TTL_SECONDS
    )

    logger.info(
        f"Status updated for {run_id}: {status}"
    )


def get_pipeline_status(
    run_id: str) -> str | None:
    
    """
    Retrieve pipeline status.
    """

    key = f"pipeline:{run_id}:status"

    return redis_client.get(key)


def set_pipeline_node(
    run_id: str,
    node: str) -> None:

    """
    Store current pipeline node.
    """

    key = f"pipeline:{run_id}:node"

    redis_client.set(
        key,
        node,
        ex=TTL_SECONDS
    )

    logger.info(
        f"Node updated for {run_id}: {node}"
    )


def get_pipeline_node(
    run_id: str) -> str | None:

    """
    Retrieve current pipeline node.
    """

    key = f"pipeline:{run_id}:node"

    return redis_client.get(key)


def set_pipeline_counts(
    run_id: str,
    counts: dict) -> None:

    """
    Store pipeline statistics.
    Example:
    {
        "total_found": 100,
        "matched": 35
    }
    """

    key = f"pipeline:{run_id}:counts"

    redis_client.set(
        key,
        json.dumps(counts),
        ex=TTL_SECONDS
    )

    logger.info(
        f"Counts updated for {run_id}"
    )


def get_pipeline_counts(
    run_id: str
) -> dict | None:
    """
    Retrieve pipeline statistics.
    """

    key = f"pipeline:{run_id}:counts"

    data = redis_client.get(key)

    if not data:
        return None

    return json.loads(data)