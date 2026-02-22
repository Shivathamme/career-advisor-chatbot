import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('gemini_class')

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY ot found in .env file")