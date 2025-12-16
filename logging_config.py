from loguru import logger
import sys
from pathlib import Path

# Log directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Remove default logger
logger.remove()

# Common format
LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)

# Console logging
logger.add(
    sys.stdout,
    level="INFO",
    format=LOG_FORMAT,
    colorize=True,
)

# File logging (rotating)
logger.add(
    LOG_DIR / "app.log",
    level="DEBUG",
    format=LOG_FORMAT,
    rotation="10 MB",      # rotate when file reaches 10MB
    retention="7 days",    # keep logs for 7 days
    compression="zip",     # compress old logs
    enqueue=True,          # safe for multi-thread/process
    backtrace=True,
    diagnose=True,
)

def get_logger():
    """Import-safe logger accessor"""
    return logger
