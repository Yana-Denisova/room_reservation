# app/main.py

from fastapi import FastAPI

# Импортируем роутер.
from api.meeting_room import router
from core.config import settings

my_app = FastAPI(title=settings.app_title)

# Подключаем роутер.
my_app.include_router(router)