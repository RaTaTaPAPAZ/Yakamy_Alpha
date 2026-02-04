from datetime import datetime, timedelta
import re


def extract_date(text: str):
    text = text.lower()
    now = datetime.now()

    if "сегодня" in text:
        return now

    if "завтра" in text:
        return now + timedelta(days=1)

    match = re.search(r"через (\d+) (час|часа|часов)", text)
    if match:
        hours = int(match.group(1))
        return now + timedelta(hours=hours)

    match = re.search(r"через (\d+) (день|дня|дней)", text)
    if match:
        days = int(match.group(1))
        return now + timedelta(days=days)

    return None
