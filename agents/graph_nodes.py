from agents.state import AgentState
from agents.planner import create_plan
from agents.researcher import research_company
from agents.analyst import analyze_research
from agents.reporter import generate_report


def planner_node(state: AgentState):
    company = state["company"]
    plan = create_plan(company)

    return {
        "plan": plan
    }


def research_node(state: AgentState):
    company = state["company"]
    research = research_company(company)

    return {
        "research": research
    }


def analysis_node(state: AgentState):
    company = state["company"]
    research = state["research"]
    analysis = analyze_research(company, research)

    return {
        "analysis": analysis
    }


def report_node(state: AgentState):
    company = state["company"]
    analysis = state["analysis"]
    report = generate_report(company, analysis)

    return {
        "report": report
    }