from .detect import detect_intent
from .handlers import handle_note, handle_task, handle_reminder
from .types import MCPResult
from .intents import IntentType

def parse(text: str) -> MCPResult:
    intent = detect_intent(text)

    if intent == IntentType.REMINDER:
        return handle_reminder(text)

    if intent == IntentType.TASK:
        return handle_task(text)

    return handle_note(text)

