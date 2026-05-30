from pydantic import BaseModel
from typing import Optional


class JobCard(BaseModel):
    id: str
    job_title: str
    company_name: str
    match_score: float
    email_confidence: Optional[int] = None
    user_status: str


class JobDetail(BaseModel):
    id: str
    job_title: str
    company_name: str
    description: str

    company_profile: dict
    contact: dict
    email_draft: dict


class StatusUpdate(BaseModel):
    user_status: str