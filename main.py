from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import ValidationError
from resume_parser import parse_resume
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="LinkedInForge Agent API",
    description="API for the AI agent that automates LinkedIn profile updates based on a resume.",
    version="1.0.0"
)

@app.get("/")
def root():
    """Redirect to the Swagger API documentation."""
    return RedirectResponse(url="/docs")

@app.post("/parse_resume")
async def parse_resume_endpoint(file: UploadFile = File(...)):
    """
    Endpoint to upload a PDF resume and return structured JSON using Gemini.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    try:
        contents = await file.read()
        parsed_resume = parse_resume(contents)
        return parsed_resume.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run_workflow")
async def run_workflow_endpoint(linkedin_url: str, file: UploadFile = File(...)):
    """
    Endpoint to trigger the full LinkedInForge workflow.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    try:
        from workflow import app_workflow
        
        contents = await file.read()
        
        # Initial state for the LangGraph workflow
        initial_state = {
            "resume_pdf_bytes": contents,
            "resume_data": None,
            "linkedin_url": linkedin_url,
            "scraped_data": None,
            "gap_report": None,
            "approved": False
        }
        
        # Execute the workflow
        # Note: LangGraph async support is used by default if nodes are async
        result = await app_workflow.ainvoke(initial_state)
        
        # Return the gap report
        if result.get("gap_report"):
            return result["gap_report"].model_dump()
        return {"status": "completed", "result": "No gap report generated."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
