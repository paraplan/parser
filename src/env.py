import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

API_URL: Final[str] = os.getenv("SCHEDULE_API_URL", "https://verysecret")
API_KEY: Final[str] = os.getenv("SCHEDULE_API_KEY", "verysecret")
