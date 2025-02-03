from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key is missing! Make sure it's set in the .env file.")

print("API Key loaded successfully!")
