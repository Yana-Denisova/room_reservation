from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Перспективный сервис для бизнеса'
    database_url: str = 'sqlite+aiosqlite:///../fastapi.db'
    secret: str = 'secret'

    class Config:
        env_file = '.env'

settings = Settings()
