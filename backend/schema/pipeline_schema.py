from pydantic import BaseModel

class PipelineRunResponse(BaseModel):
    run_id: str