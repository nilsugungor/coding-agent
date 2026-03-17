import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Error: Api key not found!!!!")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="coding-agent")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(
    tools=[available_functions],
    system_instruction=system_prompt,
    temperature=0
    )
)

if response.usage_metadata == None:
    raise RuntimeError("Usage metadata none failed api request!!!")

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if response.candidates[0].content.parts[0].function_call:
    for function_call in response.candidates[0].content.parts:
        if function_call.function_call:
            call = function_call.function_call
            print(f"Calling function: {call.name}({call.args})")
else:
    print(response.text)
