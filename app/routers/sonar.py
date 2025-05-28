import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.perplexity.ai/chat/completions"
token = os.getenv("PERPLEXITY_API_KEY")

def realtime_request(animal: str, location: str):
    payload = {
    "model": "sonar",
    "messages": [
        {
            "role": "system",
            "content": "You are an expert on animals"
        },
        {
            "role": "user",
            "content": f"I see this animal - {animal} in the wild and I'm not sure if it is dangerous.. I am currently in {location} \
            should I be worried about this animal here?"
        }
    ],
    "web_search_options": {
      "user_location": {
        "country": f"{location}"
            }
        }
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    
    return response.json()['choices'][0]['message']['content']
    