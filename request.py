import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.perplexity.ai/chat/completions"
token = os.getenv("PERPLEXITY_API_KEY")

payload = {
    "model": "sonar",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "what is the value of the euro as of May 1, 2025?"
        }
    ]
}
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)