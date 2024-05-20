import openai
from config import config


openai.api_key = config.openai_api_key

def generate_function_descriptions(file_path, content):
    response = openai.Completion.create(
        engine=config.description_engine,
        prompt=f"{config.description_prompt}\n\n{content}\n",
        max_tokens=config.max_tokens
    )
    return response.choices[0].text.strip()

def generate_file_summary(file_path, content):
    response = openai.Completion.create(
        engine=config.summary_engine,
        prompt=f"{config.summary_prompt}\n\n{content}\n",
        max_tokens=config.max_tokens
    )
    return response.choices[0].text.strip()
