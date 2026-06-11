from langgraph.graph import StateGraph,END

from backend.src.pipeline.state import PipelineState

from backend.src.job_discovery import discover_jobs

from backend.src.cv_matching import match_jobs_to_cv

from backend.agents.company_research import research_company

from backend.agents.email_hunter import find_company_contact

from backend.agents.email_draft import generate_email

from backend.utils.logger import get_logger

logger = get_logger("graph")


def job_discovery_node(state: PipelineState):

    logger.info( "Running Job Discovery")

    jobs = discover_jobs(
        state["job_preference"]
    )

    state["raw_jobs"] = jobs
    state["current_node"] = "job_discovery"

    return state


def cv_matching_node(
    state: PipelineState
):

    logger.info(
        "Running CV Matching"
    )

    matched_jobs = match_jobs_to_cv(
        cv_text=state["cv_text"],
        jobs=state["raw_jobs"]
    )

    state["matched_jobs"] = matched_jobs
    state["current_node"] = "cv_matching"

    return state


def company_research_node(
    state: PipelineState
):

    logger.info(
        "Running Company Research"
    )

    company_profiles = {}

    for job in state["matched_jobs"]:

        domain = job["domain"]

        if domain not in company_profiles:

            company_profiles[domain] = (
                research_company(
                    job["company_name"]
                )
            )

    state["company_profiles"] = company_profiles
    state["current_node"] = "company_research"

    return state


def contact_discovery_node(
    state: PipelineState
):

    logger.info(
        "Running Contact Discovery"
    )

    contacts = {}

    for domain in state[
        "company_profiles"
    ]:

        contacts[domain] = (
            find_company_contact(
                domain
            )
        )

    state["contacts"] = contacts
    state["current_node"] = "contact_discovery"

    return state


def email_draft_node(
    state: PipelineState
):

    logger.info(
        "Running Email Drafting"
    )

    email_drafts = {}

    for job in state[
        "matched_jobs"
    ]:

        domain = job["domain"]

        profile = state[
            "company_profiles"
        ][domain]

        contact = state[
            "contacts"
        ][domain]

        email_drafts[domain] = (
            generate_email(
                company_profile=profile,
                contact=contact,
                cv_text=state["cv_text"],
                job_title=job[
                    "job_title"
                ]
            )
        )

    state["email_drafts"] = (
        email_drafts
    )

    state["current_node"] = (
        "email_draft"
    )

    return state


graph = StateGraph(
    PipelineState
)

graph.add_node(
    "job_discovery",
    job_discovery_node
)

graph.add_node(
    "cv_matching",
    cv_matching_node
)

graph.add_node(
    "company_research",
    company_research_node
)

graph.add_node(
    "contact_discovery",
    contact_discovery_node
)

graph.add_node(
    "email_draft",
    email_draft_node
)

graph.set_entry_point(
    "job_discovery"
)

graph.add_edge(
    "job_discovery",
    "cv_matching"
)

graph.add_edge(
    "cv_matching",
    "company_research"
)

graph.add_edge(
    "company_research",
    "contact_discovery"
)

graph.add_edge(
    "contact_discovery",
    "email_draft"
)

graph.add_edge(
    "email_draft",
    END
)

pipeline_graph = (
    graph.compile()
)