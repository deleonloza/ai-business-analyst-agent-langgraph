from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):
    company: str
    plan: str
    research: List[Dict[str, Any]]
    analysis: str
    report: str