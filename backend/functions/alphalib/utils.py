from datetime import datetime, timezone


def get_current_time_utc() -> str:
    """Get current time in iso format

    Returns:
        str: current time in iso format
    """
    return datetime.utcnow().replace(tzinfo=timezone.utc, microsecond=0).isoformat()


def parse_datetime(iso_time: str) -> datetime:
    """Get datetime object from iso time string

    Args:
        iso_time (str): ISO time string

    Returns:
            datetime: datetime object
    """
    return datetime.fromisoformat(iso_time)
