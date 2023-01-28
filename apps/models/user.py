from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from apps.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass
