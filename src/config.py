from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_DIR = Path(__file__).parent.parent

RAW_DATA_PATH = ROOT_DIR / "data" / "raw_jobs.json"

load_dotenv(ROOT_DIR / ".env")

API_ID = os.getenv("JOB_API_ID")
API_KEY = os.getenv("JOB_API_KEY")
API_URL = os.getenv("JOB_API_URL")

if not API_ID:
    raise ValueError("API ID Missing!")
elif not API_KEY:
    raise ValueError("API Key Missing!")
elif not API_URL:
    raise ValueError("API Url Missing!")
