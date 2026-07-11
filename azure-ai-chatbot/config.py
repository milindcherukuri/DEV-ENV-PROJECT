import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv("AZURE_LANGUAGE_ENDPOINT")
AZURE_KEY = os.getenv("AZURE_LANGUAGE_KEY")