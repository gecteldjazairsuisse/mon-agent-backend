from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your FastAPI backend on Render!"}

@app.post("/api/agentfy/invoke")
def invoke_agent(prompt: str):
    return {"response": f"Agent received: {prompt}"}
