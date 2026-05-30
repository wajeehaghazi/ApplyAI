import asyncio
import json
from backend.services.redis_service import (
    get_pipeline_status,
    get_pipeline_node,
    get_pipeline_counts
)

from backend.utils.logger import get_logger
logger = get_logger("sse_manager")


async def pipeline_event_stream(run_id: str):
    """
    Stream pipeline updates to frontend using SSE.
    """

    previous_node = None

    while True:

        status = get_pipeline_status(run_id)

        node = get_pipeline_node(run_id)

        counts = get_pipeline_counts(run_id)

        if node != previous_node:

            payload = {
                "run_id": run_id,
                "status": status,
                "node": node,
                "counts": counts
            }

            yield (
                f"event: node_complete\n"
                f"data: {json.dumps(payload)}\n\n"
            )

            previous_node = node

        if status == "done":

            yield (
                "event: done\n"
                "data: Pipeline completed\n\n"
            )

            break

        if status == "failed":

            yield (
                "event: error\n"
                "data: Pipeline failed\n\n"
            )

            break

        await asyncio.sleep(1.5)