from pydantic import BaseModel
from typing import List, Optional

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]
    link: Optional[str] = None

class SkillCategory(BaseModel):
    category: str
    skills: List[str]

class Certification(BaseModel):
    name: str
    issuer: str
    date_issued: Optional[str] = None
    url: Optional[str] = None

class Achievement(BaseModel):
    title: str
    description: str
    date: Optional[str] = None

class Experience(BaseModel):
    role: str
    company: str
    start_date: str
    end_date: Optional[str] = None
    description: str
    skills_used: List[str] = []

class Education(BaseModel):
    degree: str
    institution: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    gpa: Optional[str] = None

class ResumeKnowledgeBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin_url: Optional[str] = None
    summary: str
    projects: List[Project] = []
    skills: List[SkillCategory] = []
    certifications: List[Certification] = []
    achievements: List[Achievement] = []
    experience: List[Experience] = []
    education: List[Education] = []
