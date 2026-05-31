from backend.schema.agent_schema import CompanyProfile, Contact

from backend.services.hunter_service import find_contact

from backend.utils.logger import get_logger

logger = get_logger("email_hunter")

def find_company_contact(
    company_profile: CompanyProfile) -> Contact:

    """
    Find the best contact for a company.
    """

    logger.info(f"Finding contact for {company_profile.domain}")

    contact = find_contact(company_profile.domain)

    return contact