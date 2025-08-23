import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
from call_function import available_functions
from call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from genai-project!")

    verbose = "--verbose" in sys.argv

    if len(sys.argv) < 2:
        print("Error - Please provide a prompt")
        sys.exit(1)


    if verbose:
        verbose_flag_postion = sys.argv.index("--verbose")
        user_prompt = " ".join(sys.argv[1:verbose_flag_postion])
    else:
        user_prompt = " ".join(sys.argv[1:])

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]


    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
    )
    )
        

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count


    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    

    if not response.function_calls:
        print(response.text)
    else:
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose=verbose)


            function_response = getattr(
                function_call_result.parts[0], 
                "function_response", 
                None
            )
            if not function_response or not hasattr(function_response, "response"):
                raise Exception("Function did not return a valid response.")

            if verbose:
                print(f"-> {function_response.response}")


if __name__ == "__main__":
    main()
