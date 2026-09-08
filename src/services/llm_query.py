from openai import OpenAI
from config import Config
import httpx
import json
import httpx2
key=Config.LLM_API_KEY
http_client = httpx.Client(verify=False)
import requests
import json
from query_input import input_query
query=input_query()
from vector_db import retrieval
def llm_response(query:str):    
    if not query:
        return "No question asked" 
    # First API call with reasoning
    #try:
    system_prompt="You are a customer facing support agent,"\
            " and you have to answer customer question according to the retrieved context."\
            " Dont make up any non existing info and answer the customer strictly based on the document"
    response = requests.post(
        verify=False,
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "nvidia/nemotron-3.5-lightning:free",
        "messages": [
            {"role":"system","content":system_prompt},
            
            {
            "role": "user",
            "content": query + "context is" + retrieval(query)
            }
        ],
        "reasoning": {"enabled": False}
    })
    )

    # Extract the assistant message with reasoning_details
    response = response.json()
    #print(response)
    response = response['choices'][0]['message']

    # Preserve the assistant message with reasoning_details
    messages = [
    {"role": "user", "content": "Hi"},
    {
        "role": "assistant",
        "content": response.get('content'),
        #"reasoning_details": response.get('reasoning_details')  # Pass back unmodified
    }
    ]
    l=response['content']
    
    return l
    # except Exception as e:
    #     print("LLM calling may have Failed")        
    #     return str(e.args)

print(llm_response(query))

