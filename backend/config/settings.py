from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    SUPABASE_URL: str

    SUPABASE_SERVICE_KEY: str

    JWT_SECRET_KEY: str

    OPENAI_API_KEY: str

    REDIS_URL: str

<<<<<<< Updated upstream
=======
    GROQ_API_KEY: str 

    TAVILY_API_KEY: str
    
    HUNTER_API_KEY: str

    APIFY_API_TOKEN: str

    RAPIDAPI_KEY: str

>>>>>>> Stashed changes
    class Config:
        env_file = ".env"


settings = Settings()