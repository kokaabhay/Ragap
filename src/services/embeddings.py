import requests
import json
from src.services.config import Config
key=Config.LLM_API_KEY
from src.services.extract_from_pdf import chunking,filepath
from openai import OpenAI
lot=chunking(filepath)
def embed(lot:list):
    if not lot:
        print("Chunking list is empty")
        #revisit this return part
        return
    try:
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=key,
        )

        embedding = client.embeddings.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        model="liquid/lfm-2.5-embedding-350m:free",
        #input="Your text string goes here",
        input= lot, # batch embeddings also supported!
        encoding_format="float"
        )
        print(embedding.data[0].embedding)
        embeddings=embedding.data[0].embedding
        return embeddings
    except Exception as e:
        print(Exception,"Calling Embedding model may have failed")
        return str(e)
    
    
#print(len(embed(chunking(filepath))))
