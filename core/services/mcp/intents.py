from enum import Enum


class IntentType(Enum):
    NOTE = "note"
    TASK = "task"
    REMINDER = "reminder"
    UNKNOWN = "unknown"