from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:your_password@localhost:5432/contract_db"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()