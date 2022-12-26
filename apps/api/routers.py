# app/api/routers.py
from fastapi import APIRouter

# Две длинных строчки импортов заменяем на одну короткую.
from api.endpoints import meeting_room_router, reservation_router

main_router = APIRouter()
main_router.include_router(meeting_room_router)
main_router.include_router(reservation_router)
