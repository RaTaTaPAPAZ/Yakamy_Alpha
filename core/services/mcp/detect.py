from .handlers import handle_note, handle_task, handle_reminder
import re
from .intents import IntentType
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