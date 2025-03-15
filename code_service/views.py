from fastapi import FastAPI
import openai
import os
from fastapi import APIRouter
from .llm_service import analyze_code 


router = APIRouter()

@router.post("/analyze/start")
async def start_analysis(repo_url: str):
    import git
    repo = git.Repo.clone_from(repo_url, "/tmp/repo")
    job_id = "abc123" 
    return {"job_id": job_id}

@router.post("/analyze/function")
async def analyze_function(job_id: str, function_name: str):
    function_code = "def add(a, b): return a + b"  
    return await analyze_code(function_code)


app = FastAPI()

# API Key برای OpenAI
openai.api_key = os.getenv("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")

@app.post("/analyze")
async def analyze_code(function_code: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following Python function: {function_code}",
        max_tokens=100
    )
    suggestions = response['choices'][0]['text']
    return {"suggestions": suggestions.split('\n')}
