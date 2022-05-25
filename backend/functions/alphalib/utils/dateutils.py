from datetime import datetime, timezone


def get_current_time_utc() -> datetime:
    """Get current time in iso format

    Returns:
        str: current time in iso format
    """
    return datetime.utcnow().replace(tzinfo=timezone.utc, microsecond=0)  # .isoformat()


def convert_iso_format(dt: datetime):
    """Convert datetime object to iso format

    Args:
        dt (datetime): datetime object

    Returns:
        str: datetime object in iso format
    """
    return dt.isoformat()


def parse_datetime(iso_time: str) -> datetime:
    """Get datetime object from iso time string

    Args:
        iso_time (str): ISO time string

    Returns:
            datetime: datetime object
    """
    if str is None:
        return datetime.min
    return datetime.fromisoformat(iso_time)


def days_diff(start_time: datetime, end_time: datetime) -> int:
    """Difference in days between two datetime objects

    Args:
        start_time (datetime): start time
        end_time (datetime): end time

    Returns:
        int: difference in days
    """
    if start_time is None or end_time is None:
        return 999
    diff = end_time - start_time
    return round(diff.total_seconds() / 60 / 24)
