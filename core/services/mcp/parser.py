import re
from .intents import IntentType
from .dates import extract_date


REMINDER_KEYWORDS = [
    'напомни',
    'напоминание',
    'напомнить',
]

TASK_KEYWORDS = [
    'задача',
    'сделать',
    'выполнить',
    'нужно',
]


def detect_intent(text: str) -> IntentType:
    lowered = text.lower()

    for word in REMINDER_KEYWORDS:
        if word in lowered:
            return IntentType.REMINDER

    for word in TASK_KEYWORDS:
        if word in lowered:
            return IntentType.TASK

    return IntentType.NOTE

from .handlers import handle_note, handle_task, handle_reminder


def parse(text: str) -> dict:
    intent = detect_intent(text)

    if intent == IntentType.REMINDER:
        data = handle_reminder(text)
    elif intent == IntentType.TASK:
        data = handle_task(text)
    else:
        data = handle_note(text)

    return {
        "intent": intent,
        "data": data
    }


