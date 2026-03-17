import os
import argparse

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Error: Api key not found!!!!")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="coding-agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

response = client.models.generate_content(
    model='gemini-2.5-flash-image',
    contents=args.user_prompt
)

if response.usage_metadata == None:
    raise RuntimeError("Usage metadata none failed api request!!!")

#print(f"User prompt: {response.candidates[0].content}")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(response.text)

