from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from schemas.reservation import ReservationCreate, ReservationDB
from crud.reservation import reservation_crud
from api.validators import (
    check_meeting_room_exists,
    check_reservation_before_edit,
    check_reservation_intersections,
)
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


@router.get(
    '/',
    response_model=list[ReservationDB],
)
async def get_all_reservations(
        session: AsyncSession = Depends(get_async_session),
):
    all_reservations = await reservation_crud.get_multi(session)
    return all_reservations


@router.delete('/{reservation_id}', response_model=ReservationDB)
async def delete_reservation(
        reservation_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    reservation = await check_reservation_before_edit(
        reservation_id, session
    )
    reservation = await reservation_crud.remove(
        reservation, session
    )
    return reservation
