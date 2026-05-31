from pydantic import BaseModel


class CompanyProfile(BaseModel):

    domain: str

    one_liner: str

    size_estimate: str

    industry: str

    tech_stack: list[str]

    culture_note: str

    recent_news: list[str]


class Contact(BaseModel):

    domain: str

    email: str

    name: str

    title: str

    confidence_score: int

    source: str

    smtp_ok: bool


class EmailDraft(BaseModel):

    subject: str

    body: str

    tone: str