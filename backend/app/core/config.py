from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

class Settings:
    def __init__(self):
        self.database_url: str = os.getenv("DATABASE_URL", "")
        self.firebase_cred_path: str = os.getenv("FIREBASE_CRED_PATH", "")
        self.gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
        self.rentcast_api_key: str = os.getenv("RENTCAST_API_KEY", "")
        self.project_name: str = "Revest"

        self.cors_origins: List[str] = [
            origin.strip()
            for origin in os.getenv("CORS_ORIGINS", "https://localhost:3000").split(",")
        ]

settings = Settings()