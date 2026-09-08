from fastapi import FastAPI,HTTPException
from src.services.llm_query import llm_response 
from src.services.query_input import input_query
from pydantic import BaseModel,Field
app=FastAPI(title="Basic customer RAG",description="get your question answered by our agent")

class question(BaseModel):
    query:str=Field(...,description="Your question rgarding the policy document")

@app.post("/ask")
def ask_question(request:question):
    query=request.query 
    return llm_response(query)



@app.get("/")
def get_health():
    return {"status":"ok"}