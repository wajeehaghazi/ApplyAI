from pydantic import BaseModel

class Job(BaseModel):

    job_title: str
    company_name: str
    domain: str
    description: str
    job_url: str
    posted_date: str
    source: str

class MatchedJob(Job):
    
    match_score: float
    job_match_id: str | None = None