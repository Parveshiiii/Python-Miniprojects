from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise Exception("api key is not set. setup your api key in .env file GROQ_API_KEY")

client = Groq(api_key = api_key)

def chat(content: str):
    response = client.chat.completions.create(
        model = "",
        messages = [
            {
                "role": "user",
                "content": content,
            }
        ]
    )
    return response.choices[0].message["content"]
  