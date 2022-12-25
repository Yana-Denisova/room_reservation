# app/crud/reservation.py
from crud.base import CRUDBase
from models.reservation import Reservation

reservation_crud = CRUDBase(Reservation)