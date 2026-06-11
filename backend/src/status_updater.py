from backend.utils.logger import get_logger

logger = get_logger("status_updater")

def update_status(
    state: dict,
    node_name: str) -> dict:

    state["current_node"] = (
        node_name
    )

    logger.info(f"Current node: {node_name}")

    return state