from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Перспективный сервис для бизнеса'

    class Config:
        env_file = '.env'

settings = Settings()
