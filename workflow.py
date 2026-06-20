from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from models import ResumeKnowledgeBase
from ai_brain import analyze_profile_gap, GapReport
from browser_agent import scrape_linkedin_profile
from resume_parser import parse_resume

# Define the state dictionary
class AgentState(TypedDict):
    resume_pdf_bytes: Optional[bytes]
    resume_data: Optional[ResumeKnowledgeBase]
    linkedin_url: Optional[str]
    scraped_data: Optional[dict]
    gap_report: Optional[GapReport]
    approved: bool

# Define nodes
def parse_resume_node(state: AgentState):
    print("--- Parsing Resume ---")
    if state["resume_pdf_bytes"]:
        data = parse_resume(state["resume_pdf_bytes"])
        return {"resume_data": data}
    return {}

async def scrape_linkedin_node(state: AgentState):
    print("--- Scraping LinkedIn ---")
    if state["linkedin_url"]:
        data = await scrape_linkedin_profile(state["linkedin_url"])
        return {"scraped_data": data}
    return {}

def analyze_gaps_node(state: AgentState):
    print("--- Analyzing Gaps ---")
    if state.get("resume_data") and state.get("scraped_data"):
        report = analyze_profile_gap(state["resume_data"], state["scraped_data"])
        return {"gap_report": report}
    return {}

def user_approval_node(state: AgentState):
    print("--- Waiting for User Approval ---")
    # In a real app, this would pause and wait for an API call.
    # We'll just assume true for MVP, or you can mock it.
    return {"approved": True}

def update_profile_node(state: AgentState):
    print("--- Updating Profile ---")
    if state.get("approved") and state.get("gap_report"):
        print("Mock: Profile successfully updated using Playwright.")
        # Here we would call another browser_agent function to update the profile
    return {}

# Build the graph
workflow = StateGraph(AgentState)

workflow.add_node("parse_resume", parse_resume_node)
workflow.add_node("scrape_linkedin", scrape_linkedin_node)
workflow.add_node("analyze_gaps", analyze_gaps_node)
workflow.add_node("user_approval", user_approval_node)
workflow.add_node("update_profile", update_profile_node)

workflow.set_entry_point("parse_resume")
workflow.add_edge("parse_resume", "scrape_linkedin")
workflow.add_edge("scrape_linkedin", "analyze_gaps")
workflow.add_edge("analyze_gaps", "user_approval")
workflow.add_edge("user_approval", "update_profile")
workflow.add_edge("update_profile", END)

app_workflow = workflow.compile()
