from dataclasses import dataclass
from typing import Optional, Dict, List
from .intents import IntentType


@dataclass
class MCPResult:
    intent: IntentType
    data: Dict
    missing: List[str]
    question: Optional[str] = None
