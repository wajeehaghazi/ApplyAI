import json

from backend.schema.agent_schema import CompanyProfile

from backend.services.tavily_service import search_company

from backend.services.groq_service import call_llm

from backend.utils.logger import get_logger

logger = get_logger("company_research")

def research_company(
    company_name: str) -> CompanyProfile:

    """
    Research a company using Tavily + LLM
    and return a structured CompanyProfile.
    """

    logger.info(f"Researching company: {company_name}")

    search_data = search_company( company_name)

    system_prompt = """
    You are a company research assistant.

    Extract company information and return ONLY valid JSON.

    Return fields:
    {
        "domain": "",
        "one_liner": "",
        "size_estimate": "",
        "industry": "",
        "tech_stack": [],
        "culture_note": "",
        "recent_news": []
    }

    Do not return markdown.
    Do not return explanations.
    Return JSON only.
    """

    user_prompt = f"""
    Company Name:
    {company_name}

    Search Results:
    {search_data}
    """

    response = call_llm(
        system_prompt=system_prompt,
        user_prompt=user_prompt
    )

    logger.info("=" * 50)
    logger.info("LLM RESPONSE:")
    logger.info(response)
    logger.info("=" * 50)

    try:
        clean_response = (
            response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        profile_data = json.loads(clean_response)

        return CompanyProfile(**profile_data)

    except Exception as e:
        logger.error(f"Failed to parse company profile: {e}")

        return CompanyProfile(
            domain="",
            one_liner="",
            size_estimate="Unknown",
            industry="Unknown",
            tech_stack=[],
            culture_note="",
            recent_news=[]
        )