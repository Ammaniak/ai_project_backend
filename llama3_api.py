import requests
import os
from dotenv import load_dotenv
from together import Together

load_dotenv()

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def summarise_text(transcript: str)->str:
    response = client.chat.completions.create(
        model = "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages = [{"role": "user", "content":f"Summarize this transcript:\n{transcript}"}]
    )
    
    return response.choices[0].message.content
