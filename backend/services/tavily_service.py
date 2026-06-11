from tavily import TavilyClient

from backend.config.settings import settings
from backend.utils.logger import get_logger


logger = get_logger("tavily_service")

tavily_client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)

def search_company(
    company_name: str) -> dict:

    """
    Search company information using Tavily.

    Returns:
        dict: Raw Tavily response.
    """

    logger.info(f"Searching company: {company_name}")

    query = (
        f"{company_name} "
        "company info culture tech stack hiring"
    )

    try:

        response = tavily_client.search(
            query=query,
            max_results=5
        )

        logger.info(f"Found {len(response.get('results', []))} results")

        return response

    except Exception as e:

        logger.error(f"Tavily search failed: {e}")

        return {
            "results": []
        }