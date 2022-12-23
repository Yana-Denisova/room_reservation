from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Перспективный сервис для бизнеса'
    database_url: str = 'sqlite+aiosqlite:///../fastapi.db'

    class Config:
        env_file = '.env'

settings = Settings()