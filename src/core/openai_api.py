import openai
from config import config

openai.api_key = config.openai_api_key
print(f"OpenAI API Key: {config.openai_api_key}")

if not openai.api_key:
    raise ValueError("OpenAI API key is not set")

openai.api_key = config.openai_api_key

# def generate_function_descriptions(file_path, content):
#     response = openai.Completion.create(
#         engine=config.description_engine,
#         prompt=f"{config.description_prompt}\n\n{content}\n",
#         max_tokens=config.max_tokens
#     )
#     return response.choices[0].text.strip()
#
# def generate_file_summary(file_path, content):
#     response = openai.Completion.create(
#         engine=config.summary_engine,
#         prompt=f"{config.summary_prompt}\n\n{content}\n",
#         max_tokens=config.max_tokens
#     )
#     return response.choices[0].text.strip()


### OLD API

def generate_function_descriptions(file_path, content):
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
    response = openai.ChatCompletion.create(
        model=config.summary_engine,
        messages=[
            {"role": "system", "content": config.summary_prompt},
            {"role": "user", "content": content}
        ],
        max_tokens=config.max_tokens
    )
    return response.choices[0].message.content.strip()