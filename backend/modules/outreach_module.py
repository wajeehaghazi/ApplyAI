from backend.agents.company_research import (
    research_company
)

from backend.agents.email_hunter import (
    find_company_contact
)

from backend.agents.email_draft import (
    generate_email
)

from backend.utils.logger import (
    get_logger
)


logger = get_logger(
    "outreach_module"
)


def run_outreach_pipeline(
    company_name: str,
    cv_text: str,
    job_title: str,
    jd_excerpt: str
) -> dict:
    """
    Run the complete outreach workflow.
    """

    logger.info(
        f"Starting outreach for {company_name}"
    )

    company_profile = research_company(
        company_name
    )

    contact = find_company_contact(
        company_profile
    )

    email_draft = generate_email(
        cv_text=cv_text,
        company_profile=company_profile,
        contact=contact,
        job_title=job_title,
        jd_excerpt=jd_excerpt
    )

    return {
        "company_profile": company_profile,
        "contact": contact,
        "email_draft": email_draft
    }