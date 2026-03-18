import logging
from datetime import datetime
from pathlib import Path

# إعداد اللوق
LOG_FILE = Path("logs.txt")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_event(message: str):
    """
    Save logs to file + console
    """
    timestamp = datetime.utcnow().isoformat()
    log_line = f"{timestamp} - {message}\n"

    # طباعة في الكونسول
    logging.info(message)

    # حفظ في ملف
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_line)


def safe_get(data: dict, *keys, default=None):
    """
    Safely extract nested values from dict
    Example:
    safe_get(update, 'message', 'chat', 'id')
    """
    for key in keys:
        if not isinstance(data, dict):
            return default
        data = data.get(key)
        if data is None:
            return default
    return data


def is_admin(user_id: int, developer_id: int) -> bool:
    """
    Check if user is admin
    """
    return user_id == developer_id


def format_error(e: Exception) -> str:
    """
    Format error message
    """
    return f"{type(e).__name__}: {str(e)}"
