# app/api/meeting_room.py

# Импортируем класс Depends.
from fastapi import APIRouter, Depends, HTTPException

# Импортируем класс асинхронной сессии для аннотации параметра.
from sqlalchemy.ext.asyncio import AsyncSession

# app/api/meeting_room.py

# Импортируем класс Depends.
from fastapi import APIRouter, Depends, HTTPException

# Импортируем класс асинхронной сессии для аннотации параметра.
from sqlalchemy.ext.asyncio import AsyncSession

# Импортируем асинхронный генератор сессий.
from core.db import get_async_session
from crud.meeting_room import create_meeting_room, get_room_id_by_name
from schemas.meeting_room import MeetingRoomCreate, MeetingRoomDB

router = APIRouter()


@router.post(
    '/meeting_rooms/',
    response_model=MeetingRoomDB,
    response_model_exclude_none=True,
)
async def create_new_meeting_room(
        meeting_room: MeetingRoomCreate,
        # Указываем зависимость, предоставляющую объект сессии, как параметр функции.
        session: AsyncSession = Depends(get_async_session),
):
    # Вторым параметром передаём сессию в CRUD-функцию:
    room_id = await get_room_id_by_name(meeting_room.name, session)
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )
    # Вторым параметром передаём сессию в CRUD-функцию:
    new_room = await create_meeting_room(meeting_room, session)
    return new_room