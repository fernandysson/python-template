from fastapi import APIRouter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/log/{level}")
def log_message(level: str):
    """Log a message at the specified level."""
    message = f"Log message at {level} level"
    if level.lower() == "info":
        logger.info(message)
    elif level.lower() == "debug":
        logger.debug(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    elif level.lower() == "critical":
        logger.critical(message)
    else:
        return {"error": "Invalid log level"}
    return {"message": message}