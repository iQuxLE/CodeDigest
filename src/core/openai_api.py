import openai
from config import config

openai.api_key = config.openai_api_key
print(f"OpenAI API Key: {config.openai_api_key}")

if not openai.api_key:
    raise ValueError("OpenAI API key is not set")

openai.api_key = config.openai_api_key


"""
This script uses the OpenAI API to generate descriptions and summaries for functions 
in a given file content. It includes two main functions:
1. generate_function_descriptions: Generates descriptions for functions within the provided 
   file content using a specified OpenAI model and prompt.
2. generate_file_summary: Generates a summary for the entire file content using a specified 
   OpenAI model and prompt.
Both functions make API calls to OpenAI's chat completion model and return the resulting text. 
The OpenAI API key is required and fetched from a configuration file.
"""

def generate_function_descriptions(file_path, content):
    """
    Generates descriptions for functions in the given file content using the OpenAI API.

    Args:
        file_path (str): The path to the file for which function descriptions are being generated.
        content (str): The content of the file.

    Returns:
        str: A description of the functions found within the given content.
    """

    response = openai.ChatCompletion.create(
        model=config.description_engine,
        messages=[
            {"role": "system", "content": config.description_prompt},
            {"role": "user", "content": content}
        ],
        max_tokens=config.max_tokens
    )
    return response.choices[0].message.content.strip()

def generate_file_summary(file_path, content):
    """
    Generates a summary of the given file content using the OpenAI API.

    Args:
        file_path (str): The path to the file for which a summary is being generated.
        content (str): The content of the file.

    Returns:
        str: A summary of the given content.
    """
    response = openai.ChatCompletion.create(
        model=config.summary_engine,
        messages=[
            {"role": "system", "content": config.summary_prompt},
            {"role": "user", "content": content}
        ],
        max_tokens=config.max_tokens
    )
    return response.choices[0].message.content.strip()