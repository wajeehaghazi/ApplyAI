from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    SUPABASE_URL: str

    SUPABASE_SERVICE_KEY: str

    JWT_SECRET_KEY: str

    OPENAI_API_KEY: str

    REDIS_URL: str

    class Config:
        env_file = ".env"


settings = Settings()