from datetime import datetime, timedelta
from .intents import IntentType
from .dates import extract_date


def handle_note(text: str) -> dict:
    return {
        "title": text[:255],
        "content": text
    }



def handle_task(text: str) -> dict:
    return {
        "title": text[:255],
        "description": ""
    }



def handle_reminder(text: str) -> dict:
    return {
        "text": text,
        "date": extract_date(text)
    }

