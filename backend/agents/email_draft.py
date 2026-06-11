import json

from backend.schema.agent_schema import CompanyProfile, Contact, EmailDraft

from backend.services.groq_service import call_llm

from backend.utils.prompt_hub.email_draft_prompt import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

from backend.utils.logger import get_logger

logger = get_logger("email_draft")


def generate_email(
    cv_text: str,
    company_profile: CompanyProfile,
    contact: Contact,
    job_title: str,
    jd_excerpt: str,
    tone: str = "formal") -> EmailDraft:

    """
    Generate a cold outreach email.
    """

    logger.info(f"Generating email for {company_profile.domain}")

    user_prompt = USER_PROMPT_TEMPLATE.format(
        cv_text=cv_text,
        company_name=company_profile.domain,
        company_one_liner=company_profile.one_liner,
        job_title=job_title,
        jd_excerpt=jd_excerpt,
        contact_name=contact.name,
        tone=tone
    )

    response = call_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt
    )

    try:

        email_data = json.loads(
            response
        )

        return EmailDraft(
            subject=email_data.get(
                "subject",
                ""
            ),
            body=email_data.get(
                "body",
                ""
            ),
            tone=tone
        )

    except Exception as e:

        logger.error(
            f"Failed to parse email: {e}"
        )

        return EmailDraft(
            subject="",
            body="",
            tone=tone
        )