import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
key=os.getenv("LLM_API_KEY")

#user_query later will have a different input
from query_input import input_query
user_query=input_query()
def reranking(query=user_query):
  try:
    response = requests.post(
      verify=False,
      url="https://openrouter.ai/api/v1/rerank",
      headers={
        
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
      },
      data=json.dumps({
        "model": "nvidia/llama-nemotron-rerank-vl-1b-v2:free",
        "query": query,
        # Documents can mix images and text. Images are remote URLs or base64 data URIs.
        #if need to parse files then this message shows up in terminal "This request requires at least $0.50 in balance for files" code 402
        "documents": [      
          {"text": "A fluffy cat sitting on a windowsill in the sun."},
          {"text": "A street map of downtown Berlin."}
        ],
        "top_n": 3
      })
    )

    results = response.json()
    # currently storing some of the output in a list and calling it metadata 
    metadata=[]
    for result in results["results"]:
      document = result["document"]      
      source = document.get("image") or document.get("text") 
      metadata.append({"index":result['index'],"Score":result['relevance_score'],"Source":{source}})     
      print(f"Index: {result['index']}, Score: {result['relevance_score']}, Source: {source}")
      return metadata
    
  except Exception as e:
    print("Calling Reranking may have failed ", str(e.args))
    return []
    

print(reranking())