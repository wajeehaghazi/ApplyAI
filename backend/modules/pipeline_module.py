import uuid
from backend.schema.pipeline_schema import (PipelineRunResponse)

from backend.services.redis_service import (set_pipeline_status)

from backend.services.celery_service import (run_pipeline_task)

from backend.utils.logger import get_logger


logger = get_logger(
    "pipeline_module"
)

def trigger_pipeline(user_id: str) -> PipelineRunResponse:

    run_id = str(
        uuid.uuid4()
    )

    logger.info(f"Creating pipeline run: {run_id}")

    set_pipeline_status(
        run_id,
        "queued"
    )

    run_pipeline_task.delay(
        user_id,
        run_id
    )

    return PipelineRunResponse( run_id=run_id)