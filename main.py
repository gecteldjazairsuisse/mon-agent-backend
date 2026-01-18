from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ⚠️ Ajoute cette ligne pour autoriser les requêtes depuis Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mon-agent-frontend.vercel.app"],  # Remplace par ton domaine Vercel
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InvokeRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Hello from your FastAPI backend on Render!"}

@app.post("/api/agentfy/invoke")
def invoke_agent(request: InvokeRequest):
    return {"response": f"Agent received: {request.prompt}"}
