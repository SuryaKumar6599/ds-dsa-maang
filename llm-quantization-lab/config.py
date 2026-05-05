import os
import re
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Load config safely
HF_TOKEN = os.getenv("HF_TOKEN")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "facebook/opt-1.3b")
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "results"))
MODEL_DIR = Path(os.getenv("MODEL_DIR", "models"))
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "50"))
N_THREADS = int(os.getenv("N_THREADS", "8"))

#  Sanitization helpers
def mask_token(text: str) -> str:
    if HF_TOKEN and HF_TOKEN in text:
        return text.replace(HF_TOKEN, "***MASKED_HF_TOKEN***")
    return text

def sanitize_path(text: str) -> str:
    # Replace absolute home paths with ~/****
    return re.sub(r"/Users/[^/]+/", "~/****/", text)

def sanitize_log(text: str) -> str:
    return sanitize_path(mask_token(str(text)))