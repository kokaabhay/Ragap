from openai import OpenAI
import os
import httpx
import json
import httpx2
from dotenv import load_dotenv
load_dotenv()
key=os.getenv("LLM_API_KEY")
http_client = httpx.Client(verify=False)
import requests
import json

def llm_response():
    # First API call with reasoning
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
            {
            "role": "user",
            "content": "Hi"
            }
        ],
        "reasoning": {"enabled": False}
    })
    )

    # Extract the assistant message with reasoning_details
    response = response.json()
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
    print(l)
    return l

