from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InvokeRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Hello from your FastAPI backend on Render!"}

@app.post("/api/agentfy/invoke")
def invoke_agent(request: InvokeRequest):
    return {"response": f"Agent received: {request.prompt}"}
