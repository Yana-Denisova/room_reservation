# app/models/meeting_room.py

# Импортируем из Алхимии нужные классы.
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

# Импортируем базовый класс для моделей.
from apps.core.db import Base


class MeetingRoom(Base):
    # Имя переговорки должно быть не больше 100 символов,
    # уникальным и непустым.
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    # Установите связь между моделями через функцию relationship.
    reservations = relationship('Reservation', cascade='delete')
