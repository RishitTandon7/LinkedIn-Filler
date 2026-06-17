import os
from io import BytesIO
from PyPDF2 import PdfReader
import ollama
from pydantic import BaseModel
import json
from models import ResumeKnowledgeBase

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extracts text from a PDF file."""
    reader = PdfReader(BytesIO(pdf_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def parse_resume(pdf_bytes: bytes) -> ResumeKnowledgeBase:
    """Parses a resume PDF and returns a structured object using Ollama."""
    text = extract_text_from_pdf(pdf_bytes)
    
    prompt = f"""
    You are an expert resume parser. Analyze the following resume text and extract the information into the requested JSON schema.
    If any information is missing, use empty arrays or omit the optional fields.

    Resume Text:
    {text}
    """
    
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}],
        format=ResumeKnowledgeBase.model_json_schema()
    )
    
    # Parse the JSON response
    parsed_json = json.loads(response['message']['content'])
    return ResumeKnowledgeBase(**parsed_json)
