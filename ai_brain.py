import json
from pydantic import BaseModel
import ollama
from models import ResumeKnowledgeBase

class GapReport(BaseModel):
    missing_skills: list[str]
    missing_projects: list[str]
    missing_experience: list[str]
    outdated_descriptions: list[str]
    recommended_about_section: str
    recommended_experience_updates: dict[str, str] # Company/Role -> New description

def analyze_profile_gap(resume_data: ResumeKnowledgeBase, scraped_linkedin_data: dict) -> GapReport:
    """
    Compares the parsed resume data against scraped LinkedIn profile data
    and generates a GapReport with recommended updates using Ollama.
    """
    prompt = f"""
    You are an expert career coach and AI profile analyzer.
    Compare the candidate's parsed Resume data against their current LinkedIn profile data.
    Identify missing skills, missing projects, missing experience, and outdated descriptions.
    Then, generate a new optimized "About" section, and suggest new descriptions for experiences that need updates to match the resume.

    Resume Data:
    {resume_data.model_dump_json(indent=2)}

    Current LinkedIn Profile Data:
    {json.dumps(scraped_linkedin_data, indent=2)}
    """
    
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}],
        format=GapReport.model_json_schema()
    )
    
    return GapReport(**json.loads(response['message']['content']))
