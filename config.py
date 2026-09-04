import requests
import json

response = requests.post(
  verify=False,
  url="https://openrouter.ai/api/v1/rerank",
  headers={
    
    "Authorization": "Bearer <OPENROUTER_API_KEY>",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "nvidia/llama-nemotron-rerank-vl-1b-v2:free",
    "query": "a photograph of a cat",
    # Documents can mix images and text. Images are remote URLs or base64 data URIs.
    "documents": [
      {"image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"},
      {"text": "A fluffy cat sitting on a windowsill in the sun."},
      {"text": "A street map of downtown Berlin."}
    ],
    "top_n": 3
  })
)

results = response.json()
for result in results["results"]:
  document = result["document"]
  source = document.get("image") or document.get("text")
  print(f"Index: {result['index']}, Score: {result['relevance_score']}, Source: {source}")