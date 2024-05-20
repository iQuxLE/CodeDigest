import os
from pydantic import BaseModel


class Config(BaseModel):
    project_root: str = os.getenv('PROJECT_ROOT', '/path/to/project')
    output_file: str = os.getenv('OUTPUT_FILE', 'output.txt')
    openai_api_key: str = os.getenv('OPENAI_API_KEY')
    description_prompt: str = ("You are a software engineer and Python expert. "
                               "If any functions in the following file lack descriptions, generate them.")
    summary_prompt: str = ("You are a software engineer and Python expert. Summarize the following file, "
                           "including its functions, classes, and overall content. Put the summary on top of each "
                           "class as comments in the following format:\n\n"
                           "#############################################\n"
                           "\"\"\"\nsummary\n\"\"\"\nclass:")
    description_engine: str = "gpt-4o-2024-05-13" #gpt-4-0125-preview
    summary_engine: str = "gpt-4o-2024-05-13" # gpt-4-0125-preview
    max_tokens: int = 4096


config = Config()
