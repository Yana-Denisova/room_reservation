from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.reservation import ReservationCreate, ReservationDB
from crud.reservation import reservation_crud
from api.validators import check_reservation_intersections, check_meeting_room_exists
from core.db import get_async_session


router = APIRouter()

@router.post(
    '/',
    response_model=ReservationDB
)
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    # Так как валидатор принимает **kwargs, 
        # аргументы должны быть переданы с указанием ключей.
    await check_reservation_intersections(**reservation.dict(), session=session)
    new_reservation = await reservation_crud.create(reservation, session)
    return new_reservation
