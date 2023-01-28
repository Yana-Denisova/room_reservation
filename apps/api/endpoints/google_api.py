from datetime import datetime

from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.core.db import get_async_session
from apps.core.google_client import get_service
from apps.core.user import current_superuser
from apps.services.google_api import (spreadsheets_create,
                                      set_user_permissions,
                                      spreadsheets_update_value)
from apps.crud.reservation import reservation_crud

router = APIRouter()


@router.post(
    '/',
    response_model=list[dict[str, int]],
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        from_reserve: datetime,
        to_reserve: datetime,
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)

):
    reservations = await reservation_crud.get_count_res_at_the_same_time(
        from_reserve, to_reserve, session
    )
    spreadsheetid = await spreadsheets_create(wrapper_services)
    await set_user_permissions(spreadsheetid, wrapper_services)
    await spreadsheets_update_value(spreadsheetid,
                                    reservations,
                                    wrapper_services)
    print(f'Создан документ: '
          f'https://docs.google.com/spreadsheets/d/{spreadsheetid}')
    return reservations
