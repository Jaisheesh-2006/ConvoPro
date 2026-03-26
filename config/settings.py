from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    MONGO_DB_URL: str
    MONGO_DB_NAME: str
    GROQ_API_KEY: str
    GROQ_MODELS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )