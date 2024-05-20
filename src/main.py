from fastapi import FastAPI
from app.api.endpoints import router as api_router
from dotenv import load_dotenv
import os
import openai
from src.config import config

# Load environment variables from a .env file if it exists
load_dotenv()

app = FastAPI()

# Include the API router
app.include_router(api_router)

# Set OpenAI API key from environment variable or config file
openai.api_key = os.getenv('OPENAI_API_KEY', config.openai_api_key)
