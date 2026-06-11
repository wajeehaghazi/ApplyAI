from typing import TypedDict

class PipelineState(TypedDict):

    user_id: str
    run_id: str
    cv_text: str
    cv_embedding: list[float]
    job_preference: str

    raw_jobs: list[dict]
    matched_jobs: list[dict]

    company_profiles: dict[str, dict]
    contacts: dict[str, dict]
    email_drafts: dict[str, dict]

    errors: list[dict]

    current_node: str