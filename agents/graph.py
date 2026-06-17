from langgraph.graph import StateGraph, START, END
from agents.state import AgentState
from agents.graph_nodes import (
    planner_node,
    research_node,
    analysis_node,
    report_node
)

graph_builder = StateGraph(AgentState)

graph_builder.add_node("planner",planner_node)
graph_builder.add_node("research",research_node)
graph_builder.add_node("analysis",analysis_node)
graph_builder.add_node("report",report_node)

graph_builder.add_edge(START,"planner")
graph_builder.add_edge("planner","research")
graph_builder.add_edge("research","analysis")
graph_builder.add_edge("analysis","report")
graph_builder.add_edge("report",END)

graph = graph_builder.compile()