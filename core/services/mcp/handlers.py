from .types import MCPResult
from .intents import IntentType
from .dates import extract_date

def handle_note(text: str) -> MCPResult:
    return MCPResult(
        intent=IntentType.NOTE,
        data={
            "title": text[:255],
            "content": text
        },
        missing=[]
    )

def handle_task(text: str) -> MCPResult:
    return MCPResult(
        intent=IntentType.TASK,
        data={
            "title": text[:255],
            "description": ""
        },
        missing=[]
    )



def handle_reminder(text: str) -> MCPResult:
    date = extract_date(text)

    if not date:
        return MCPResult(
            intent=IntentType.REMINDER,
            data={"text": text},
            missing=["date"],
            question="Когда мне тебя напомнить?"
        )

    return MCPResult(
        intent=IntentType.REMINDER,
        data={
            "text": text,
            "remind_at": date
        },
        missing=[]
    )

